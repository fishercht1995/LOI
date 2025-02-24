import os

def load_access_keys():
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    return {"aws_key": aws_access_key, 
            "aws_secret_key": aws_secret_key}