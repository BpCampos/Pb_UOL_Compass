import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

# @params: [JOB_NAME]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df_csv = spark.read.csv(source_file, header=True, sep='|')

df_csv_filtrado = df_csv.drop("generoArtista", "nomeArtista", "anoNascimento", "anoFalecimento",
                              "profissao", "titulosMaisConhecidos", "personagem", "tituloOriginal", "anoLancamento")

df_csv_filtrado = df_csv_filtrado.filter(
    (col('genero') == 'Drama') | (col('genero') == 'Romance')).dropDuplicates()

df_csv_filtrado = df_csv_filtrado.coalesce(1)

df_csv_filtrado.write.mode('append').parquet(target_path)

job.commit()
