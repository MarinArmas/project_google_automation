#!/usr/bin/env python3


import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module
# Change the URL
url = "http://localhost/upload/"
for image in os.listdir("~/supplier-data/images"):
    image_path = os.path.join("~/supplier-data/images", image)
    if os.path.splitext(image_path)[1] == ".jpeg":
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})