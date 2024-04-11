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
dim_idiomaOriginal = merged_df.select('original_language')
dim_idiomaOriginal = dim_idiomaOriginal.dropna(
    how='any', subset=None).dropDuplicates()
dim_idiomaOriginal = dim_idiomaOriginal.withColumn(
    'codIdiomaOriginal', lit(monotonically_increasing_id()))
dim_idiomaOriginal = dim_idiomaOriginal.select(
    'codIdiomaOriginal', col('original_language').alias('idiomaOriginal'))
dim_idiomaOriginal.write.format('parquet').save(
    f'{target_path}/dim_idiomaOriginal')

# DataFrame correspondente à dimensão idioma falado
dim_idiomaFalado = merged_df.select(explode('spoken_languages').alias('dict')).select(col(
    'dict.english_name').alias('idioma'), col('dict.iso_639_1').alias('abreviacao')).dropDuplicates()
dim_idiomaFalado = dim_idiomaFalado.withColumn(
    'codIdiomaFalado', lit(monotonically_increasing_id()))
dim_idiomaFalado = dim_idiomaFalado.select(
    'codIdiomaFalado', 'idioma', 'abreviacao')
dim_idiomaFalado.write.format('parquet').save(
    f'{target_path}/dim_idiomaFalado')

# DataFrame correspondente à dimensão tempo
dim_tempo = merged_df.select('release_date', 'anoLancamento')
dim_tempo = dim_tempo.withColumn('anoLancamento', coalesce(
    year(dim_tempo['release_date']), col('anoLancamento')))
dim_tempo = dim_tempo.withColumn(
    'mesLancamento', month(dim_tempo['release_date']))
dim_tempo = dim_tempo.withColumn(
    'diaLancamento', dayofmonth(dim_tempo['release_date']))
dim_tempo = dim_tempo.select(col('release_date').alias(
    'dataLancamento'), 'anoLancamento', 'mesLancamento', 'diaLancamento')
dim_tempo.write.format('parquet').save(f'{target_path}/dim_tempo')

# DataFrame correspondente à dimensão países produtores
dim_paisesProdutores = merged_df.select(explode('production_countries').alias('dict')).select(
    col('dict.iso_3166_1').alias('sigla'), col('dict.name').alias('pais')).dropDuplicates()
dim_paisesProdutores = dim_paisesProdutores.withColumn(
    'codPaisesProd', lit(monotonically_increasing_id()))
dim_paisesProdutores = dim_paisesProdutores.select(
    'codPaisesProd', 'pais', 'sigla')
dim_paisesProdutores.write.format('parquet').save(
    f'{target_path}/dim_paisesProdutores')

# DataFrame correspondente à dimensão genero
dim_genero = merged_df.select(explode('genres').alias('dict')).select(col('dict.id').alias(
    'codGenero'), col('dict.name').alias('genero')).dropDuplicates().sort(col('codGenero'))
dim_genero.write.format('parquet').save(f'{target_path}/dim_genero')

# DataFrame correspondente à dimensão produtora
dim_produtora = merged_df.select(explode('production_companies').alias('dict')).select(col('dict.id').alias('codProdutora'), col(
    'dict.name').alias('nome'), col('dict.origin_country').alias('pais')).dropDuplicates().sort(col('codProdutora'))
dim_produtora.write.format('parquet').save(f'{target_path}/dim_produtora')

# DataFrame correspondente à tabela fato filme
fato_filme = merged_df.select('id', coalesce(col('tituloOriginal'), col('original_title')).alias('tituloOriginal'), coalesce(col('tituloPincipal'), col('title')).alias('tituloPrincipal'),
                              coalesce(col('tempoMinutos'), col('runtime')).alias('duracaoMinutos'), col('release_date').alias(
                                  'dataLancamento'), 'anoLancamento', coalesce(col('notaMedia'), col('vote_average')).alias('notaMedia'),
                              coalesce(col('numeroVotos'), col('vote_count')).alias('numeroVotos'), col(
                                  'budget').alias('orcamento'), coalesce(col('imdb_id'), col('id')).alias('idImdb'),
                              col('overview').alias('visaoGeral'), col('popularity').alias('popularidade'), col('revenue').alias('receita'), col('tagline').alias('slogan'))

# Adiciona os ids da dim_produtora à tabela fato_filme
produtora_df = merged_df.select(col('id').alias('temp_id'), explode(
    'production_companies').alias('produtora')).drop('produtora.logo_path')
produtora_df = produtora_df.join(dim_produtora, produtora_df.produtora.id == dim_produtora.codProdutora).groupBy(
    'temp_id').agg(collect_list('codProdutora').alias('codProdutora_alt'))
fato_filme = fato_filme.join(
    produtora_df, fato_filme.id == produtora_df.temp_id, 'left_outer').drop('temp_id')

# Adiciona os ids da dim_idiomaFalado à tabela fato_filme
idiomaFalado_df = merged_df.select(col('id').alias(
    'temp_id'), explode('spoken_languages').alias('idiomaFalado'))
idiomaFalado_df = idiomaFalado_df.join(dim_idiomaFalado, idiomaFalado_df.idiomaFalado.english_name == dim_idiomaFalado.idioma).groupBy('temp_id')\
    .agg(collect_list('codIdiomaFalado').alias('codIdiomaFalado_alt'))
fato_filme = fato_filme.join(idiomaFalado_df, fato_filme.id ==
                             idiomaFalado_df.temp_id, 'left_outer').drop('temp_id')

# Adiciona os ids da dim_paisesProdutores à tabela fato_filme
paisesProdutores_df = merged_df.select(col('id').alias(
    'temp_id'), explode('production_countries').alias('paisesProdutores'))
paisesProdutores_df = paisesProdutores_df.join(dim_paisesProdutores, paisesProdutores_df.paisesProdutores['name'] == dim_paisesProdutores.pais).groupBy('temp_id')\
    .agg(collect_list('codPaisesProd').alias('codPaisesProd_alt'))
fato_filme = fato_filme.join(paisesProdutores_df, fato_filme.id ==
                             paisesProdutores_df.temp_id, 'left_outer').drop('temp_id')

# Adiciona os ids da dim_idiomaOriginal à tabela fato_filme
idiomaOriginal_df = merged_df.select(
    col('id').alias('temp_id'), 'original_language')
idiomaOriginal_df = idiomaOriginal_df.join(dim_idiomaOriginal, idiomaOriginal_df.original_language == dim_idiomaOriginal.idiomaOriginal).groupBy(
    'temp_id').agg(collect_list('codIdiomaOriginal').alias('codIdiomaOriginal_alt'))
fato_filme = fato_filme.join(idiomaOriginal_df, fato_filme.id ==
                             idiomaOriginal_df.temp_id, 'left_outer').drop('temp_id')

# Adiciona os ids da dim_genero à tabela fato_filme
genero_df = merged_df.select(col('id').alias(
    'temp_id'), explode('genres.name').alias('genero_filme'))
genero_df = genero_df.join(dim_genero, genero_df.genero_filme == dim_genero.genero).groupBy(
    'temp_id').agg(collect_list('codGenero').alias('codGenero1'))
fato_filme = fato_filme.join(
    genero_df, fato_filme.id == genero_df.temp_id, 'left_outer').drop('temp_id')

genero_df2 = merged_df.select(col('id').alias('temp_id'), 'genero')
genero_df2 = genero_df2.join(dim_genero, genero_df2.genero == dim_genero.genero).groupBy(
    'temp_id').agg(collect_list('codGenero').alias('codGenero2'))
fato_filme = fato_filme.join(
    genero_df2, fato_filme.id == genero_df2.temp_id, 'left_outer').drop('temp_id')

joined_genero = fato_filme.select(col('id').alias('temp_id'), coalesce(
    col('codGenero1'), col('codGenero2')).alias('codGenero_alt'))

fato_filme = fato_filme.join(joined_genero, fato_filme.id == joined_genero.temp_id,
                             'left_outer').drop('temp_id', 'codGenero1', 'codGenero2')

fato_filme = fato_filme.withColumn(
    'duracaoMinutos', col('duracaoMinutos').cast('integer'))
fato_filme = fato_filme.withColumn(
    'anoLancamento', col('anoLancamento').cast('integer'))
fato_filme = fato_filme.withColumn(
    'dataLancamento', to_date(col('dataLancamento'), 'yyyy-MM-dd'))
fato_filme = fato_filme.withColumn(
    'notaMedia', col('notaMedia').cast('double'))
fato_filme = fato_filme.withColumn(
    'numeroVotos', col('numeroVotos').cast('integer'))

fato_filme = fato_filme.select(
    '*', explode('codProdutora_alt').alias('codProdutora'))
fato_filme = fato_filme.select(
    '*', explode('codGenero_alt').alias('codGenero'))
fato_filme = fato_filme.select(
    '*', explode('codIdiomaFalado_alt').alias('codIdiomaFalado'))
fato_filme = fato_filme.select(
    '*', explode('codIdiomaOriginal_alt').alias('codIdiomaOriginal'))
fato_filme = fato_filme.select('*', explode('codPaisesProd_alt').alias('codPaisesProd')).drop(
    'codGenero_alt', 'codIdiomaOriginal_alt', 'codPaisesProd_alt', 'codIdiomaFalado_alt', 'codProdutora_alt')

fato_filme = fato_filme.coalesce(1)
fato_filme.write.format('parquet').save(f'{target_path}/fato_filme')

job.commit()
