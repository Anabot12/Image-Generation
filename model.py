import torch
from diffusers import StableDiffusionPipeline
import os


cache_dir = "D:/huggingface_cache"

# Creating  the directory if it doesn't exist
#os.makedirs(cache_dir, exist_ok=True)
# # upon succesfully executing the code once a folder was created (ensure to uncomment the above statement )

# Set up the pipeline and specify cache directory on D drive
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16, use_auth_token=True, resume_download=True, local_files_only=False, timeout=100000
)
pipe.to("cuda")

# Saving the pipeline locally
model_save_path = "D:/stable_diffusion_model"
os.makedirs(model_save_path, exist_ok=True)
pipe.save_pretrained(model_save_path)

print(f"Model saved at {model_save_path}")
