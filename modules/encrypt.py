#!/usr/bin/python3

import sys
import json
import os.path
import os
import platform

class Encryptor:
    def __init__(self, data_file, save_data, to_save_data_file):
        self.crypto_alphabet = None
        self.data_file = data_file
        self.encrypted_text = ""
        self.decrypted_text = None
        self.to_save_data_file = to_save_data_file
        self.save_data = save_data
        self.b64_data_file = "key.txt"

#       This could be a future feature
        #self.need_a_file = True # <-- if True, then program will encrypt a specific file's content

    def load(self):

        # check if we have a decrypted crypto alphabet already
        if os.path.isfile(self.data_file):
            with open(self.data_file, "r") as f:
                self.crypto_alphabet = json.load(f)
                f.close()

        elif os.path.isfile(self.b64_data_file):
            print(f"First decrypt {self.b64_data_file} with 'key_manager.py' and '-de' option\n")
            sys.exit(1)
           # decode base64, use bash or cmd commands
           # the commented code below doesnt work, just use the modeules/key_manager script with -de option before
        #    os.system(f"certutil -decode {self.b64_data_file} data.txt"); os.system("ren data.txt " + self.data_file ) if platform.system == "Windows" else os.system(f"base64 -d {self.b64_data_file} > {self.data_file}")
        #    with open(self.data_file, "r") as f:
        #        self.crypto_alphabet = json.load(f)
        #        f.close()

        else:
            raise FileNotFoundError ("\nFile: '" + self.data_file + "' or '"+ self.b64_data_file +"' does not exist!\nWe need a crypto alphabet's file to be able to encrypt\nOr if needed file exists, then change data_file's name in variables")

    def encrypt(self, decrypted_text):
        self.decrypted_text = decrypted_text

        for each_char in decrypted_text:

            # if there is something that does not exist, and this char just contains spaces, then we'll translate it to just one space
            if each_char not in self.crypto_alphabet:
                if each_char.isspace():
                    self.encrypted_text += " "

                else:
                    print("Character: " + each_char + "\nDoes not exist in the crypto alphabet")
                    sys.exit(1)
            else:       
                self.encrypted_text += self.crypto_alphabet[each_char]

    def print_result(self):
        print(f"""
Decrypted: {self.decrypted_text}

Encrypted: {self.encrypted_text}
""")

    def function_save_data(self):
        from datetime import datetime
        with open(self.to_save_data_file, 'a') as f:
            f.write(f"""
{datetime.today().strftime('%Y-%d-%m %H:%M:%S')}
Decrypted: {self.decrypted_text}

Encrypted: {self.encrypted_text}
""")
            print(f"Data saved to '{self.to_save_data_file}'")
            f.close()

    def main(self, decrypted_text, encrypted_text):
        Encryptor.load(self)

        # Encrypt the single argument
        #print(sys.argv[1:]) # why not, to see what argument i put and what text to encrypt

        for e in decrypted_text: # 1: is to ignore 0 argument, which is program's name
            encrypted_text += e

        Encryptor.encrypt(self,decrypted_text)

        Encryptor.print_result(self)
        if self.save_data:
            Encryptor.function_save_data(self)

##################################

    def solo_main(self):
        encryptor.load()
        if len(sys.argv) == 1:
            encryptor.encrypt("Hello, World") 
        elif len(sys.argv) == 2:
            encryptor.encrypt(sys.argv[1])
        # check multiple arguments
        else:
            decrypted_text  = "" 

            for e in sys.argv[1:]: # 1: is to ignore 0 argument, which is program's name
                decrypted_text += e
            encryptor.encrypt(decrypted_text)

        encryptor.print_result()

        if self.save_data:
            encryptor.function_save_data()

if __name__ == '__main__':
    encryptor = Encryptor("data.json", False, "DATA.txt")
    encryptor.solo_main()
