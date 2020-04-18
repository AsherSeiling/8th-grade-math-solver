def problemlist():
    print('List')
def ynrspble():
    print("Would you like to go back to start? Y/N")
    yorn = input("")
    if yorn.lower() == "y":
        problemlist()
    else:
        if yorn.lower() == "n":
            print("Thank you for using Seiling math solver v")
        else:
            print("Syntax error")
#--------------------------------------------------------------