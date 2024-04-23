import logging
import boto3
from botocore.exceptions import ClientError
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=os.getenv("aws_access_key_id"),
                             aws_secret_access_key=os.getenv("aws_secret_access_key"),
                             aws_session_token=os.getenv('aws_session_token'))
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


today = date.today().strftime("%Y/%m/%d")


upload_file('movies.csv', 'desafiofinalcompass',
            f'Raw/local/CSV/Movies/{today}/movies.csv')

upload_file('series.csv', 'desafiofinalcompass',
            f'Raw/local/CSV/Series/{today}/series.csv')
