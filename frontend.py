
import os
import json
import logging
from collections import defaultdict

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

ImgFolderPath = ""

def CollectJsonItems(lst: list):
    res = defaultdict(list)
    for d in lst:
        for k, v in d.items():
            res[k].append(v)

    HashList_avg = res['hash_avg']
    return HashList_avg


with open("hashes.json", "r") as file:
    hashes_json = json.load(file)
    HashList_avg = CollectJsonItems(hashes_json['all_hashes']) 
