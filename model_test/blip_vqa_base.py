from transformers import BlipForQuestionAnswering

# 指定模型保存路径
save_folder = "/home/yuqi/zipnn/models"

# 重新下载模型
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base", cache_dir=save_folder)

