# do not rely on it is just a practice project.
# it is not secure and safe to store you passwords 
# encryption used from cryptography module. - pip install cryptography
# encryption on pwd does not work.
# this code will generate two files - 1) passwordks.txt and 2) key.key

from cryptography.fernet import Fernet

# uncomment the below code when you run it for the forst time then comment it again
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# write_key() # once the jkey is generated comment it or remove it
''' # you the above dedf function only once to generate the key then you can comment it

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


pwd = input("Enter your master password: ")
key = load_key() + pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip()) # rstrip = removes the extra whitespaces
            user, passw = data.split("|") # split = divides or breaks the text from the location it told to, in this case it split the text data when it sees the "|"
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view an existing ones\n Type:\n add - to add a new password \n view - to view your existing password\n press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue