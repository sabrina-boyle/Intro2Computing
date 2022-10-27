"""
Program:Lookup
Author: sabsing

This program uses three functions to take inputted requests from the user and output
the data requested by going through while loops, dictionaries, exception handling, optional
arguments, methods, and conditionals. The actual data is read in from a separate file.

Inputs: User chooses 1 for phone numbers and 2 for addresses. They then input a name.
Outputs: Either the phone number or address of the requested person.
"""
import sys

def inputAddresses():
    """ This function takes in the address information from a file and makes it into
    a dictionary. The dictionary is returned to the caller.
    """
    try:
        lookup = open("address.txt", 'r')
    except FileNotFoundError:
        print("error: file not found.")
        sys.exit(1)
    else:
        addresses = {}
        while True:
            data = lookup.readline()
            dataList = data.split(',')
            if data == "":
                break
            else:
                dataList[5] = dataList[5].strip("\n") 
                value = [dataList[1].strip(), dataList[2].strip(),
                         dataList[3].strip(), dataList[4].strip(), dataList[5].strip()]
                addresses[dataList[0].lower()] = value
        return addresses
    

def format_display(info, isPhone = True):
    """ This function formats the info retrieved from lookup based on the requested data
    (e.g. phone or address)
    """
    if isPhone:
        print("%-10s %s" % ("Phone:", info[4]))
    else:
        print("%-10s %s" % ("Street:", info[0]))
        print("%-10s %s" % ("City:", info[1]))
        print("%-10s %s" % ("State:", info[2]))
        print("%-10s %s" % ("Zip Code:", info[3]))
    
        

def main():
    """ This main function reads in input addresses, takes input from user and formats output
    according to requests.
    """
    ab = inputAddresses()

    # Double nested while loop to handle all input options
    while True:
        num = input("Lookup (1) phone numbers or (2) addresses: ").strip()
        if num == "":
            print("Thanks for using the boyle_lookup module!")
            break
        elif num < '1' or num > '2':
            print("error: must be either 1 or 2.")
            continue
        else:
            num = int(num)
            while True:
                try:
                    name = str(input("Enter space-separated first and last name: ")).lower()
                    personalData = ab[name]
                except ValueError:
                    print("error: not correct type.")
                    continue
                except KeyError:
                    if name == "":
                        print("")
                        break
                    else:
                        print("error: name not found.")
                        continue
                else:
                    if num == 1:
                        format_display(personalData)
                    else:
                        format_display(personalData, False)

if __name__ == "__main__":
    main()
