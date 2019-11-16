from http.cookies import SimpleCookie


def get_auth_token_from_cookie(event):
    try:
        cookie = SimpleCookie()
        cookie.load(event["headers"]["Cookie"])
        token = cookie["TOKEN"].value  # <- TOKEN is the name of the cookie
        return token
    except:
        print("Problem retrieving Token Cookie from request")
        print(event)
        raise Exception("Problem retrieving Token Cookie from request")


def generatePolicy(principalId, effect, methodArn):
    authResponse = {}
    authResponse["principalId"] = principalId
    base = methodArn.split("/")[0]
    stage = methodArn.split("/")[1]
    arn = base + "/" + stage + "/*/*"

    if effect and methodArn:
        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "FirstStatement",
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": arn,
                }
            ],
        }
        authResponse["policyDocument"] = policyDocument
    return authResponse


def lambda_handler(event, context):
    try:
        token = get_auth_token_from_cookie(event)
        # JWT Token validations goes here
        # Additional claims based validation goes here
        print(token)
        username_from_token = "sub"
        generatePolicy(username_from_token, "Allow", event["methodArn"])
    except Exception as e:
        print(e)
        return generatePolicy(None, "Deny", event["methodArn"])

