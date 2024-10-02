import torch
from diffusers import StableDiffusionPipeline
import numpy as np
import cv2
import json
import os

# Loading the pipeline
save_path = "D:/stable_diffusion_model"
pipe = StableDiffusionPipeline.from_pretrained(save_path, torch_dtype=torch.float16)
pipe.to("cuda")

# Fixing the seed
torch.manual_seed(12345)

# Loading metadata
metadata_path = 'D:\\New folder\\avataar_assignment\\metadata.json'
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

def generate_images(prompts, depth_maps):
    output_images = []
    os.makedirs('generated_images', exist_ok=True)

    for prompt, depth_map_path in zip(prompts, depth_maps):
        # Loading the predefined depth maps
        if depth_map_path.endswith('.png'):
            depth_map = cv2.imread(depth_map_path, cv2.IMREAD_UNCHANGED)
        elif depth_map_path.endswith('.npy'):
            depth_map = np.load(depth_map_path)
        else:
            print(f"Unsupported file format for depth map: {depth_map_path}")
            continue

        # Depth map should be present
        if depth_map is None:
            print(f"Failed to load depth map from: {depth_map_path}")
            continue

        # Creating depth and canny edge maps
        depth_map_tensor = torch.tensor(depth_map).unsqueeze(0)

        # For edge detection to 8 units
        if depth_map.dtype != np.uint8:
            depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        edges = cv2.Canny(depth_map, 100, 200)
        edges_tensor = torch.tensor(edges).unsqueeze(0)

        # Generating the image
        with torch.no_grad():
            image = pipe(prompt=prompt, controlnet=[depth_map_tensor, edges_tensor]).images[0]

        # Saving the generated image
        output_path = f"generated_images/{prompt.replace(' ', '_')}.png"
        image.save(output_path)
        output_images.append(image)

    return output_images

#meta data from json meta data file
prompts = metadata['prompts']
depth_maps = metadata['depth_maps']
generate_images(prompts, depth_maps)
