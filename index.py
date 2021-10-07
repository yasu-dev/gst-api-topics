import logging
import boto3
import json
import simplejson as json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'Topic'
table = dynamodb.Table(table_name)

def handler(event, context):

    logger.info('GET topics')

    response = table.scan()

    return {
            'statusCode': 200,
            'headers': {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            },
            'body': json.dumps(response['Items'])
    }
