#!/usr/bin/env python3

# This is a module for main.py but it's not yet connected, so it is a solo file
# This script encodes a crypto alphabet (data.json) using base64, so you can low-key 'safely' pass it to your comrade
# And it decodes key.txt using base64 into data.json
# it works!

# Usage: python3 modules/key_manager.py [data.json OR key.txt]

import base64
import sys
import shutil

target_file = "data.json"
target_crypto_file = "key.txt"

def _help():
    print("""
Usage: python3 modules/key_manager.py [OPTION]

Options:
    -en  ---> Encode data.json using base64 and rename it to key.txt
    -de  ---> Decode key.txt using base64 and rename it to data.json
""")

def encode(filename):
    try:
        shutil.copyfile(filename, target_crypto_file)
        with open(target_crypto_file, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        file_64_encode = base64.b64encode(encoded_string)
        file_result = open(target_crypto_file, 'wb')
        file_result.write(file_64_encode)
    except Exception as e:
        sys.exit("An error ocured:\n" + str(e))
    else:
        print("Check out the " + target_crypto_file + " and pass it to the partner")

def decode(filename):
    try:
        shutil.copyfile(filename, target_file)
        with open(target_file, "rb") as file:
            decoded_string = base64.b64decode(file.read())
        file_64_decode = base64.b64decode(decoded_string)
        file_result = open(target_file, 'wb')
        file_result.write(file_64_decode)
    except Exception as e:
        sys.exit("An error ocured:\n" + str(e))
    else:
        print("Check out the " + target_file)    

def main():
    if len(sys.argv) == 1:
        _help()
    if len(sys.argv) == 2:
#       Auto detection: If detects: data.json, will encode it, otherwise will decode a key.txt using base64
        if sys.argv[1] == "-en":
            encode(target_file)
        elif sys.argv[1] == "-de":
            decode(target_crypto_file)
        else:
            sys.exit(f"Sorry! Did not detect {target_file} or {target_crypto_file}\nThis script is still in early testing, try to change something")

main()
