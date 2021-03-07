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

# get user input
name = input("Enter a name:")

# print value in the dictionary by giving it a string name as the key if the name exists
if name in birthdayDictionary:
    print(name +  "'s birthday is: " + birthdayDictionary[name])

# print no information found if name is not in the dictionary    
else:
    print("No information for " + name + " found.")
