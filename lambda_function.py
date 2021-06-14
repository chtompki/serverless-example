import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    response = {
        'statusCode': 200,
        'headers': {'x-hello-world': 'some header value'},
        'body': event['body']
    }
    return response
