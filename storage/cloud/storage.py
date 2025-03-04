from s3 import S3Storage
from gcp import GCPStorage
from util import load_access_keys

class storage:
    def __init__(self, models = {}, stats = {}):
        keys = load_access_keys()
        self.s3_storage = S3Storage(aws_access_key=keys["aws_key"], aws_secret_key=keys["aws_secret_key"])
        self.gcp_storage = GCPStorage("modelssingle")
        if len(models) == 0:
            self.models = {}
        if len(stats) == 0:
            self.stats = {}
    
    def put(self, file_path, key, cloud = "s3"):
        if cloud == "s3":
            self.s3_storage.put(file_path, self.bucket_name, key)
            self.models[key] = "s3"
        
        if cloud == "gcp":
            self.gcp_storage.put(file_path, key)
            self.models[key] = "gcp"
            

    def get(self, key, download_path, cloud = "s3"):
        if cloud == "s3":
            self.s3_storage.get(self.bucket_name, key, download_path)
            if key not in self.stats:
                self.stats[key] = 0
            self.stats[key] += 1
            
        if cloud == "gcp":
            self.gcp_storage.get(key, download_path)
            if key not in self.stats:
                self.stats[key] = 0
            self.stats[key] += 1

    def move(self, cloud_in, cloud_out, key, download_path):
        if cloud_in == "s3":
            self.get(key, download_path, "s3")
        
        if cloud_in == "gcp":
            self.get(key, download_path, "gcp")

        if cloud_out == "s3":
            self.put(self, "{}/{}".format(download_path, key), key, "s3")

        if cloud_out == "gcp":
            self.put(self, "{}/{}".format(download_path, key), key, "gcp")
