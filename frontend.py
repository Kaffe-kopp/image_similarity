
import os
import json
from backend import *

ImgFolderPath = ""

with open("hashes.json", "r") as hashes_json:
    hashes = json.dumps(hashes_json)
    print(hashes)
