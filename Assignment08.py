#------------------------------------#
# Title: Assignment08.py
# Desc: Product Data Manipulation
# Change Log:
# 8.31.2019: Created script
#------------------------------------#


# Step 1: Create class to gather input and store to list
class ProductStore(object):
    #objFile = None  # File Handle
    strUserInput = None  # A string which holds user input
    LstUserInput= []

    def SaveInput(self):
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while (True):
                strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if (strUserInput.lower() == "exit"):
                    break
                else:
                    ProductStore.LstUserInput.append(strUserInput)
        except Exception as e:
            print("Error: " + str(e))

        print(ProductStore.LstUserInput)
        return(ProductStore.LstUserInput)



# Step 2: Create class to manipulate file
class ProductFileManipulate(object):
    def WriteUserInput(File, Message="Contents of File"):
        for items in ProductStore.LstUserInput:
            File.write(items)
            File.write("\n")

    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
      except Exception as e:
        print("Error: " + str(e))

#I/O
try:
  objFile = open("Products.txt", "r+")
  ProductFileManipulate.ReadAllFileData(objFile, "Here is the current data:")
  ProductStore.SaveInput(object)
  ProductFileManipulate.WriteUserInput(objFile)
  ProductFileManipulate.ReadAllFileData(objFile, "Here is the data that was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):
      objFile.close()