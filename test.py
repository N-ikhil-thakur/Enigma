# from rotate import rotate_dict_keys , rotate_dict_values , interchange_keys_values

# age = {'Nikhil':18 , 'Niraj':14 , 'Nikita':21 , 'Mom':35}

# age = interchange_keys_values(age)
# print(age)

# import random

# dic = {
#     'w1':{

#     }
# }
# import random
# array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#          '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '-', '+', '=', '_', "'", '"', ':', ';', '.', '/', ' ', '>', '<', '?', ',', '\\']

# new_array = array.copy()
# n = 0
# while(n < 7):
#     n += 1
#     random.shuffle(new_array)

#     print(dict(zip(array, new_array)))
#     print('\n')


from encryptor import EnigmaEncryptor

encryptor = EnigmaEncryptor(-2, 5, 1, 2, 3, 1, 4, 5, 2, 4, 5)
print(f'|{encryptor.encrypt("nnnnnnnnnn")}|')
print(encryptor.encrypt('/c>'))
