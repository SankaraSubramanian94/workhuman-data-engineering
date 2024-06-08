import boto3
import json

s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        document = s3_client.get_object(Bucket=bucket, Key=key)
        content = document['Body'].read().decode('utf-8')
        
        # Process document (send to SQS for further processing)
        sqs_client.send_message(
            QueueUrl='YOUR_SQS_QUEUE_URL',
            MessageBody=json.dumps({'content': content, 'key': key})
        )

    return {'statusCode': 200, 'body': json.dumps('Success')}
