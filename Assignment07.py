# ------------------------------------#
# Title: Assignment07.py
# Desc: This script performs basic math operations, handles errors and pickels data
# Change Log:
# 8.31.2019: Created script
# ------------------------------------#


# Step 1: Gather user name and inputs
import pickle
UserName= str(input("Please enter your name: "))
try:
    x = float(input("Input your 1st number:"))
except Exception as e1:
    print(e1)
    print("Error belongs to the following class: ", e1.__class__)
    exit()

# Step 2: Gather second number from user
try:
    y = float(input("Input your 2nd number:"))
except Exception as e2:
    print(e2)
    print("Error belongs to the following class: ", e2.__class__)
    exit()

# Step 3: Calculate results of adding, subtracting, multiplying and dividing the 2 numbers
Sum = x + y
Difference = x - y
Product = x * y
try:
    Division = x / y
except Exception as e3:
    print(e3)
    print("Error belongs to the following class: ", e3.__class__)

# Step 4: Display results of adding, subtracting, multiplying and dividing the 2 numbers
print("\n The sum of the two numbers is", Sum)
print("\n Subtracting the second number from the first gives us", Difference)
print("\n The product of the two numbers is", Product)
print("\n Dividing the first number by the second number gives us a quotient of", Division)

# Step 5: Save values to file
objfile = open("DataInputs.txt", "ab")
UserChoice=int(input("Enter 1 to save these calculations to file"))
if UserChoice == 1:
    FileDump = [UserName, x, y]
    pickle.dump(FileDump, objfile)
    objfile.close()

objfile = open("DataInputs.txt", "rb")
objFileData = pickle.load(objfile)
print(objFileData)
objfile.close()

input("\n Thanks for using the most primitive calculator in the world! \n \nHit enter to end")