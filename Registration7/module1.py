import json
 
def save_to_file(users):
    with open('file.txt', 'w') as f:
        for user,password in users.items():
            f.write(f"{user} {password}\n")
 
def load_from_file():
    try:
        with open('file.txt', 'r') as f:
            data = f.read().split('\n')
            users={}
            for user in data:
                if user:
                    user,password=user.split()
                    users[user]=password
            return users
    except:
        return {}
 
users = load_from_file()
 
def login(username, password):
    if username in users:
        if users[username] == password:
            print("Success: You are logged in.")
            return True
        else:
            print("Error: Incorrect password.")
            return False
    else:
        print("Error: Incorrect username.")
        return False
 
def register_user(username, password):
    if username in users:
        print("Error: That username is already taken.")
        return
    else:
        users[username] = password
        print("Success: User registered.")
