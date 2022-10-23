import random
import time

letter_list_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_list_lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_character = "!§$%&/()=?`*'-+\}][{"
password = []

print("\n")
print("Network Scanner V1.0")
print("******************************************************************")
print(r"""
╔═╗╦═╗╔╦╗╦ ╦╦ ╦╦═╗  ╔╦╗╦╔╗╔╔═╗╔═╗╦ ╦╔═╗╔╗╔
╠═╣╠╦╝ ║ ╠═╣║ ║╠╦╝  ║║║║║║║╠═╣╚═╗╚╦╝╠═╣║║║
╩ ╩╩╚═ ╩ ╩ ╩╚═╝╩╚═  ╩ ╩╩╝╚╝╩ ╩╚═╝ ╩ ╩ ╩╝╚╝       

https://www.som-it.net
""")
print("******************************************************************\n")


def list_to_string(list):
    tmp = ''.join(list)
    return tmp
    
print("Password Generator V0.1")
print("(1) 4 Stellen (Schwach)")
print("(2) 8 Stellen (Schwach)")
print("(3) 16 Stellen (Stark)")
print("(4) 32 Stellen (Stark)")
print("(5) 64 Stellen (Stark)")
print("(6) 128 Stellen (Unvorstellbar Stark)")
print("(7) 256 Stellen (Unvorstellbar Stark)")
print("\n")

while True:
    try:
        user_choice = int(input("Wählen Sie aus der oberen Liste die Länge Ihres Passwortes: "))
        if user_choice == 1:
            length = 4
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')
            
            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 2:
            length = 8
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 3:
            length = 16
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 4:
            length = 32
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 5:
            length = 64
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 6:
            length = 128
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        elif user_choice == 7:
            length = 256
            for x in range(length):
                password.extend(random.sample(letter_list_lower + letter_list_upper + numbers + special_character, 1))
            
            print("Generierung läuft...")
            time.sleep(1)
            print("Ihr Passwort lautet:" + '\033[1m', list_to_string(password), '\033[0m')

            with open(r'C:\Users\Arthur\Desktop\passwort.txt', 'a') as writer:
                writer.write(list_to_string(password) + '\n')
            print("Eine Datei wurde auf Ihrem Desktop erstellt bzw. aktualisiert.")

            user_break = str(input("Möchten Sie ein weiteres Passwort generieren [g] oder das Programm beenden [q] ? Wählen Sie [g] oder [q] aus: "))
            if user_break == 'g':
                password.clear()
                continue
            elif user_break == 'q':
                break

        else:
            print("Geben Sie eine der Nummern an !")

    except ValueError:
        print('\033[1m' + "Geben Sie einen Gültigen Wert ein." + '\033[0m')

print("\n")
print("Programmiert von " + '\033[4m' + "A.Minasyan" + '\033[0m' + " , 2022")
print("Auf Wiedersehen.")