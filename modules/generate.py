#!/usr/bin/env python3

"""
This is a two-in-one file.
It can be run directly with python (to generate the thing)
or can be run from the main script ( main.py )
"""

import random
import json
import platform
from os import system

class Generator:
    def __init__(self, data_file):
        # list of all characters that our crypto alphabet will contain...
        # REMOVED DOUBLE PARENTESIS '\"'
        # REMOVED NEW LINE (dont know why added it) '\n'
        # REMOVED a symbol that possibly caused many conflicts '`'
        # DID NOT YET REMOVE A SLASH

#       English/Spanish only
        self.normal_symbols = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 
        'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'Ñ', 'ñ', 'O', 'o', 'P', 'p', 
        'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 
        'Z', 'z', 'Ç', 'ç', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', 
        '^', '&', '*', '(', ')', '-', '_', '=', '+', '|', '}', '{', '[', ']', "'",  ';',
         ':', '/', '?', '>', '<', ',', '.', '¿', '¡'] # , ' '

#       can add rus letters
#        self.normal_symbols = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 
#        'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 
#        'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 
#        'Э', 'э', 'Ю', 'ю', 'Я', 'я', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', 
#        '^', '&', '*', '(', ')', '-', '_', '=', '+', '|', '}', '{', '[', ']', "'",  ';',
#         ':', '/', '?', '>', '<', ',', '.',]

        self.encrypted_symbols = []
        self.crypto_alphabet = None
        self.data_file = data_file
        self.key = None
        self.b64_data_file = "key.txt" # <-- the key file. With this file we can create a specific crypto-alphabet and start using it

#   To improve this function
    def print_result(self):
        try:
            with open(self.data_file, 'r') as f:
                print(f.read())
        except:
            print("Oops, check line 47 in generate.py looks like the needed file wasn't specified (Not a Fatal error)")

    def generate_alphabet(self):
        add = random.sample(self.normal_symbols, len(self.normal_symbols))

        for each_one in add:
            self.encrypted_symbols.append(each_one)

        crypto_alphabet = dict(zip(self.encrypted_symbols, self.normal_symbols))

        #print(crypto_alphabet)

        self.crypto_alphabet = crypto_alphabet

    def save_alphabet_result(self):
        with open(self.data_file, "w", encoding='utf-8') as file:
#           Set ensure_ascii to False if don't wanna see \u00f1 like text (it's ñ) but on windows spanish letter then won't work
            json.dump(self.crypto_alphabet, file, indent=4, ensure_ascii=True)

#   I think will get rid of this func
    def encode_alphabet_file(self):

        if platform.system() == 'Linux':
            # on linux i found an easy way to encode files, so i use this for linux 
            system(f"base64 {self.data_file} > {self.b64_data_file}")

        else:
#            print("Could not encode the alphabet file, cause: Windows not supported")
            system(f"certutil -encode {self.data_file} {self.b64_data_file} > __archivo_temporal.txt")
            system("del /F /Q __archivo_temporal.txt")

#   this function is to be ran if the crypto.py is calling it
# i mean if i run: python3 main.py -gen
    def main(self):
        Generator.generate_alphabet(self)
        Generator.save_alphabet_result(self)
        #Generator.print_result(self)
        #Generator.encode_alphabet_file(self)

#   this function is to be ran if im running only the generate.py
# i mean if i run directly: python3 generate.py
    def solo_main(self):
        generator.generate_alphabet(self)
        generator.save_alphabet_result(self)
        #generator.print_result(self)
        #generator.encode_alphabet_file(self)        


if __name__ == '__main__':
    generator = Generator("data.json")
    generator.main()
