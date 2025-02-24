from s3 import S3Storage
from util import load_access_keys

class storage:
    def __init__(self, models):
        keys = load_access_keys()
        self.s3_storage = S3Storage(aws_access_key=keys["aws_key"], aws_secret_key=keys["aws_secret_key"])
    
    def 