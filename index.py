import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'Topic'
table = dynamodb.Table(table_name)

def handler(event, context):

    logger.info('get_topics_information')

    response = table.scan()
    data = response['Items']

    return {
            'headers': {'Content-Type': 'application/json'},
            'statusCode': 200,
            'body': json.dumps(data)
            }