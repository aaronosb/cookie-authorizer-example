import json


def respond(err, res=None):
    response = {
        "statusCode": "400" if err else "200",
        "body": str(err) if err else json.dumps(res),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://example.com",  # <- Also have to set CORS Headers in function response
            "Access-Control-Allow-Credentials": True,
        },
    }
    return response


def lambda_handler(event, context):
    """Sample HelloWorld Function"""
    try:
        # Accessing the principalId set via Cookie Authorizer
        username = event["requestContext"]["authorizer"]["principalId"]
        res = {"message": f"Hello {username}"}
        return respond(None, res)
    except Exception as e:
        print(e)
        return respond
