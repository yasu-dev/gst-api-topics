import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'Topic'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):

    logger.info("Topics")
    return table.scan()
