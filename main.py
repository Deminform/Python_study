import random

letters_count = int(input('How many letters would you like in your password?\n'))
symbol_count = int(input('How many symbols would you like?\n'))
numbers_count = int(input('How many numbers would you like?\n'))

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '}', '{', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/', '~', '`']
chars_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chars_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_chars = chars_lowercase + chars_uppercase

def symbol_generator(my_list, count):
    tmp_holder = ""
    if count != 0:
        for i in range(0, count):
            tmp_holder += str(my_list[random.randint(0, len(my_list) - 1)])
        return tmp_holder
    else:
        return ""     

password_char_list = list(symbol_generator(symbols, symbol_count) + symbol_generator(numbers, numbers_count) + symbol_generator(all_chars, letters_count))
random.shuffle(password_char_list)
password = ''.join(password_char_list)

print(f'Here is your password: {password}') 


