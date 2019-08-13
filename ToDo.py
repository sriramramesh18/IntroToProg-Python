#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Sriram Ramesh, 08/12, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# listTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strMenu = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "C:\_PythonClass\Todo.txt"
strData = ""
dicRow = {}
listTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

ToDoRead = open(objFileName, "r")
for x in ToDoRead:
    task, priority = x.strip().split(",")   # Extracting string and splitting it based on comma
    dicRow[task.strip()] = priority.strip() # Assigning the key value pair to the dictionary dicRow{}
    listTable.append(x.rstrip('\n'))

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strMenu = str(input("Which option would you like to perform? [1 to 4] - "))
    print()
    print("****************************************************************")
    print()

    # Step 3 -Show the current items in the table
    if (strMenu.strip() == '1'):
        print(listTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strMenu.strip() == '2'):
        newTask = str(input("Please type out the next task here: "))
        newPriority = str(input("Please type out the priority of that task here: "))
        newItem = newTask + "," + newPriority
        listTable.append(newItem)
        print("The ToDo list is \n", listTable)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strMenu == '3'):
        DelDict = {}
        for y in listTable:
            task, priority = y.strip().split(",")
            DelDict[task.strip()] = priority.strip()
        try:
            RemoveType = str(input("Enter name of task that you want to delete"))
            DelDict.pop(RemoveType)
            NewList = []
            for task in DelDict:
                NewItems = task + "," + DelDict[task]
                NewList.append(NewItems)
            listTable=NewList
            print("Your ToDo list now contains",listTable)
        except:
            print("Can only remove a task that exists. Please check entry for accuracy incl. case sensitivity")
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strMenu == '4'):
        ToDoRead = open(objFileName, "w")
        print("ToDo list can be found at", objFileName)
        for Item in listTable:
            ToDoRead.write(Item)
            ToDoRead.write("\n")
        ToDoRead.close()
        continue
    elif (strMenu == '5'):
        break  # and Exit the program