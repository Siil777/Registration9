import sys

with open('file.txt', 'r') as base:
    """w+ open a file for readin and saving smth
    """
    data = base.readlines()
    """ readlines () read each str of file 
    """
 
users = {}
"""users = {} list of users
"""
for user in data:
    """data from readlines() is being tied with name and password
    it lets us read each str which will
    be inputed by user: alphabet or digit
    """
    name = user.split()[1]
    """Thanking to readlines() [1] and [0]
        Can write on what line password and name
    """
    password = user.split()[0]
    users[name] = password
 
 
logins = users.keys()
 
 
def get_data(passw) -> tuple:
    """ tuple: also a list, but can consist different type
    of data listed by commas.
    """
    global users
    """function clobal is writed 1 time and has impact on all function
    in file
    """
    logins = users.keys()

    users[login] = passw
  
 
    return (login, passw)
 
 
def add_user(passw):
    data: tuple = get_data()
    with open('file.txt', 'r+') as base:
        base.write(data[0] + " " + data[1] + '\n')
