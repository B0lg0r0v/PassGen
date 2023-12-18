# PassGen

<p align='center'>
   <img width='700' src='https://github.com/B0lg0r0v/PassGen/assets/115954804/1ad23371-648c-46e9-ae29-cb61984d3b9c'>
</p>

# Table of Contents

- [PassGen](#passgen)
  * [Why PassGen ?](#why-passgen)
  * [General Information](#general-information)
  * [Usage](#usage)
  * [Features Overview](#features-overview)
  * [Installation](#installation)
  * [Disclaimer](#disclaimer)

## Why PassGen 

- PassGen provides several options for customizing the generated passwords.
- It includes options for encrypting and decrypting passwords using AES-256. This feature can add an extra layer of security by allowing users to store and transfer their passwords in an encrypted format.
- PassGen can copy the generated password to the clipboard or save it to a file
- Open Source
- Unlike other password generators, PassGen runs locally and doesn't require an internet connection.

## General Information

- When using the encryption argument, make sure to put your password between `""`. This is because if you have special characters in your password, your terminal can missinterpret them. This can lead to breaking your password and encrypting something else.

## Usage

```
usage: passgen.py [options]

Password generator with security in mind.

optional arguments:
  -h, --help            show this help message and exit

Password options:
  -l LENGTH, --length LENGTH
                        Specify the password length. Default is 20.
  -n NUMBER_PASSWORDS, --number-passwords NUMBER_PASSWORDS
                        Specify the number of passwords to generate. Default is 1.
  -c, --clipboard       Copy the generated password to the clipboard. Only works with one password at a time.
  -e ENCRYPT, --encrypt ENCRYPT
                        Encrypt a password with AES-256. Only works with one password at a time.
  -de KEY PASSWORD, --decrypt KEY PASSWORD
                        Decrypt a password given the key and the encrypted password.
  -o OUTPUT, --output OUTPUT
                        Save the generated password to a file.

Exclude options:
  -ex EXCLUDE_SPECIFIC, --exclude-specific EXCLUDE_SPECIFIC
                        Exclude specific characters from the password.
  -exl, --exclude-lower
                        Exclude lowercase letters from the password.
  -exs, --exclude-special
                        Exclude special characters from the password.
  -exu, --exclude-upper
                        Exclude uppercase letters from the password.
  -exd, --exclude-digits
                        Exclude digits from the password.
```

## Features Overview

*Command:* `python3 passgen.py -l 35 -n 2 -exd -o MyOutput.txt`

<p align='left'>
<img width='800' src='https://github.com/B0lg0r0v/PassGen/assets/115954804/9126aa07-c404-4c92-9df0-a43ba2e2a9d2'>
</p>
<br>

*Command:* `python3 passgen.py -e "MySecurePassword"`

<p align='left'>
<img width='800' src='https://github.com/B0lg0r0v/PassGen/assets/115954804/ba044324-ab8f-4d27-b220-d79be0febf68'>
</p>

*Command:* `python3 passgen.py -de <KEY> <ENCRYPTED PASSWORD>`

<p align='left'>
<img width='800' src='https://github.com/B0lg0r0v/PassGen/assets/115954804/97549bd0-e097-4217-9412-b2d0365701c9'>
</p>

## Installation

```
git clone https://github.com/B0lg0r0v/PassGen.git
cd PassGen
pip3 install -r requirements.txt
```

## Disclaimer

This tool is primarly created for me as a project to enhance my coding skills and start creating some red team / blue team tools. It is not considered to be the most efficient tool out there.
