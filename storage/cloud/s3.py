import boto3

"""
class S3Storage:
    def __init__(self, bucket_name="east1storage", region="us-east-1",
                 aws_access_key="your_access_key",
                 aws_secret_key="your_secret_key"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            region_name=region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def put(self, file_path, s3_key):
        self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
        print(f"✅ 上传成功: s3://{self.bucket_name}/{file_path}")

    def get(self, s3_key, download_path):
        self.s3_client.download_file(self.bucket_name, s3_key, download_path)
        print(f"✅ 下载成功: {download_path}")

"""

import os
import boto3

class S3Storage:
    def __init__(self, bucket_name="east1storage", region="us-east-1",
                 aws_access_key="your_access_key",
                 aws_secret_key="your_secret_key"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            region_name=region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def put(self, local_path, s3_key_prefix=""):
        """上传文件或文件夹到 S3"""
        if os.path.isdir(local_path):  # 处理文件夹
            for root, _, files in os.walk(local_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_file_path, local_path)  # 计算相对路径
                    s3_key = os.path.join(s3_key_prefix, relative_path).replace("\\", "/")  # Windows 兼容
                    self.s3_client.upload_file(local_file_path, self.bucket_name, s3_key)
                    print(f"✅ 文件上传成功: {local_file_path} -> s3://{self.bucket_name}/{s3_key}")
        else:  # 处理单个文件
            s3_key = s3_key_prefix or os.path.basename(local_path)
            self.s3_client.upload_file(local_path, self.bucket_name, s3_key)
            print(f"✅ 文件上传成功: {local_path} -> s3://{self.bucket_name}/{s3_key}")

    def get(self, s3_key, download_path):
        """下载文件"""
        self.s3_client.download_file(self.bucket_name, s3_key, download_path)
        print(f"✅ 下载成功: {download_path}")


def test():
    from util import load_access_keys
    keys = load_access_keys()
    s3_storage = S3Storage(aws_access_key=keys["aws_key"], aws_secret_key=keys["aws_secret_key"])
    s3_storage.put("/home/yuqi/LOI/test", "test")

import os
import shutil

def copy_safetensors_files(src_root, dest_root):
    # 确保目标目录存在
    os.makedirs(dest_root, exist_ok=True)
    dest_root_tensors = f"{dest_root}/tensors"
    dest_root_znn = f"{dest_root}/znn"
    os.makedirs(dest_root_tensors, exist_ok=True)
    os.makedirs(dest_root_znn, exist_ok=True)
    # 遍历源目录
    for root, dirs, files in os.walk(src_root):
        # 检查当前目录是否包含 .safetensors 文件
        safetensors_files = [f for f in files if f.endswith(".safetensors") and "znn" not in f]
        znn_files = [f for f in files if "znn" in f]
        if safetensors_files:
            # 获取当前子目录名称
            relative_path = os.path.relpath(root, src_root)
            dest_folder = os.path.join(dest_root_tensors, relative_path)

            # 创建目标文件夹
            os.makedirs(dest_folder, exist_ok=True)

            # 复制 .safetensors 文件
            for file in safetensors_files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, file)
                shutil.copy2(src_file, dest_file)  # 保留原始文件元数据
                print(f"Copied: {src_file} -> {dest_file}")

        if znn_files:
            # 获取当前子目录名称
            relative_path = os.path.relpath(root, src_root)
            dest_folder = os.path.join(dest_root_znn, relative_path)

            # 创建目标文件夹
            os.makedirs(dest_folder, exist_ok=True)

            # 复制 .safetensors 文件
            for file in znn_files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, file)
                shutil.copy2(src_file, dest_file)  # 保留原始文件元数据
                print(f"Copied: {src_file} -> {dest_file}")


def upload():
    from util import load_access_keys
    import sys
    keys = load_access_keys()
    s3_storage = S3Storage(aws_access_key=keys["aws_key"], aws_secret_key=keys["aws_secret_key"])
    s3_storage.put(f"/home/yuqi/zipnn/models/{sys.argv[1]}/{sys.argv[2]}", f"{sys.argv[1]}-{sys.argv[2]}")

if __name__ == "__main__":
    #test()
    """
    # 设置源目录 (b) 和目标目录 (a)
    import sys
    base = "/home/yuqi/zipnn/models"
    folder_a = "/home/yuqi/zipnn/models/{}".format(sys.argv[2])  # 替换成你的 b 目录
    folder_b = "/home/yuqi/zipnn/models/{}".format(sys.argv[1])  # 替换成你的 a 目录
    copy_safetensors_files(folder_b, folder_a)
    """
    upload()

