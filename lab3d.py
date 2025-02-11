#!/usr/bin/env python3
'''Lab 3 Part 2 - disk space using subprocess'''
# Author ID:rbhandari17@myseneca.ca

import subprocess

# Function to get free disk space on the root directory
def free_space():
    # Run the command using subprocess to capture the output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)

    # Capture the output
    output = p.communicate()

    # Decode the byte output and strip any newline characters
    free_space = output[0].decode('utf-8').strip()
    return free_space

if __name__ == '__main__':
    # Test the function by printing the result
    print(free_space())
