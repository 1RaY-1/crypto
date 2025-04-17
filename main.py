#!/usr/bin/env python3

# Author: 1RaY-1 (https://github.com/1ray-1)
# Upload date: September 25th, 2023
# License: MIT (see LICENSE file)
# Description: Read README.md

# THE MAIN FILE
# You can rather run main.py to make things easier and more disciplined or directly run a needed module from 'modules' folder

import argparse
import os
import sys
import platform
import os.path

try:
    from modules.encrypt import Encryptor
    from modules.decrypt import Decryptor
    from modules.generate import Generator
except ModuleNotFoundError:
    try:
        from encrypt import Encryptor
        from decrypt import Decryptor
        from generate import Generator
    except ModuleNotFoundError:
        print("[!] Where modules ??\nMissing files: encrypt.py decrypt.py generate.py ")
        sys.exit(1)

# CONFIG

# Wanna save logs of "decoding/encoding" texts to a text file?
save_logs = True # Put 'False' to disable this or 'True' to enable
# Where to save logs?
logs_file="logs.txt" # Working dir btw

# All the options
gen_kwrds = ['g', '-g', 'gen', '-gen', '--generate-key']
dec_kwrds = ['d', '-d', 'de', '-de', '--decrypt']
en_kwrds = ['e', '-e', 'en',  '-en', '--encrypt']

def Help():
    print(f"""
Crypto program --- USAGE
python3 {sys.argv[0]} [OPTION] [TEXT] # <-- recommended to use "" or ''

Example:
* Encrypt a text
python3 {sys.argv[0]} -en "Hello, World"

Options:
1: {gen_kwrds} <-- Generate a new crypto alphabet

2: {dec_kwrds} <-- Decrypt a text

3: {en_kwrds} <-- Encrypt a text

More:
- If it doesnt encrypt/decrypt all the letters of a word, just generate a new alphabet and try again
- Module files can be run directly from terminal (using: python3 modules/[MODULE-FILE].py)
""")

def print_alphabet():
    pass

def main():
    # check command line arguments

    if len(sys.argv) == 1:
        Help()
        return 1
    elif [x for x in gen_kwrds if x in sys.argv[1]]:
        generator = Generator("data.json")
        generator.main()
        return 0
    elif [ x for x in dec_kwrds if x in sys.argv[1]] and len(sys.argv) == 3:
        # decrypt the second argument 
        decryptor = Decryptor(data_file="data.json", save_data=save_logs, to_save_data_file=logs_file)
        decryptor.main(encrypted_text=sys.argv[2], decrypted_text="")
        return 0
    elif [x for x in en_kwrds if x in sys.argv[1]] and len(sys.argv) == 3:
        # encrypt the second argument
        encryptor = Encryptor(data_file="data.json", save_data=save_logs, to_save_data_file=logs_file)
        encryptor.main(decrypted_text=sys.argv[2], encrypted_text="")
        return 0
    else:
        Help()
        return 1

if __name__ == '__main__':
    sys.exit( main() )
