from argparse import ArgumentParser 
import secrets

letter_list_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_list_lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_character = "!§$%&/()=?`*'-+\}][{@;.~_#,"
password = []

print("\n")
print("******************************************************************")
print(r"""
   ___                  _____         
  / _ \ ___ _ ___  ___ / ___/___  ___ 
 / ___// _ `/(_-< (_-</ (_ // -_)/ _ \
/_/    \_,_//___//___/\___/ \__//_//_/
                                      
Author: B0lg0r0v
https://root.security
""")
print("******************************************************************\n")


def listToString(list):
    tmp = ''.join(list)
    return tmp

def generation(value):
    for x in range(value):
        password.extend(secrets.choice(letter_list_lower + letter_list_upper + numbers + special_character))

    return listToString(password)

def main():
    parser = ArgumentParser()
    parser.add_argument('-l', '--length', help='Desired password length.')
    parser.add_argument('-v', '--version', action='version', version='PassGen V1.0')
    parser.epilog = "4 digits (Weak), 8 digits (Weak), 16 digits (Strong), 32 digits (Very Strong), 64 digits & above (Uncrackable)"
       
    args = parser.parse_args()

    try:
        if args.length is not None:
            print(f"Generated password: {generation(int(args.length))}")
        else:
            print("Usage: passgen.py [-l LENGTH] [-h HELP]")
    except ValueError:
        print("Please enter a valid number.")

main()
