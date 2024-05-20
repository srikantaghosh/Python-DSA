# Instruction

# Create a program will generate a password based on user inputs. Initial variables are already provided.

# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
# Your program should ask for number of letters, symbols and numbers initially
# Then based on these inputed values it will generate password
# Output can be like this:

# How many letters do you want in your password? 8
# How many numbers do you want in your password? 2
# How many symbols do you want in your password? 2
# Your password is: EDUpEYIG67*@

## Setting up initial variables:
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your password? "))
number_of_symbols = int(input("How many symbols do you want in your password? "))

## creating a empty password
password =  ""

for letter in range(1,number_of_letters+1):
    password += random.choice(letters)

for num in range(1,number_of_numbers+1):
    password += random.choice(nums)

for symbol in range(1,number_of_symbols+1):
    password += random.choice(symbols)

print(f"Your password is: {password}")

##shuffling the order of password

password_list = list(password)
random.shuffle(password_list)

advance_password = ""

for apc in password_list:
    advance_password += apc

print(f"Your advanced password is: {advance_password}")