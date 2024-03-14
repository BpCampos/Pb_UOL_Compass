import logging
import boto3
from botocore.exceptions import ClientError
import os
from datetime import date


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id='ASIAW3MECJ57TRIPKQEA',
                             aws_secret_access_key='OSOh6k/0dL1H+4yVLxrTKWefIO9mqUuJ7wy05zrU',
                             aws_session_token='IQoJb3JpZ2luX2VjEGwaCXVzLWVhc3QtMSJGMEQCIFAphyc76607dEUIDKyaLnDnY73FEGNOhhFGL3kpXJREAiBlcjtTD7DwOOMIAZTOV+T/zuBCufq/RlXNUQnFWVt+6yqdAwh1EAAaDDQ3MTExMjc2NTMxMSIMvTGk8/RRrOwKax0HKvoCb2WYXiAUD5FH+/kg5fg0o8mHRwqSYsUUcaJXfGGtWXw9y4PArvKt3K0AtqkMtar+Ke0cHuNsmYV+Dgf/3ZYEN9AuIvScIPMAIkeaAzdcb/9QpBIWiaJFudBTLevXAK8Uf7Y1ticSiUqd0lBo4WmBiC4A+cNuwVnzly61xbfk08/p1Hp1U/B5uN7reRwtmapJxmMvACQK9ejxYo0+q+w88Rlf2reDzr+bkNaTz/y7RUidsPBU3fMiz+aXm2F2FaELS1Id/BLtwViDbe3PDBGctlGmZprbKURaZikn6KBHZd4Uk6Zg9oKU5tsapHedByAaJjSvSuzPhqGY/+PRk80NBgz4UpayxNjxrsSBHgim4CYPaoYIfjjICatT1UN30KrvUGFbFZTgKS5GHDJpqyf1PfiMh78z6lhap/ICc66jwU9WePU2RKBXlBXS1J7SLzfFMt6E5S+/034gPDbA84hZdeRoLn6BaJSeU7bEF0/pOftriOL69VO0dFmEMLvJy68GOqcBcK4EARnO/DkQeSu/0NI/+skcmzDG3EeTcisJKtJj0VSxOerjz5ChRpBMcRa8J0RS3AWkipEv9xrVdqYzve5L3nuNIPaN7h36x3FiEnBnx1DmRm1RQB4m0KMErjkc4EeKXstzJPVqWZGfJ1gSIjV0yPHaLfe/cJ5r9Cpqoh7Qq+YBaI5d5vMWttvm1CRP1YZK53K6LxneibzUxJb5D3Kt5JGvBgysehw=')
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
