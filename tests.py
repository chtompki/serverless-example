import unittest
import lambda_function

EVENT = {
    'resource': '/',
    'path': '/',
    'httpMethod': 'POST',
    'headers': {
        'Accept': '*/*',
        'CloudFront-Forwarded-Proto': 'https',
        'CloudFront-Is-Desktop-Viewer': 'true',
        'CloudFront-Is-Mobile-Viewer': 'false',
        'CloudFront-Is-SmartTV-Viewer': 'false',
        'CloudFront-Is-Tablet-Viewer': 'false',
        'CloudFront-Viewer-Country': 'US',
        'content-type': 'application/x-www-form-urlencoded',
        'Host': 'cckfhngf25.execute-api.us-east-1.amazonaws.com',
        'User-Agent': 'curl/7.64.1',
        'Via':
            '2.0 77a52be30020596b6a87a26e3dcc75e7.cloudfront.net (CloudFront)',
        'X-Amz-Cf-Id':
            'CRIdzUeKSNWi42xaBv2dN24cFzjcVWVYfMvc-Y5r6JIXsJJVztEKhg==',
        'X-Amzn-Trace-Id': 'Root=1-60c7661b-0ac926f872069ca40bc5ce89',
        'X-Forwarded-For': '160.19.3.61, 70.132.43.96',
        'X-Forwarded-Port': '443',
        'X-Forwarded-Proto': 'https'
    },
    'multiValueHeaders': {
        'Accept': ['*/*'],
        'CloudFront-Forwarded-Proto': ['https'],
        'CloudFront-Is-Desktop-Viewer': ['true'],
        'CloudFront-Is-Mobile-Viewer': ['false'],
        'CloudFront-Is-SmartTV-Viewer': ['false'],
        'CloudFront-Is-Tablet-Viewer': ['false'],
        'CloudFront-Viewer-Country': ['US'],
        'content-type': ['application/x-www-form-urlencoded'],
        'Host': ['cckfhngf25.execute-api.us-east-1.amazonaws.com'],
        'User-Agent': ['curl/7.64.1'],
        'Via': [
            '2.0 77a52be30020596b6a87a26e3dcc75e7.cloudfront.net (CloudFront)'
        ],
        'X-Amz-Cf-Id': [
            'CRIdzUeKSNWi42xaBv2dN24cFzjcVWVYfMvc-Y5r6JIXsJJVztEKhg=='
        ],
        'X-Amzn-Trace-Id': ['Root=1-60c7661b-0ac926f872069ca40bc5ce89'],
        'X-Forwarded-For': ['160.19.3.61, 70.132.43.96'],
        'X-Forwarded-Port': ['443'],
        'X-Forwarded-Proto': ['https']
    },
    'queryStringParameters': None,
    'multiValueQueryStringParameters': None,
    'pathParameters': None,
    'stageVariables': None,
    'requestContext': {
        'resourceId': 'etojqq5b17',
        'resourcePath': '/',
        'httpMethod': 'POST',
        'extendedRequestId': 'A6zkSHaVIAMFo0w=',
        'requestTime': '14/Jun/2021:14:22:19 +0000',
        'path': '/dev',
        'accountId': '409543137833',
        'protocol': 'HTTP/1.1',
        'stage': 'dev',
        'domainPrefix': 'cckfhngf25',
        'requestTimeEpoch': 1623680539287,
        'requestId': '81c2aaa0-6a79-4300-bd2a-e5e0827d4f7d',
        'identity': {
            'cognitoIdentityPoolId': None,
            'accountId': None,
            'cognitoIdentityId': None,
            'caller': None,
            'sourceIp': '160.19.3.61',
            'principalOrgId': None,
            'accessKey': None,
            'cognitoAuthenticationType': None,
            'cognitoAuthenticationProvider': None,
            'userArn': None,
            'userAgent': 'curl/7.64.1',
            'user': None
        },
        'domainName': 'cckfhngf25.execute-api.us-east-1.amazonaws.com',
        'apiId': 'cckfhngf25'
    },
    'body': '{"key1":"value1", "key2":"value2", "key3":"value3"}',
    'isBase64Encoded': False
}


class LambdaFunctiontest(unittest.TestCase):
    def test_lambda_handler_success(self):
        response = lambda_function.lambda_handler(EVENT, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(
            response['headers']['x-hello-world'],
            'some header value'
        )
        self.assertEqual(
            response['body'],
            '{"key1":"value1", "key2":"value2", "key3":"value3"}'
        )


if __name__ == '__main__':
    unittest.main()
