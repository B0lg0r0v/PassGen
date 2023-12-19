from argparse import ArgumentParser 
import secrets
import os
import sys
import base64
from cryptography.fernet import Fernet
import pyperclip
from colorama import init as colorama_init
from colorama import Fore
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

#----------------Function to generate password----------------#

def generatePassword(length, chars):
    try:
        return ''.join(secrets.choice(chars) for i in range(length))
    
    except Exception as e:
        print(f'\n{indent} {Fore.RED}Error.{Fore.RESET}')
        sys.exit(1)

#----------------Function to encrypt and decrypt passwords----------------#

def decryptPassword(key, encryptedPassword):

    try:
        f = Fernet(key)
        decryptedPassword = f.decrypt(encryptedPassword.encode())
        return decryptedPassword.decode()

    except Exception as e:
        print(f'\n{indent} {Fore.RED}Error.{Fore.RESET}')
        sys.exit(1)


def encryptPassword(password):
    try:
        passwordProvided = password
        passwordToEncrypt = passwordProvided.encode()  # Convert to type bytes

        keyPassword = secrets.token_bytes(32)

        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000,#reconmended by OWASP
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(keyPassword))  # Can only use kdf once
        f = Fernet(key)
        encryptedPassword = f.encrypt(passwordToEncrypt)
        print(f'{indent} Encrypted password: {Fore.LIGHTYELLOW_EX}{encryptedPassword}{Fore.RESET}')
        print(f'{indent} Symmetric Key: {Fore.LIGHTYELLOW_EX}{key}{Fore.RESET}')
        print(f'{indent}{Fore.LIGHTRED_EX} Be sure to save the symmetric key somewhere safe. If you lose it, you will not be able to decrypt the password.{Fore.RESET}')

    
    except KeyboardInterrupt:
        print(f'\n{indent} {Fore.RED}Canceled.{Fore.RESET}')
        sys.exit(1)

    except Exception as e:
        print(f'\n{indent} {Fore.RED}Error.{Fore.RESET}')
        sys.exit(1)


#----------------------------------------------------------------------#
        
def main():
    
#----------------List of characters----------------#

    letterListUpper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterListLower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    specialCharacter = "!§$%&/()=?`*'-+\}][{@;.~_#,"
    charset = ''
    password = []
    storedPassword = []

#--------------------------------------------------#

    parser = ArgumentParser(
    prog='passgen.py',
    usage='%(prog)s [options]',
    description='Password generator with security in mind.'
)

    group = parser.add_argument_group('Password options')

    group.add_argument("-l", "--length", type=int, help="Specify the password length. Default is 20.")
    group.add_argument("-n", "--number-passwords", type=int, help="Specify the number of passwords to generate. Default is 1.")
    group.add_argument("-c", "--clipboard", action="store_true", help="Copy the generated password to the clipboard. Only works with one password at a time.")
    group.add_argument("-e", "--encrypt", help="Encrypt a password with AES-256. Only works with one password at a time.")
    group.add_argument("-de", "--decrypt", nargs=2, metavar=('KEY', 'PASSWORD'), help="Decrypt a password given the key and the encrypted password.")
    group.add_argument("-o", "--output", help="Save the generated password to a file.")

    group = parser.add_argument_group('Exclude options')

    group.add_argument("-ex", "--exclude-specific", help="Exclude specific characters from the password.")
    group.add_argument("-exl", "--exclude-lower", action="store_true", help="Exclude lowercase letters from the password.")
    group.add_argument("-exs", "--exclude-special", action="store_true", help="Exclude special characters from the password.")
    group.add_argument("-exu", "--exclude-upper", action="store_true", help="Exclude uppercase letters from the password.")
    group.add_argument("-exd", "--exclude-digits", action="store_true", help="Exclude digits from the password.")
    
    args = parser.parse_args()

    charset = ''

    #----------------Check if the user has selected any options----------------#
    
    if not args.decrypt and not args.encrypt:
    
        if args.length:
            length = args.length

            if length < 1:
                print(f'{indent} {Fore.RED}The minimum password length is 1 character.{Fore.RESET}')
                sys.exit(1)

            # Prevent the user from generating a password with a length greater than 256
            elif length > 256:
                print(f'{indent} {Fore.RED}The maximum password length is 256 characters.{Fore.RESET}')
                sys.exit(1)

        else:
            length = 20

        if args.number_passwords:
            numberPasswords = args.number_passwords
        else:
            numberPasswords = 1        
    
        if not args.exclude_lower:
            charset += letterListLower
        
        if not args.exclude_upper:
            charset += letterListUpper
        
        if not args.exclude_digits:
            charset += numbers
        
        if not args.exclude_special:
            charset += specialCharacter
        
        if args.exclude_specific:
            for i in args.exclude_specific:
                charset = charset.replace(i, '')
    
        password.append(charset)

        chars = ''.join(password)


        for i in range(numberPasswords):
            storedPassword.append(generatePassword(length, chars))
            print(f'{indent} -----> {Fore.GREEN}{storedPassword[i]}{Fore.RESET}')

        if args.output:
            outputPath = os.path.normpath(args.output)
            if os.path.isabs(outputPath) or '..' in outputPath: #Trying to prevent path traversal
                print(f'{indent} {Fore.RED}Invalid path.{Fore.RESET}')
                sys.exit(1)
            
            else:
                try:
                    with open(outputPath, 'w') as f:
                        for i in range(numberPasswords):
                            f.write(f'{storedPassword[i]}\n')
                    print(f'{indent} {Fore.LIGHTBLUE_EX}Passwords saved to {outputPath}.{Fore.RESET}')
                except Exception as e:
                    print(f'\n{indent} {Fore.RED}Error.{Fore.RESET}')
                    sys.exit(1)    
        
        if args.clipboard:
            pyperclip.copy(storedPassword[0])
            print(f'{indent} {Fore.LIGHTBLUE_EX}Password copied to clipboard.{Fore.RESET}')
            
            
    #----------------Check if the user has selected the encrypt option----------------#

    # Function to encrypt a password with AES-256
    if args.encrypt:
        encryptPassword(str(args.encrypt))
     
    # Function to decrypt a password given the key and the encrypted password
    if args.decrypt:
        try:
            key, encryptedPassword = args.decrypt
            print(f'{indent} Decrypted password: {Fore.LIGHTGREEN_EX}{decryptPassword(key, encryptedPassword)}{Fore.RESET}')
        
        except KeyboardInterrupt:
            print(f'\n{indent} {Fore.RED}Canceled.{Fore.RESET}')
            sys.exit(1)

    #----------------------------------------------------------------------------------#
    

if __name__ == "__main__":

    print(r"""
          
   ___                  _____         
  / _ \ ___ _ ___  ___ / ___/___  ___ 
 / ___// _ `/(_-< (_-</ (_ // -_)/ _ \
/_/    \_,_//___//___/\___/ \__//_//_/
                                        

    Author: B0lg0r0v
    https://root.security
    """)
    print("\n")

    indent = ' ' * 3

    colorama_init(autoreset=True)
    main()



    



