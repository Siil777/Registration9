from typing import Any
from module1 import*
import sys
import string
from re import*
from module1 import get_data

while True:
        print("Write 1 for reg, 2 for login, or 0 for exit")
        cmd = input()
        if cmd == '1':
            add_user=()
        elif cmd=='2':
            add_user=()
        elif cmd == '0': 
            sys.exit()
        else: print("Wrong command")

        while True:
                login = input("Enter login: ")
                passw = input("Enter password: ")
                if login not in logins and cmd=='1':

                    print("Success.")
                    break
                if login in logins and cmd=='2':
                    print('you logened')
                    
                    break
                if login not in logins and cmd=='2':
                    print('you ought to register for start')
                    break
                else: print("There is a user with this username. Try again with other username.")
                break
