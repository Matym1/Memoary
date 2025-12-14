import os
import json

IMG_FOLDER_PATH='./public/images'
IMG_INDEX_PATH='./public/images/image_index.json'



img_data = {
    "alt":"",
    "tags":[]
}
img_index = {
}

# Read all images
dir_list = os.listdir(IMG_FOLDER_PATH)

for image in dir_list:
    split_image = image.split('.')
    if split_image[-1].lower()== 'jpg':
        img_index[split_image[0]]=img_data

json_object = json.dumps(img_index)

with open(IMG_INDEX_PATH, "w") as outfile:
    outfile.write(json_object)