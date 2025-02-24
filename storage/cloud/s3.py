import boto3

class S3Storage:
    def __init__(self, bucket_name="east1storage", region="us-east-1",
                 aws_access_key="your_access_key",
                 aws_secret_key="your_secret_key"):
        """ 手动提供 AWS 密钥（不推荐直接硬编码在代码里） """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            region_name=region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def put(self, file_path, s3_key):
        self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
        print(f"✅ 上传成功: s3://{self.bucket_name}/{s3_key}")

    def get(self, s3_key, download_path):
        self.s3_client.download_file(self.bucket_name, s3_key, download_path)
        print(f"✅ 下载成功: {download_path}")


def test():
    pass

if __name__ == "__main__":
    test()


