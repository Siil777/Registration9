from typing import Any
from module1 import*
import sys
import string
from re import*


from JsonX import*

while True:
    command = input("Enter 1 to register, 2 to login, 0 to exit: ")
    if command == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
        save_to_file(users)
    elif command == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            break
    elif command == "0":
        save_to_file(users)
        break
    else:
        print("Invalid command.")
