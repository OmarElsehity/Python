#!/usr/bin/python3

#----------------------------------------------------------------

l = [1, 2, 3, 4, 5, 6, 8, 4, 4, 1]

count = 0
for i in l:
    if i == 4:
        count += 1

print (count)

#----------------------------------------------------------------

# L = ['a', 'o', 'u', 'e', 'i']

# letter = input("Please Enter Letter: ")

# if letter.casefold() in L:
#     print ("Vowel")
# else:
#     print("Not Vowel")

#----------------------------------------------------------------
    
# import os

# path_var = os.environ.get('PATH')

# print(f"PATH: {path_var}")