# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_secure_password():
    from random import shuffle, randint, choice



    #Password Generator function:

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your new secure Generated Password is: {password}")

generate_secure_password()

#########################################3
#
# #Password Generator function (longer code):
#
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# nr_letters = random.randint(8, 10)
# nr_numbers = random.randint(2, 4)
# nr_symbols = random.randint(2, 4)
#
# password_list = []
#
# # for char in range(nr_letters):
# #   password_list.append(random.choice(letters))
#
# #List Comprehension:
# password_letters = [random.choice(letters) for char in range(nr_letters)]
# # password_list += password_letters
# # print(password_list)
#
# ####
#
# # for char in range(nr_numbers):
# #   password_list += random.choice(numbers)
#
# #List Comprehension:
# password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
# # password_list += password_numbers
# # print(password_list)
#
# #####
#
# # for char in range(nr_symbols):
# #     password_list += random.choice(symbols)
#
# #List Comprehension:
# password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
# # password_list += password_symbols
# # print(password_list)
#
# #could also merge the 'password_list += password_letters' as well as numbers and symbols with this:
# password_list = password_letters + password_numbers + password_symbols
# # print(password_list)
#
# random.shuffle(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#
# print(f"Your new secure Generated Password is: {password}")
#
