import random
import string

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
def upperCase():
    upper_case = string.ascii_uppercase
    return upper_case    

# abcdefghijklmnopqrstuvwxyz
def lowerCase():
    lower_case = string.ascii_lowercase
    return lower_case

# 0123456789
def numbers():
    numbers = string.digits
    return numbers

# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
def symbols():
    symbols = string.punctuation
    return symbols

def passwordGenerator(length):
    password = []

    for i in range(length):
        password.append(random.choice(list(upperCase() + lowerCase() + numbers() + symbols())))
        
    return "".join(password)


length = input("How many characters do you want in your password? ")

try:
    length = int(length)

except ValueError as ve:
    print("You need a positive number for the length of your password")
    print(f"\'{length}\' is not a positive number")
else:
    print(f"Password: {passwordGenerator(length)}")