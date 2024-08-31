#!/usr/bin/env python3
import shutil
import psutil
import emails
import time
import subprocess
import os 

def check_cpu_usage():
    """Returns True if the CPU usage is over 80%."""
    return psutil.cpu_percent(1) > 80

def check_disk_space():
    """Returns True if the available disk space is lower than 20%."""
    disk_usage = shutil.disk_usage('/')
    percent_free = disk_usage.free / disk_usage.total * 100
    return percent_free < 20

def check_memory_usage():
    """Returns True if available memory is less than 100MB."""
    available_memory = psutil.virtual_memory().available
    return available_memory < 100 * 1024 * 1024

def check_hostname_resolution():
    """Returns True if hostname 'localhost' cannot be resolved to '127.0.0.1'."""
    try:
        result = subprocess.run(['ping', '-c', '1', 'localhost'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # On Unix, if the ping succeeds, it will return 0. On Windows, it may differ, hence adjust accordingly.
        return result.returncode != 0
    except Exception:
        return True

def send_email(subject):
    """Sends an email with the given subject."""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)

def main():
    while True:
        if check_cpu_usage():
            send_email("Error - CPU usage is over 80%")
        if check_disk_space():
            send_email("Error - Available disk space is less than 20%")
        if check_memory_usage():
            send_email("Error - Available memory is less than 100MB")
        if check_hostname_resolution():
            send_email("Error - localhost cannot be resolved to 127.0.0.1")
        
        time.sleep(60)  # Wait for 60 seconds before checking again.

if __name__ == "__main__":
    main()