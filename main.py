# Random Password Generator

from random import randint
from random import shuffle
from random import choice


def generate_uppercase_letter():
    uppercase_letter = chr(randint(65, 90))
    return uppercase_letter


def generate_lowercase_letter():
    lowercase_letter = chr(randint(97, 122))
    return lowercase_letter


def generate_special():
    sp1 = chr(randint(33, 47))
    sp2 = chr(randint(58, 64))
    sp3 = chr(randint(91, 96))
    sp_list_temp = [sp1, sp2, sp3]
    res_alnum = choice(sp_list_temp)
    return res_alnum


def generate_num():
    num_str = chr(randint(48, 57))
    return num_str


def shuffle_string(string_input):
    string_list = list(string_input)
    shuffle(string_list)
    return ''.join(string_list)


def convert_to_string(var):
    length = len(var)
    str1 = ""
    for i in range(length):
        str1 = str1 + var[i]
    return str1


nu, nl, nal, nn = input("Enter the number of uppercase, lowercase, special and numeric characters you want in "
                        "your password respectively (give a space after each number) : ").split()

uppercase_list = []
lowercase_list = []
sp_list = []
num_list = []

for j in range(int(nu)):
    uppercase_char = generate_uppercase_letter()
    uppercase_list.append(uppercase_char)
for j in range(int(nl)):
    lowercase_char = generate_lowercase_letter()
    lowercase_list.append(lowercase_char)
for j in range(int(nal)):
    sp = generate_special()
    sp_list.append(sp)
for j in range(int(nn)):
    num = generate_num()
    num_list.append(num)

uppercase_string = convert_to_string(uppercase_list)
lowercase_string = convert_to_string(lowercase_list)
sp_string = convert_to_string(sp_list)
num_string = convert_to_string(num_list)

temp_pass = f"{uppercase_string}{lowercase_string}{sp_string}{num_string}"
res_pass = shuffle_string(temp_pass)
print(f"Your randomly generated password is  {res_pass} \nLength : {len(res_pass)} characters long")
