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
    return ''.join(secrets.choice(chars) for i in range(length))

#-------------------------------------------------------------#


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
            iterations=300000,
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
    password = []
    storedPassword = []

#--------------------------------------------------#

    parser = ArgumentParser()

    parser.add_argument("-v", "--version", action="version", version="PassGen v1.0")
    parser.add_argument("-l", "--length", type=int, help="Password length. If not specified, the default length is 16.")
    parser.add_argument("-n", "--number-passwords", type=int, help="Number of passwords")
    parser.add_argument("-s", "--special", action="store_true", help="Only special characters.")
    parser.add_argument("-u", "--upper", action="store_true", help="Only uppercase.")
    parser.add_argument("-d", "--digits", action="store_true", help="Only digits.")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Copy password to clipboard. Works only with one password at a time.")
    parser.add_argument("-e", "--encrypt", help="Encrypts your password with AES-256. Works only with one password at a time.")
    parser.add_argument("-de", "--decrypt", action="store_true", help="Decrypt password with AES-256. Rquires the symmetric key.")
    parser.add_argument("-ex", "--exclude-specific", help="Exclude specific characters.")
    parser.add_argument("-exl", "--exclude-lower", action="store_true", help="Exclude lowercase.")
    parser.add_argument("-exs", "--exclude-special", action="store_true", help="Exclude special characters.")
    parser.add_argument("-exu", "--exclude-upper", action="store_true", help="Exclude uppercase.")
    parser.add_argument("-exd", "--exclude-digits", action="store_true", help="Exclude digits.")

    
    args = parser.parse_args()

    
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

        if args.special:
            password.append(specialCharacter)
        
        if args.upper:
            password.append(letterListUpper)

        if args.digits:
            password.append(numbers)

        if args.exclude_lower:
            password.append(letterListUpper + numbers + specialCharacter)
        
        if args.exclude_upper:
            password.append(letterListLower + numbers + specialCharacter)
        
        if args.exclude_digits:
            password.append(letterListLower + letterListUpper + specialCharacter)
        
        if args.exclude_special:
            password.append(letterListLower + letterListUpper + numbers)
        
        if args.exclude_specific:
            password.append(letterListLower + letterListUpper + numbers + specialCharacter.replace(args.exclude_specific, ''))
        
        if not args.special and not args.upper and not args.digits and not args.exclude_lower and not args.exclude_upper and not args.exclude_digits and not args.exclude_special and not args.exclude_specific:
            password.append(letterListLower + letterListUpper + numbers + specialCharacter)


        chars = ''.join(password)


        for i in range(numberPasswords):
            storedPassword.append(generatePassword(length, chars))
            print(f'{indent} -----> {Fore.GREEN}{storedPassword[i]}{Fore.RESET}')
        
        if args.clipboard:
            pyperclip.copy(storedPassword[0])
            print(f'{indent} {Fore.LIGHTBLUE_EX}Password copied to clipboard.{Fore.RESET}')


    # Function to encrypt a password with AES-256
    if args.encrypt:
        encryptPassword(str(args.encrypt))
     
    # Function to decrypt a password given the key and the encrypted password
    if args.decrypt:
        try:
            key = input(f'{indent} Enter the symmetric key: ')
            encryptedPassword = input(f'{indent} Enter the encrypted password: ')
            print(f'{indent} Decrypted password: {Fore.GREEN}{decryptPassword(key, encryptedPassword)}{Fore.RESET}')
        
        except KeyboardInterrupt:
            print(f'\n{indent} {Fore.RED}Canceled.{Fore.RESET}')
            sys.exit(1)



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

    indent = ' ' * 4
    colorama_init(autoreset=True)
    main()



    



