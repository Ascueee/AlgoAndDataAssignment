import array

#initializing arrays for data sorting
startTime = time.time()

idArray = []
priceArray = []
nameArray = []
categoryArray = []


#a method that checks what type the value is and stores in the appropriet array for later use
def storeData(value):
    try:
        idArray.append(int(value))
    except ValueError:
        try:
            priceArray.append(float(value))
        except ValueError:
            if value == "Electronics" or value == "Books" or value == "Clothing" or value == "Home & Kitchen":
                categoryArray.append(value)
            else:
                nameArray.append(value)

#collects user input for menu section of the program
def UserInput():
    theInput = input("Please Select An Option: Insert, Update, Delete, Search, sort(sorts by price lowest to highest), Print(prints the list of items), Quit: ")
    theInput = theInput.lower()
    return theInput

#prints the array by calling the zip function which prints the arrays itteravily in a list type format
def PrintArray(idArr, nameArr, priceArr, categoryArr):
    print("-------------------------------------------------------------------------")
    print(" ")
    for idArr, nameArr,priceArr,categoryArr in zip(idArr,nameArr,priceArr,categoryArr):
        print(f"{idArr}, {nameArr}, {priceArr}, {categoryArr}")
    print(" ")
    print("-------------------------------------------------------------------------")


#This function allows the user to insert a new product to the list
def Insert():
    print("You have Selected Insert!!")
    newId = input("Please input the new products id: ")
    newName = input("Please input the new products name: ")
    newPrice = input("Please input the new products price(make sure to add a decimal): ")
    newCategory = input("Please input the new products category: ")

    #updates the arrays with the new product for printing
    idArray.append(int(newId))
    nameArray.append(newName)
    priceArray.append(float(newPrice))
    categoryArray.append(newCategory)


#This function allows the user to update values inside the arrays
def UpdateProducts():
    print("Input by typing the option into the menu")
    updateInput = input("Would you like to modify: Id, Name, Price, or Category: ")
    updateInput = updateInput.lower()

    #checks what the user the user wants to change
    if updateInput == "id":
        #asks  the user for the value that they want to change
        checkInfo = input("Please input the Id you want to change(ex:57353): ")
        checkInfo = int(checkInfo)
        
        #checks if the value the user wants exsits in the lists
        for i in range(len(idArray)):
            #if it exists inside the array then they are allowed to change the value
            if idArray[i] == checkInfo:
                updateInfo = input("Please input new value: ")
                updateInfo = int(updateInfo)
                idArray[i] = updateInfo
    elif updateInput == "name":
        checkInfo = input("Please input the name you want to change(ex:Camera SBBHC): ")
        checkInfo = checkInfo
        for i in range(len(nameArray)):
            if nameArray[i] == checkInfo:
                updateInfo = input("Please input new value: ")
                nameArray[i] = updateInfo
    elif updateInput == "price":
        checkInfo = input("Please input the price you want to change(ex:546.88): ")
        checkInfo = float(checkInfo)
        for i in range(len(priceArray)):
            if(priceArray[i] == checkInfo):
                updateInfo = input("Please input new value: ")
                updateInfo = float(updateInfo)
                priceArray[i] = updateInfo
    elif updateInput == "category":
        #asks the user to input a previous ID to find the product to change the ID
        findId = input("Please first input the ID of the product to find the item for category switch(ex:57353): ")
        findId = int(findId)
        for i in range(len(idArray)):
            #checks if the ID has been found to update  the category
            if(idArray[i] == findId):
                #lets the user input a new category for the product
                updateInfo = input("Please input new value: ")
                categoryArray[i] = updateInfo


#This function allows the user to delete a product depending on the product ID
def Delete():
    deleteIndex = 0

    #checks for ID as ids are unique instead of name and prices
    whichId = input("Please input the Id of the product you would like do delete(ex:57353): ")
    whichId = int(whichId)

    #chekcs if  the ID exists in the array
    for i in range(len(idArray)):
        #if it does contain the ID then it will update the deleteIndex at the current Id index
        if(idArray[i] == whichId):
            deleteIndex = i
    
    #deletes the values at the index
    del idArray[deleteIndex]
    del nameArray[deleteIndex]
    del priceArray[deleteIndex]
    del categoryArray[deleteIndex]

#This function takes in the price array and sorts based on price(cheapest to highest) as well as updates the values in the other array according to the sort
def InsertionSortPrice(floatArray):
    indexLength = range(1, len(floatArray))
    for i in indexLength:
        #gets value to sort
        valueToSort = floatArray[i]

        #compares valueToSort with the left 
        while floatArray[i-1] > valueToSort and i > 0:
            #swaps the two values
            floatArray[i], floatArray[i-1] = floatArray[i-1], floatArray[i]

            #updates the other arrays to be sorted by Price
            idArray[i], idArray[i-1] = idArray[i-1], idArray[i]
            nameArray[i], nameArray[i-1] = nameArray[i-1], nameArray[i]
            categoryArray[i], categoryArray[i-1] = categoryArray[i-1], categoryArray[i]

            i = i - 1
    
    return floatArray

#this is used to sort only one array instead of all arrays by price
def SingleInsertionSort(arrayToSort):
    indexLength = range(1, len(arrayToSort))
    for i in indexLength:
        #gets value to sort
        valueToSort = arrayToSort[i]

        #compares valueToSort with the left 
        while arrayToSort[i-1] > valueToSort and i > 0:
            #swaps the two values
            arrayToSort[i], arrayToSort[i-1] = arrayToSort[i-1], arrayToSort[i]
            i = i - 1
    
    return arrayToSort

#this function takes in a search filter and then uses binary search to find specific element in the array
def Search():
    print("")
    userInput = input("How would you like to search for the item?? Id, Price: ")
    userInput = userInput.lower()


    if userInput == "id":
        userInput = input("Please input the Id your looking for: ")
        userInput = int(userInput)

        pastIndex = 0

        tempArr = []
        tempArr = idArray

        #searches through the old array linearly to find the past index
        indexLength = range(1, len(idArray))
        for  i in indexLength:
            if idArray[i] == userInput:
                print("found the past index")
                pastIndex = i

        tempArr = SingleInsertionSort(tempArr)
        foundItem = BinarySearch(tempArr, userInput)

        if foundItem != None:
            print("Item found!!!")
            print("Item Id: ")
            print(tempArr[foundItem])
            print("Item Name: ")
            print(nameArray[pastIndex])
            print("Items Price: ")
            print(priceArray[pastIndex])
            print("Item Category")
            print(categoryArray[pastIndex])
        elif foundItem == None:
            print("Could not find the item you're looking for")
    elif userInput == "price":
        userInput = input("Please input the price your looking for: ")
        userInput = float(userInput)

        pastIndex = 0

        tempArr = []
        tempArr = priceArray

        #searches through the old array linearly to find the past index
        indexLength = range(1, len(priceArray))
        for  i in indexLength:
            if priceArray[i] == userInput:
                print("found the past index")
                pastIndex = i

        tempArr = SingleInsertionSort(tempArr)
        foundItem = BinarySearch(tempArr, userInput)

        if foundItem != None:
            print("Item found!!!")
            print("Item Id: ")
            print(idArray[pastIndex])
            print("Item Name: ")
            print(nameArray[pastIndex])
            print("Items Price: ")
            print(tempArr[foundItem])
            print("Item Category")
            print(categoryArray[pastIndex])
        elif foundItem == None:
            print("Could not find the item you're looking for")


#Uses the binary search algorithim to find certain elements in a sorted array
def BinarySearch(searchArr, itemToSearch):
    startSearch = 0
    endOfSearch = len(searchArr) - 1

    while startSearch <= endOfSearch:
        #gets the midpoint of the array
        midOfIndex = startSearch + (endOfSearch- startSearch) // 2
        midVal = searchArr[midOfIndex]

        #compares the midVal
        if midVal == itemToSearch:
            return midOfIndex
        elif itemToSearch < midVal:
            endOfSearch = midOfIndex - 1

        else:
            startSearch = midOfIndex + 1

    print("The item your looking for does not exsist")
    return None        


#the main function of the program
def main():
    inProgram = True

    #opens the file and calls the store data function
    with open("product_data3.txt", "r") as file:
        for x in file:
            lines = [value.strip() for value in x.split(",")]
            for value in lines:
                storeData(value)

    #program while loop
    while(inProgram):
        userInput = UserInput()

        if userInput == "insert":
            Insert()
        elif userInput == "update":
            UpdateProducts()
        elif userInput == "delete":
            Delete()
        elif userInput == "search":
            Search()
        elif userInput == "sort":
            InsertionSortPrice(priceArray)
            print("Process finished --- %s seconds ---" % (time.time() - startTime))
            inProgram = False
        elif userInput == "print":
            PrintArray(idArray,nameArray,priceArray,categoryArray)
        elif userInput == "quit":
            print("closing the program")
            inProgram = False


#The main function for the program
if __name__ == "__main__":
    main()
    