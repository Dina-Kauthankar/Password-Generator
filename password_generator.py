import random
import string

print("===== PASSWORD GENERATOR =====")

# User inputs
length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower()
use_lower = input("Include lowercase letters? (y/n): ").lower()
use_digits = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if use_upper == 'y':
    characters += string.ascii_uppercase
if use_lower == 'y':
    characters += string.ascii_lowercase
if use_digits == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print(" Error: Please select at least one character type.")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("\n Generated Password:", password)