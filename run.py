#!/usr/bin/env python3
import os
import requests

def process_file(file_path, image):
    fruits_dict = {}
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

            # Ensure that there are enough lines in the file
            if len(lines) < 3:
                print(f"Skipping file {file_path}: Not enough data")
                return None

            fruits_dict['name'] = lines[0].strip()
            fruits_dict['weight'] = lines[1].strip()
            fruits_dict['description'] = lines[2].strip()
            fruits_dict['image_name'] = image
        
        return fruits_dict

    except (IOError, IndexError, SyntaxError) as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def send_post_request(fruits_dict):
    try:
        # Change the URL
        response = requests.post('http://104.197.242.79/feedback', json=fruits_dict)
        
        if response.status_code == 201:
            print("Successfully posted")
        else:
            print("Failed to post:", response.status_code)
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    # Change the directory
    directory = './txt'
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        image = os.path.splitext(filename)[0] + ".jpeg"
        if os.path.isfile(file_path):
            fruits_dict = process_file(file_path, image)
            if fruits_dict:  # Check if processing was successful
                send_post_request(fruits_dict)
                # print(fruits_dict)

if __name__ == "__main__":
    main()