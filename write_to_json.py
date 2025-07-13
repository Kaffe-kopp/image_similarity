
import os
import json
from PIL import Image
import imagehash
import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

ImgFolderPath = "to_convert"

ImgFolder = os.listdir(ImgFolderPath)


with open("hashes.json", "r+") as file:
    hashes_json = json.load(file)
    for img in ImgFolder:
        if img in [i['name'] for i in hashes_json['all_hashes']]:
            logging.debug(f'{img} already exists')
            continue
        name = img
        #series_num = None _p0 _p1 etc
        hash_avg = imagehash.average_hash(Image.open(f"{ImgFolderPath}/{img}"))

        img_data = {
            "name": name,
            #"series_num": series_num,
            "hash_avg": str(hash_avg)
            #add more hashes uwu plz
        }

        hashes_json["all_hashes"].append(img_data)

        file.seek(0)

        json.dump(hashes_json, file, indent=4)

