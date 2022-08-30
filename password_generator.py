#Version-1
#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


t = ""
x = ""
y = ""

for int in range(nr_letters):
    t = t + letters[random.randrange(0, len(letters))]

for sym in range(nr_symbols):
    y = y + symbols[random.randrange(0, len(symbols))]

for nbr in range(nr_numbers):
    x = x + numbers[random.randrange(0, len(numbers))]
password = x + t + y
key = ''.join(random.choice(password) for i in range(len(password)))

print("Your password is: ", key)


#Version-2

