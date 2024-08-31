#!/usr/bin/env python3

import os
from PIL import Image

def list_images_in_directory(directory):
    image_files = []

    # Iterate through the contents of the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        
        # Check if the path is a file
        if os.path.isfile(file_path):
            try:
                # Attempt to open the file as an image
                with Image.open(file_path) as img:
                    # Convert image to a mode suitable for JPEG if necessary
                    if img.mode not in ("RGB", "L"):  # JPEG doesn't support 'LA', 'RGBA', etc.
                        img = img.convert("RGB")
                    
                    # If successful, append to the list
                    image_files.append(filename)
            except (IOError, SyntaxError):
                # If an error occurs (not an image or corrupt file), skip it
                continue

    return image_files

# Example usage
directory_path = '~/supplier-data/images'
image_list = list_images_in_directory(directory_path)

print("Image files found in the directory:")
for image in image_list:
    
    with Image.open(os.path.join(directory_path, image)) as img:
        img.resize((600,400)).save(os.path.join(directory_path, image), "TIFF")