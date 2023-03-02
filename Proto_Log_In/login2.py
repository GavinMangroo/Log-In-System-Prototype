userinput = ""
i = ""
import os

class Profile:
    userName = ""
    password = ""
    securityQuestion1 = "What is your favourite colour?"
    securityQuestion2 = "What is the name of your favourite pet?"
    securityAnswer1 = ""
    securityAnswer2 = ""

def signUp():
    global userinput
    passwordverif = ""
    global prf 
    prf = Profile
    prf.userName = input("Enter a username: ")
    prf.password = input("Enter a password: ")
    passwordverif = input("Re-enter password for verification: ")
    while passwordverif != prf.password:
        passwordverif = input("Try again: ")
    print("\nWould you like to add a security question?\n1. Yes\n2. No\n")
    userinput = input("Type either 1 or 2: ")
    if userinput == "1":
        print(prf.securityQuestion1)
        prf.securityAnswer1 = input("Answer: ")
        print("\nWould you like add another security question?\n1. Yes\n2. No\n")
        userinput = input("Type either 1 or 2: ")
        if userinput == "1":
            print(prf.securityQuestion2)
            prf.securityAnswer2 = input("Answer: ")
        elif userinput == "2":
            pass
        else:
            print("Invalid Option!")           
    elif userinput == "2":
        pass
    else: 
        print("Invalid Option.")
    
    print("\nSuccessfully Signed Up!")


def logIn():
    global userinput
    count = 0
    name = input("Enter your username: ")
    while name != prf.userName:
        name = input("Invalid Username!\nTry again: ")
    print("Username Valid!\n")
    password = input("Enter your password (Only three(3) attempts): ")
    while password != prf.password:
        password = input("Invalid Password!\nTry again: ")
        count += 1
        if count == 3: 
            print("\nYou have expired all attempts.")
            print("Would you like to answer a security question?\n1. Yes\n2. No")
            userinput = input("Type 1 or 2: ")
            if userinput == "1" and prf.securityAnswer1 or prf.securityAnswer2 != "":
                print("Which question would you like to answer?\n1. ", prf.securityQuestion1, "\n2. ", prf.securityQuestion2)
                userinput = input("Type 1 or 2: ")
                if userinput == "1":
                    print(prf.securityQuestion1)
                    userinput = input("Answer: ")
                    while userinput != prf.securityAnswer1:
                        userinput = input("Try Again: ")
                    print("Correct!")
                    break
                elif userinput == "2":
                    print(prf.securityQuestion2)
                    userinput = input("Answer: ")
                    while userinput != prf.securityAnswer2:
                        userinput = input("Try again: ")
                    print("Correct!")
                    break
                else:
                    print("Invalid Option!")
                    exit()
            elif userinput == "2":
                exit()
            else:
                print("Invalid Option!")
                exit()

    if password == prf.password: print("Valid Password!")
    print("\nSuccessfuly Logged In!\n")


while True:
    print("Welcome to The Sphinx's Log In test!\n\nWould you like to create an account?\n1. Yes\n2. No\n")
    i = input("Please select the number that correspond to your choice: ")
    if i == "1":
        signUp()
        print("\nYou've created your account!\n\nWould you like to log in?\n1. Yes\n2. No")
        i = input("Please select the number that correspond to your choice: ")
        if i == "1":
            os.system('cls')
            logIn()
            break
        elif i == "2":
            break
        else:
            print("Invalid Option!")
    elif i == "2":
        break
    else:
        print("Invalid Option!")

print("\n\nThank you for testing for The Sphinx!")
    






