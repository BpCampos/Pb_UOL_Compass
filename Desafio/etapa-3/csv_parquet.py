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

# DataFrame correspondente à dimensão filme
dim_filme = merged_df.select('id', coalesce(col('imdb_id'), col('id')).alias('id_imdb'), coalesce(col(
    'tituloPincipal'), col('title')).alias('titulo'), coalesce(col('tempoMinutos'), col('runtime')).alias('duracao_minutos'))
dim_filme.write.format('parquet').save(f'{target_path}/dim_filme')

# DataFrame correspondente à dimensão tempo
dim_tempo = merged_df.select(col('release_date').alias('data_lancamento'))
dim_tempo = dim_tempo.withColumn(
    'ano_lancamento', year(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.withColumn(
    'mes_lancamento', month(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.withColumn(
    'dia_lancamento', dayofmonth(dim_tempo['data_lancamento']))
dim_tempo = dim_tempo.select(to_date(col('data_lancamento'), 'yyyy-MM-dd').alias('data_lancamento'), 'ano_lancamento',
                             'mes_lancamento', 'dia_lancamento').dropna(how='any', subset=None).dropDuplicates().coalesce(1)
dim_tempo.write.format('parquet').save(f'{target_path}/dim_tempo')

# DataFrame correspondente à dimensão países produtores
dim_paises_prod = merged_df.select(explode('production_countries').alias(
    'part')).select(col('part.name').alias('paises_prod_nome')).dropDuplicates()
dim_paises_prod = dim_paises_prod.withColumn(
    'cod_paises_prod', lit(monotonically_increasing_id()))
dim_paises_prod.write.format('parquet').save(
    f'{target_path}/dim_paises_produtores')

# DataFrame correspondente à dimensão genero
dim_genero = merged_df.select(explode('genres').alias('part')).select(col('part.id').alias('genre_id'), col(
    'part.name').alias('genre_name')).filter((col('part.name') == 'Drama') | (col('part.name') == 'Romance')).dropDuplicates()
dim_genero.write.format('parquet').save(f'{target_path}/dim_genero')

# DataFrame correspondente à tabela fato filme
fato_filme = merged_df.select('id', col('release_date').alias('data_lancamento'), coalesce(col('notaMedia'), col('vote_average')).alias('nota_media'), coalesce(col(
    'numeroVotos'), col('vote_count')).alias('numero_votos'), col('budget').alias('orcamento'), col('popularity').alias('popularidade'), col('revenue').alias('receita'))

# Adiciona os ids da dim_filme à tabela fato_filme
filme_df = merged_df.select(col('id').alias(
    'temp_id'), 'runtime', 'title', 'imdb_id')
fato_filme = fato_filme.join(filme_df, fato_filme.id == filme_df.temp_id, 'left').drop(
    'temp_id', 'runtime', 'title', 'imdb_id')

# Adiciona os ids da dim_paises_produtores à tabela fato_filme
paises_prod_df = merged_df.select(col('id').alias(
    'temp_id'), explode('production_countries.name').alias('names'))
paises_prod_df = paises_prod_df.join(dim_paises_prod, paises_prod_df.names ==
                                     dim_paises_prod.paises_prod_nome, 'left').drop('names', 'paises_prod_nome')
fato_filme = fato_filme.join(
    paises_prod_df, fato_filme.id == paises_prod_df.temp_id, 'left').drop('temp_id')

# Adiciona os ids da dim_genero à tabela fato_filme
genero_df = merged_df.select(col('id').alias('temp_id'), explode(
    'genres.id').alias('genero_id'), col('genero').alias('genero_filme_csv'))
genero_df = genero_df.join(dim_genero, genero_df.genero_id ==
                           dim_genero.genre_id).drop('genre_id', 'genre_name')
genero_df = genero_df.select('temp_id', coalesce(
    col('genero_id'), col('genero_filme_csv')).alias('cod_genero'))
fato_filme = fato_filme.join(
    genero_df, fato_filme.id == genero_df.temp_id, 'left').drop('temp_id')

fato_filme = fato_filme.withColumn(
    'data_lancamento', to_date(col('data_lancamento'), 'yyyy-MM-dd'))
fato_filme = fato_filme.withColumn(
    'nota_media', col('nota_media').cast('double'))
fato_filme = fato_filme.withColumn(
    'numero_votos', col('numero_votos').cast('integer'))

fato_filme = fato_filme.coalesce(1)
fato_filme.write.format('parquet').save(f'{target_path}/fato_filme')

job.commit()
