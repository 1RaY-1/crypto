#!/usr/bin/python3

import json
import sys
import os
import os.path
import platform

class Decryptor:
    def __init__(self, data_file, save_data , to_save_data_file):
        self.data = None
        self.data_file = data_file
        self.decrypted_text = None
        self.encrypted_text = None
        self.to_save_data_file = to_save_data_file
        self.save_data = save_data
        self.b64_data_file = "key.txt"

    def load(self):

        # check if we have a decrypted crypto alphabet
        if os.path.isfile(self.data_file):
            with open(self.data_file, "r") as f:
                self.crypto_alphabet = json.load(f)
                f.close()

#       I think this peace of code below doesnt work...
        #elif os.path.isfile(self.b64_data_file):
          # decode base64, use bash or cmd commands
        #    os.system(f"certutil -decode {self.b64_data_file} {self.data_file}") if platform.system == "Windows" else os.system(f"base64 -d {self.b64_data_file} > {self.data_file}")
        #    with open(self.data_file, "r") as f:
        #        self.crypto_alphabet = json.load(f)
        #        f.close()

        else:
            raise FileNotFoundError ("\nFile: '" + self.data_file + "' or '"+ self.b64_data_file +"' does not exist!\nWe need a crypto alphabet's file to be able to encrypt data\nOr if needed file exists, then change data_file's name in variables")


    def decrypt(self, encrypted_text):
        self.encrypted_text = encrypted_text
        self.decrypted_text = ""

        try:
            for each_one in self.encrypted_text:
                if each_one not in self.crypto_alphabet:
                    if each_one.isspace():
                        self.decrypted_text += " "
                else:
                    self.decrypted_text += list(self.crypto_alphabet.keys())[list(self.crypto_alphabet.values()).index(each_one)]
        except KeyError:
            print("Character: " + each_one + "\nDoes not exist in the crypto alphabet")
            sys.exit(1)

    def print_result(self):
        print(f"""
Encrypted: {self.encrypted_text}

Decrypted: {self.decrypted_text}
""")

    def function_save_data(self):
        from datetime import datetime
        with open(self.to_save_data_file, 'a') as f:
            f.write(f"""
{datetime.today().strftime('%Y-%d-%m %H:%M:%S')}
Encrypted: {self.encrypted_text}

Decrypted: {self.decrypted_text}
    """)
            print(f"Data saved to '{self.to_save_data_file}'")
            f.close()

    def main(self, encrypted_text, decrypted_text):
        Decryptor.load(self)

        #print(sys.argv[1:])

        for e in encrypted_text: # '1:' is to ignore 0 argument, which is program's name
            decrypted_text += e

        Decryptor.decrypt(self,encrypted_text)

        Decryptor.print_result(self)

        if self.save_data:
            Decryptor.function_save_data(self)

    def solo_main(self):
        decryptor.load()

        if len(sys.argv) == 1:
            print("Enter some text, maybe?")
            sys.exit(1)

        elif len(sys.argv) == 2:
            decryptor.decrypt(sys.argv[1])

        # check multiple arguments
        else:
            #print("Text to decrypt: " + sys.argv[2:])

            for e in sys.argv[1:]: # '1:' is to ignore 0 argument, which is program's name
                decrypted_text += e

            decryptor.decrypt(encrypted_text)

        decryptor.print_result()

        if self.save_data:
            decryptor.function_save_data()

if __name__ == '__main__':    
    decryptor = Decryptor("data.json", False, "DATA.txt")
    decryptor.solo_main()
