
# import random, define a base string for password, name, and characters in password
import random

password = ""

name = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#$%&"

# while loop to ensure a password is outputted
while password == "":
    # limit input
    limit = int(input("Thanks for using python password generator!\n"
                      "How many characters would you like in your password? (minimum of 6): "))
    # name input
    name = (input("What would you like to name the password?: "))
    # character limiter
    if limit < 6:
        print("The minimum password length is 6")
    else:
        # character selector
        for c in range(limit):
            password += random.choice(chars)
# print statement
print(name + "\n" + password)
