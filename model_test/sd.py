from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"
cache_dir = "/home/yuqi/zipnn/models"  # 替换成你的目标目录

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    cache_dir=cache_dir
)
