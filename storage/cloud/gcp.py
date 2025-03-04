from google.cloud import storage
import os

from google.cloud import storage

import os
from google.cloud import storage

class GCPStorage:
    def __init__(self, bucket_name="modelssingle", key_path="/home/yuqi/gcp.json"):
        """ 初始化 GCS 客户端 """
        self.bucket_name = bucket_name
        self.client = storage.Client.from_service_account_json(key_path)  # 指定密钥文件
        self.bucket = self.client.bucket(self.bucket_name)

    def put(self, local_path, gcs_key_prefix=""):
        """ 上传文件或文件夹到 GCS """
        if os.path.isdir(local_path):  # 如果是目录，则递归上传
            for root, _, files in os.walk(local_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_file_path, local_path)  # 计算相对路径
                    gcs_key = os.path.join(gcs_key_prefix, relative_path).replace("\\", "/")  # 适配 S3 结构
                    
                    blob = self.bucket.blob(gcs_key)
                    blob.upload_from_filename(local_file_path)
                    print(f"✅ 文件上传成功: {local_file_path} -> gs://{self.bucket_name}/{gcs_key}")
        else:  # 单个文件上传
            gcs_key = gcs_key_prefix or os.path.basename(local_path)
            blob = self.bucket.blob(gcs_key)
            blob.upload_from_filename(local_path)
            print(f"✅ 文件上传成功: {local_path} -> gs://{self.bucket_name}/{gcs_key}")

    def get(self, gcs_key, download_path):
        """ 从 GCS 下载文件 """
        blob = self.bucket.blob(gcs_key)
        blob.download_to_filename(download_path)
        print(f"✅ 下载成功: {download_path}")



def test():
    import sys
    gcp = GCPStorage("modelssingle")
    gcp.put(f"/home/yuqi/zipnn/models/{sys.argv[1]}/{sys.argv[2]}", f"{sys.argv[1]}-{sys.argv[2]}")

if __name__ == "__main__":
    test()