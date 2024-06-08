import json
from vectorize_store import process_document

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        content = body['content']
        
        # Process document content
        process_document(content)

    return {'statusCode': 200, 'body': json.dumps('Success')}
