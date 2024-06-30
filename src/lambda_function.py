import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! - V1.0.0.6 - Version Lambda 1.0')
    }
