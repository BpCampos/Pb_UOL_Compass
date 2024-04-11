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

tmdb = spark.read.json(f'{source_file}*.json')

data = source_file[len(source_file) -
                   11: len(source_file) - 1].replace('/', '-')

df_with_date = tmdb.withColumn("dt", lit(data))

df_transformed = df_with_date.drop("adult", "belongs_to_collection", "backdrop_path",
                                   "homepage", "poster_path", "status_code", "status_message", "success", "status", "video")

df_transformed = df_transformed.dropDuplicates()

df_transformed.write.mode("append").partitionBy(
    'dt').format("parquet").save(target_path)

job.commit()
