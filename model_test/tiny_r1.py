from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model_name = "qihoo360/TinyR1-32B-Preview"
# 指定模型保存路径
save_folder = "/home/yuqi/zipnn/models"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    cache_dir=save_folder
)