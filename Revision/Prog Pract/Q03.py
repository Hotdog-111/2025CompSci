# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

passwordAccepted = False
lengthCheck = False
digitPresent = False
uppercaseCheck = False
lowercaseCheck = False
notContainsPassword = False
notStartNumOrSpace = False
passw = []
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
password = input("Enter a password: ").strip()

while passwordAccepted == False:
    while lengthCheck == False:
        if len(str(password)) < 8:
            print("Password must be at least 8 characters long.")
            lengthCheck = False
            password = input("Enter a password: ").strip()
        else:
            break
    for i in password:
        passw.append(i)
    while digitPresent == False:
        for i in range(len(password)):
            if password[i].isdigit():
                digitPresent = True
                break
            else:
                digitPresent = False
        if digitPresent == False:
            print("Password must contain at least one digit.")
            password = input("Enter a password: ").strip()
            break

    while uppercaseCheck == False or lowercaseCheck == False:
        for i in range(len(password)):
            if password[i].isupper():
                uppercaseCheck = True
            elif password[i].islower():
                lowercaseCheck = True

        if lowercaseCheck == False or uppercaseCheck == False:
            print("Password must contain at least one uppercase letter and one lowercase letter.")
            password = input("Enter a password: ").strip()
            break

    while notContainsPassword == False:
        for i in range(len(password)):
            if "password" in password.lower():
                notContainsPassword = False
            else:
                notContainsPassword = True
        if notContainsPassword == False:
            print("Password must not contain the word 'password'.")
            password = input("Enter a password: ").strip()
            break

    while notStartNumOrSpace == False:
        if password[0].isdigit() or password[0] == " ":
            print("Password must not start with a number or space.")
            password = input("Enter a password: ").strip()
            break
        else:
            notStartNumOrSpace = True
            break
    passwordAccepted = True