#Login for a random program V2.0
import getpass, re, time, base64 

def uname():
    global create_uname
    create_uname = raw_input("Enter the username your would like: ")
    
def menu():
    while True:      
        menu = raw_input("1) Login\n2) Create an account\n3) Exit\n> ")
        if menu == "1":
            loginn()       
        elif menu == "2":
            account()
        elif menu == "3":
            exit()
        else:
            print "Please enter a valid option"
def account():
    f = open("database.txt","a+")
    create_name_first = raw_input("Enter your first name: ")
    create_name_last = raw_input("Enter your last name: ")
    uname()          
    for line in f:
        while True:
            if str(create_uname) not in line:
                    break
            else:
                print "Sorry this username is already taken. Please pick another..."
                uname()
    f.write("----------")
    f.write("\n")
    f.write("First Name: ")
    f.write(create_name_first)
    f.write("\n")
    f.write("Last Name: ")
    f.write(create_name_last)
    f.write("\n")
    f.write("Username: ")
    f.write(create_uname)
    f.write("\n")
    f.close()
    password()
        

def password(): #This bit makes sure they have a valid password
    f = open("database.txt", "a")
    pwd , pwdcheck = None , None
    pwd = getpass.getpass("Please choose a password: ")
#    pwdcheck = open("pwdcheck.txt", "a") #Common passords
#    checkpwd = base64.encodestring(pwd) 
#    for line in pwdcheck:
#                while True:
#                    if str(checkpwd) not in line:
#                            break
#                    else:
#                        print "Sorry this password is already taken. Please pick another..."
#                        password()
    while True:  
        if (len(pwd)<6):
            print("Not a Valid Password")
            password()
        elif not re.search("[a-z]",pwd): 
            print("Not a Valid Password")
            password()
        elif not re.search("[0-9]",pwd): 
            print("Not a Valid Password")
            password()
        elif not re.search("[A-Z]",pwd): 
            print("Not a Valid Password")
            password()
        else:
            pwdcheck = getpass.getpass("Please re-type your password: ")
            if pwdcheck == pwd:
                pwd_encode = base64.encodestring(pwd) #Encrypts password
                f.write("User ID: ")
                uid1 = base64.encodestring(create_uname) #Element 1
                uid2 = base64.encodestring(str(len(pwd))) #Element 2
                uid3 = base64.encodestring(uid1+uid2) #Final user ID
                f.write(uid3)
                f.write("Password: ")
                display_pwd = base64.encodestring(pwd_encode+uid3) #Makes the displayed pwd
                f.write(display_pwd)
                f.write("\n")
                f.close()
                print "You have successfully made an account."
                time.sleep(2)
                menu()
            else:
                print "You entered wrong, try again"
                password()
        
def loginn(): #if it was called 'login' it would be confused with the filename
    global f 
    login_username = raw_input("Please enter your username: ")
    a = 0
    b = 0
    f = open("database.txt", "r") #Opens file for reading
    for line in f:
        if login_username in line:
            a = int(1)
    f.close() #Closes to avoid confusion with password
    if a == 0:
        print "Incorrect username."
        loginn()
        
    while True:
        login_password = str(getpass.getpass("Please enter your password: ")) #User enters password
        user_id_1 = base64.encodestring(login_username) #Steps to encrypt
        user_id_2 = base64.encodestring(str(len(login_password)))
        user_id_3 = base64.encodestring(user_id_1+user_id_2)
        login_password_encode = base64.encodestring(login_password) #Creates a hashed password
        enc_login_password = base64.encodestring(login_password_encode+user_id_3)#Follows same algorithm as creating password
        f = open("database.txt", "r")
        for line in f:
            if enc_login_password in line: #Checks if it is in lines
                b = int(1)
        f.close()      
        if a + b == 2:
            program() #Runs program
            menu() #Goes back to menu
        else:
            print "Incorrect password." #Tells if password is wrong
    

def program():
    print "Hello World"
    
menu()
