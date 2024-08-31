#!/usr/bin/env python3

import emails
import os
import reports
import datetime

def process_file(file_path):
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
        return fruits_dict

    except (IOError, IndexError, SyntaxError) as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def main():
    # Change the directory
    directory = './txt'
    data_foramted = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            fruits_dict = process_file(file_path)
            if fruits_dict:  # Check if processing was successful
                data_foramted.append("<br/>".join(f"{key}: {value}" for key, value in fruits_dict.items()))
                
    title = f"Processed Update on {datetime.date.today()}"
    reports.generate("/tmp/processed.pdf", title, "<br/><br/>".join(data_foramted))

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)

if __name__ == "__main__":
    main()