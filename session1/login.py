#!/usr/bin/python3

usersData = {
    'Ahmed': '1394',
    'Ali': '6078',
    'Amr': '9345'
}

username = input("Please Enter User Name: ")
password = input("Please Enter Password: ")

if usersData.get(username) == password:
    print("Welcome Bro")
else:
    print("Incorrect Entry")
