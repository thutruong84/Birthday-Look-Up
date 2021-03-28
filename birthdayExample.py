import json

# full path
pathToFile = "/Users/Admin/Desktop/BirthdayLookup/source/birthday.json"


# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

    birthdayDictionary[name] = birthday

# create a list of full names
fullName = list(birthdayDictionary.keys())

# create lists of first names and last names only
firstName = []
lastName = []

for j in fullName:
    firstName.append(j.split()[0])
    lastName.append(j.split()[1])

# Create a function searchName that takes in a name and a list of a name (full, first, or last) to be used
# Function returns the birthday(s) for the input name if the name exists in the birthday dictionary
# Function returns nothing if the name does not exist in birthday dictionary
def searchName(name,nameList):

    #print value in the dictionary by giving it a string name as the key if the name exists
    if name in nameList:
        print("Here is the list of name(s) and birthday(s) you are searching for:")
        for index in range(len(nameList)):
            if nameList[index] == name:
                entireName = fullName[index]
                print(entireName + " " + birthdayDictionary[entireName])
            
    # print no information found if name is not in the dictionary 
    else:
        print("No information found for " + name)



# create a menu function to display menu option and get user input

def menu():
    print("---Enter a letter to select search option or 'q' to quit---")
    print("[a] Search by full name")
    print("[b] Search by last name")
    print("[c] Search by first name")
    print("[q] Quit this program")
    option = input("Choose an option:")
    return option
    
# create a while loop that will quit the program if user enters "q"

choice = menu()

while (choice != "q"):

    # get user's input for the name
    name = input("Enter a name:")

    # process name to capitalize first letter of full name, first name, or last name
    if " " in name:
        first = name.split(" ")[0]
        last = name.split(" ")[1]
        name = first.capitalize() + " " + last.capitalize()
    else:
        name = name.capitalize()

    if choice == "a":
        searchName(name, fullName)
        choice = menu()
        
    elif choice == "b":
        searchName(name,lastName)
        choice = menu()
        
    elif choice == "c":
        searchName(name,firstName)
        choice = menu()
        
    else:
        print("Your choice is not valid")

        












    