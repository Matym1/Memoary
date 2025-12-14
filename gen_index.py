import os
import json
import random


IMG_FOLDER_PATH='./public/images'
IMG_INDEX_PATH='./public/images/image_index.json'

OCCUPANCY_PARAMETER= 0.3

img_index = {
    "images": {},
    "grid_size": 0, 
}

# Read all images
dir_list = os.listdir(IMG_FOLDER_PATH)

images  = []

# Filter only jpg images
for potential_image in dir_list:
    split_image = potential_image.split('.')
    if split_image[-1].lower()== 'jpg':
        images.append(split_image[0])

# Load existing index if exists
if os.path.exists(IMG_INDEX_PATH):
    with open(IMG_INDEX_PATH, 'r') as f:
        img_index = json.load(f)

# Decide on grid size 
grid_size  = max(int((len(images)/OCCUPANCY_PARAMETER)**(1/3)), 10)
img_index['grid_size'] = grid_size

occupied_positions = []

def gen_free_position():
    while True:
        pos = [random.randint(0,grid_size-1), random.randint(0,grid_size-1)]
        if pos not in occupied_positions:
            occupied_positions.append(pos)
            return pos

for image in images:
        if image not in img_index['images']:
            print(f"New image found: {image}, adding to index")
            tags = input(f"Enter tags for image {image} (comma separated): ").strip().split(',')
            alt = input(f"Enter alt text for image {image}: ").strip()
            if(tags==['']):
                tags = []
            else:
                tags = [tag.strip() for tag in tags]

            img_data = {
                "alt":alt,
                "tags":tags,
                "position":gen_free_position(),
                }
            img_index['images'][image]=img_data


json_object = json.dumps(img_index)

with open(IMG_INDEX_PATH, "w") as outfile:
    outfile.write(json_object)