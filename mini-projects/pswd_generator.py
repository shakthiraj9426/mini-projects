# Password Generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
name_of_company = input("Where you are going to use this password? (eg:- facebook) :")

password_list = []

for password_letters in range(0,nr_letters):
  password_list += random.choice(letters)


for password_symbols in range(0,nr_symbols):
  password_list += random.choice(symbols)

for password_numbers in range(0,nr_numbers):
  password_list += random.choice(numbers)

# password_list = ''.join(random.sample(password_list,len(password_list)))

random.shuffle(password_list)

password = ''

for char in password_list:
    password += char


print(f"here is your new password for {name_of_company}: {password}")
print(f"Total characters :- {nr_letters+nr_symbols+nr_numbers}")