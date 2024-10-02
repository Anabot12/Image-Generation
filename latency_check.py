import time
import json
from generate_image import generate_images

# Load metadata
metadata_path = 'D:\\New folder\\avataar_assignment\\metadata.json'
with open(metadata_path, 'r') as f:
    metadata = json.load(f)


prompt = metadata['prompts']
depth_map_path = metadata['depth_maps']

# Measuring latency
def measure_latency(prompt, depth_map_path):
    try:
        start_time = time.time()

        generated_image = generate_images([prompt], [depth_map_path])[0]

        end_time = time.time()

        # Calculate and print latency
        latency = end_time - start_time
        print(f"Latency for generating image from prompt '{prompt}': {latency:.2f} seconds")

    except Exception as e:
        print(f"Error during latency measurement for prompt '{prompt}': {e}")

measure_latency(prompt, depth_map_path)
