# Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
#  Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be.
# For weak passwords, pick a word or two from a list.

import random
import string
import time


def strongPassword():
    password = ""
    lowerChar = string.ascii_lowercase
    upperChar = string.ascii_uppercase

    for i in range(0, 5):
        password += str(random.randint(1, 9))
        password += random.choice(lowerChar)
        password += str(random.randint(1, 9))
        password += random.choice(upperChar)

    print("Your Strong Password is")
    print(password)


def intermediatePassword():
    password = ""
    lowerChar = string.ascii_lowercase

    for i in range(0, 3):
        password += str(random.randint(1, 9))
        password += random.choice(lowerChar)
        password += str(random.randint(1, 9))

    print("Your Intermediate Password is")
    print(password)


def weakPassword():
    wordList = ["senha", "meunome", "hacker",
                "virus", "naosouasenha", "esqueci"]
    password = ""

    for i in range(0, 2):
        password += random.choice(wordList)

    print("Your Weak Password is")
    print(password)


def anotherPassword():
    userInput = input("Do you want another password? (y/n): ")
    if userInput.lower() == "y":
        return 1
    else:
        print("OK...Do welcome")
        time.sleep(2)
        exit()


def main():

    while True:
        userInput = int(input(
            "How do you want your password (strong(1), intermediate(2), weak(3)): "))
        if userInput == 1:
            strongPassword()
            if(anotherPassword()):
                continue

        elif userInput == 2:
            intermediatePassword()
            if(anotherPassword()):
                continue
        elif userInput == 3:
            weakPassword()
            if(anotherPassword()):
                continue
        else:
            print("ERROR: Wrong input number!")


main()
