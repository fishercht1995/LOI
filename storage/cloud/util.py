import os

def load_access_keys():
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    r2_access_key = os.getenv("R2_ACCESS_KEY_ID")
    r2_secret_key = os.getenv("R2_SECRET_ACCESS_KEY")
    r2_endpoint = os.getenv("R2_ENDPOINT")
    return {"aws_key": aws_access_key, 
            "aws_secret_key": aws_secret_key,
            "r2_key": r2_access_key,
            "r2_secret_key": r2_secret_key,
            "r2_endpoint": r2_endpoint}