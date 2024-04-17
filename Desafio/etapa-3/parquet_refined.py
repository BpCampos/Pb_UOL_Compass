import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

target_path = args['S3_TARGET_PATH']

df_csv = spark.read.parquet('s3://desafiofinalcompass/Trusted/*.parquet')

df_json = spark.read.parquet(
    's3://desafiofinalcompass/Trusted/dt=2024-03-26/*.parquet')

for column in [column for column in df_json.columns if column not in df_csv.columns]:
    df_csv = df_csv.withColumn(column, lit(None))

for column in [column for column in df_csv.columns if column not in df_json.columns]:
    df_json = df_json.withColumn(column, lit(None))

merged_df = df_csv.unionByName(df_json)

# DataFrame correspondente à dimensão idioma original
dim_idioma_original = merged_df.select('original_language')
dim_idioma_original = dim_idioma_original.dropna(
    how='any', subset=None).dropDuplicates()
dim_idioma_original = dim_idioma_original.withColumn(
    'cod_idioma_original', lit(monotonically_increasing_id()))
dim_idioma_original = dim_idioma_original.select(
    'cod_idioma_original', col('original_language').alias('idioma_original'))
dim_idioma_original.write.format('parquet').save(
    f'{target_path}/dim_idioma_original')

# DataFrame correspondente à dimensão tempo
dim_tempo = merged_df.select(col('release_date').alias('data_lancamento'))
dim_tempo = dim_tempo.withColumn(
    'ano_lancamento', year(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.withColumn(
    'mes_lancamento', month(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.withColumn(
    'dia_lancamento', dayofmonth(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.select(to_date(col('data_lancamento'), 'yyyy-MM-dd').alias(
    'data_lancamento'), 'ano_lancamento', 'mes_lancamento', 'dia_lancamento')
dim_tempo.write.format('parquet').save(f'{target_path}/dim_tempo')

# DataFrame correspondente à dimensão países produtores
dim_paises_produtores = merged_df.select(explode('production_countries').alias('dict')).select(
    col('dict.iso_3166_1').alias('sigla'), col('dict.name').alias('pais')).dropDuplicates()
dim_paises_produtores = dim_paises_produtores.withColumn(
    'cod_paises_prod', lit(monotonically_increasing_id()))
dim_paises_produtores = dim_paises_produtores.select(
    'cod_paises_prod', 'pais', 'sigla')
dim_paises_produtores.write.format('parquet').save(
    f'{target_path}/dim_paises_produtores')

# DataFrame correspondente à dimensão genero
dim_genero = merged_df.select(explode('genres').alias('dict')).select(col('dict.id').alias(
    'cod_genero'), col('dict.name').alias('genero')).dropDuplicates().sort(col('cod_genero'))
dim_genero.write.format('parquet').save(f'{target_path}/dim_genero')

# DataFrame correspondente à tabela fato filme
fato_filme = merged_df.select('id', coalesce(col('tituloPincipal'), col('title')).alias('titulo_principal'),
                              coalesce(col('tempoMinutos'), col('runtime')).alias('duracao_minutos'), col('release_date').alias(
                                  'data_lancamento'), coalesce(col('notaMedia'), col('vote_average')).alias('nota_media'),
                              coalesce(col('numeroVotos'), col('vote_count')).alias('numero_votos'), col(
                                  'budget').alias('orcamento'), coalesce(col('imdb_id'), col('id')).alias('id_imdb'),
                              col('popularity').alias('popularidade'), col('revenue').alias('receita'))

# Adiciona os ids da dim_paises_produtores à tabela fato_filme
paises_produtores_df = merged_df.select(col('id').alias(
    'temp_id'), explode('production_countries').alias('paises_produtores'))
paises_produtores_df = paises_produtores_df.join(
    dim_paises_produtores, paises_produtores_df.paises_produtores['name'] == dim_paises_produtores.pais)
fato_filme = fato_filme.join(paises_produtores_df, fato_filme.id == paises_produtores_df.temp_id,
                             'left_outer').drop('temp_id', 'paises_produtores', 'pais', 'sigla')

# Adiciona os ids da dim_idioma_original à tabela fato_filme
idioma_original_df = merged_df.select(
    col('id').alias('temp_id'), 'original_language')
idioma_original_df = idioma_original_df.join(
    dim_idioma_original, idioma_original_df.original_language == dim_idioma_original.idioma_original)
fato_filme = fato_filme.join(idioma_original_df, fato_filme.id == idioma_original_df.temp_id, 'left_outer').drop(
    'temp_id', 'original_language', 'idioma_original')

# Adiciona os ids da dim_genero à tabela fato_filme
genero_df = merged_df.select(col('id').alias(
    'temp_id'), explode('genres.name').alias('genero_filme'))
genero_df = genero_df.join(
    dim_genero, genero_df.genero_filme == dim_genero.genero)
fato_filme = fato_filme.join(genero_df, fato_filme.id == genero_df.temp_id, 'left_outer').drop(
    'temp_id', 'genero', 'genero_filme')
fato_filme = fato_filme.withColumnRenamed('cod_genero', 'cod_genero1')

genero_df2 = merged_df.select(col('id').alias(
    'temp_id'), col('genero').alias('nome'))
genero_df2 = genero_df2.join(
    dim_genero, genero_df2.nome == dim_genero.genero).drop('nome')
fato_filme = fato_filme.join(genero_df2, fato_filme.id ==
                             genero_df2.temp_id, 'left_outer').drop('temp_id', 'genero')
fato_filme = fato_filme.withColumnRenamed('cod_genero', 'cod_genero2')

fato_filme = fato_filme.select('*', coalesce(col('cod_genero1'), col(
    'cod_genero2')).alias('cod_genero')).drop('cod_genero1', 'cod_genero2')

fato_filme = fato_filme.withColumn(
    'duracao_minutos', col('duracao_minutos').cast('integer'))
fato_filme = fato_filme.withColumn(
    'data_lancamento', to_date(col('data_lancamento'), 'yyyy-MM-dd'))
fato_filme = fato_filme.withColumn(
    'nota_media', col('nota_media').cast('double'))
fato_filme = fato_filme.withColumn(
    'numero_votos', col('numero_votos').cast('integer'))

fato_filme = fato_filme.coalesce(1)
fato_filme.write.format('parquet').save(f'{target_path}/fato_filme')

job.commit()
