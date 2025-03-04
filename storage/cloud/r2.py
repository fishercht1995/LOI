import boto3

import os
import boto3

class R2Storage:
    def __init__(self, bucket_name="modelsmar4", region="auto",
                 r2_access_key="your_access_key",
                 r2_secret_key="your_secret_key",
                 r2_endpoint="https://your-account-id.r2.cloudflarestorage.com"):

        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            region_name=region,
            aws_access_key_id=r2_access_key,
            aws_secret_access_key=r2_secret_key,
            endpoint_url=r2_endpoint  # Cloudflare R2 的 endpoint
        )

    def put(self, local_path, r2_key_prefix=""):
        """ 上传单个文件或整个文件夹到 Cloudflare R2 """
        if os.path.isdir(local_path):  # 如果是文件夹，则递归上传
            for root, _, files in os.walk(local_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_file_path, local_path)  # 计算相对路径
                    r2_key = os.path.join(r2_key_prefix, relative_path).replace("\\", "/")  # 适配 S3/R2 结构
                    
                    self.s3_client.upload_file(local_file_path, self.bucket_name, r2_key)
                    print(f"✅ 文件上传成功: {local_file_path} -> r2://{self.bucket_name}/{r2_key}")
        else:  # 处理单个文件上传
            r2_key = r2_key_prefix or os.path.basename(local_path)
            self.s3_client.upload_file(local_path, self.bucket_name, r2_key)
            print(f"✅ 文件上传成功: {local_path} -> r2://{self.bucket_name}/{r2_key}")

    def get(self, r2_key, download_path):
        """ 从 Cloudflare R2 下载文件 """
        self.s3_client.download_file(self.bucket_name, r2_key, download_path)
        print(f"✅ 下载成功: {download_path}")


def test():
    from util import load_access_keys
    keys = load_access_keys()

    # 你需要替换 Cloudflare R2 的 endpoint
    r2_endpoint = "https://your-account-id.r2.cloudflarestorage.com"

    r2_storage = R2Storage(
        r2_access_key=keys["r2_key"],
        r2_secret_key=keys["r2_secret_key"],
        r2_endpoint=keys["r2_endpoint"]
    )
    import sys
    r2_storage.put(f"/home/yuqi/zipnn/models/{sys.argv[1]}/{sys.argv[2]}", f"{sys.argv[1]}-{sys.argv[2]}")

if __name__ == "__main__":
    test()
