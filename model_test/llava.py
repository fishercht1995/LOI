import torch
from transformers import AutoProcessor, AutoModelForVision2Seq

# 设置模型 ID 和保存路径
model_id = "llava-hf/llava-v1.6-mistral-7b-hf"
save_folder = "/home/yuqi/zipnn/models"

# 下载并加载 Processor（用于处理文本和图像输入）
#processor = AutoProcessor.from_pretrained(model_id, cache_dir=save_folder)

# 下载并加载模型
model = AutoModelForVision2Seq.from_pretrained(model_id, cache_dir=save_folder, torch_dtype=torch.float16, device_map="auto")

print("Model and processor successfully downloaded and loaded!")
