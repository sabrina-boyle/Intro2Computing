"""
Program: Phones
Author: sabsing

This program uses a list of names and their corresponding phone numbers to give the user
the phone number needed based on the inputted name. 

Inputs: Either a last name, or a first and last name
Outputs: The full name of the inputted name and their corresponding phone number
"""

while True:
    userInput = input("Enter a last name, or first and last name: ").lower()
    userList = userInput.split()
    if userInput == "" or userInput == " ":
        break
    elif len(userList) > 2:
        print("Error: No more than two names. Try again")
    else:
        phones = open("phones.txt", 'r')
        #first and last name
        if len(userList) == 2:
            while True:
                data = phones.readline()
                dataList = data.split()
                if data == "":
                    break
                elif dataList[0].lower() == userList[0] and dataList[1].lower() == userList[1]:
                    print(dataList[0], dataList[1]+",", dataList[2])

        #last name only
        else:
            while True:
                data = phones.readline()
                dataList = data.split()
                if data == "":
                    break
                elif dataList[1].lower() == userList[0]:
                    print(dataList[0], dataList[1]+",", dataList[2])
