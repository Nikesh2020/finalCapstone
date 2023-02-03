"""
T32 Compulsory Task 1:
------------------
File name: inventory.py
Author: Nikesh Chavda
Student ID: NC22110005394
Notes: fixed value error bug as requested by code-reviewer: -
added some defensive programming to prevent the user from entering incorrect
data for the quantity of a shoe, when editing and adding a new one
Assumptions:
Dependencies:
please install the 'tabulate' module to run this code by entering the following line in the terminal: -
pip install tabulate
"""

# ======== include required libraries ==================================================================================
from tabulate import tabulate


# ======== The beginning of the class ==================================================================================
class Shoe:
    # initialise the attributes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def add_stock(self, additional_quantity):
        self.quantity += additional_quantity

    # returns the cost of the shoe
    def get_cost(self):
        return self.cost

    # returns the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

    # returns the code of the shoe.
    def get_code(self):
        return self.code

    # additional function created to make it easier to use the tabulate module
    def get_obj_list(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]

    # returns a string representation of a class.
    def __str__(self):
        return f"{self.country},{self.code},{self.product}," \
               f"{self.cost},{self.quantity}"


# =============Shoe list===========
# The list will be used to store a list of objects of shoes.
shoe_list = []

headings_list = ['Country', 'Code', 'Product', 'Cost', 'Quantity']


# ==========Functions outside the class==============
# update the text file inventory.txt with the most current information in the list buffer shoe_list
def update_file():
    file = None
    try:
        file = open('inventory.txt', 'w')                                       # open inventory.txt
        file.write("Country,Code,Product,Cost,Quantity\n")                      # write the headings of the file items
        for shoe in shoe_list:
            file.write(shoe.__str__() + '\n')
    except FileNotFoundError as error:                                          # Handle any file errors
        print("The inventory file that you are trying to open does not exist")
        print(error)
    finally:
        if file is not None:
            file.close()


# This function will open the file inventory.txt
# and read the data from this file, then creates a shoes object with this data
# and append this object into the shoes list. One line in this file represents
# data to create one object of shoes. Uses the try-except in this function
# for error handling. Remember to skip the first line using your code.
# This function will override any unsaved program data with data from the file
def read_shoes_data():

    shoe_list.clear()       # clear the shoe list before reading into it otherwise you will have multiple
                            # instances of inventory.txt stored into this list
    file = None
    try:
        file = open('inventory.txt', 'r')  # open inventory.txt

        # Get rid of the first line in the text file both methods below achieve this
        file_list = file.readlines()[1:]        # method 1 using list slicing to recreate file buffer without line 0
        # next(file)                            # method 2 using 'next' python built-in function

        for line in file_list:
            country, code, product, cost, quantity = (line.strip('\n')).split(',')  # get object attributes from file
            shoe = Shoe(country, code, product, int(cost), int(quantity))           # create a shoe object from
            shoe_list.append(shoe)                                                  # attributes and append to list

        print("\nSuccessfully read all items in file.")

    except FileNotFoundError as error:                                              # Handle any file errors
        print("The inventory file that you are trying to open does not exist")
        print(error)
    finally:
        if file is not None:
            file.close()


# This function will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.
def capture_shoes():
    print("Please enter the product details")

    # acquire attributes through user input
    country = input("Please enter the product country: ")
    code = input("Please enter the product code: ")
    product = input("Please enter the product name: ")

    # The following code is important in removing a bug that occurs if the user includes a ',' in their input
    # because a ',' is used as a field, seperator. therefore important to remove these.
    country.replace(',', '')
    code.replace(',', '')
    product.replace(',', '')

    while True:
        cost = input("Please enter the product cost: ")

        if cost.isdigit() and int(cost) >= 0:                                   # checks for +ve and numeric values
            break
        else:
            print("Error: negative number or non-numeric character entered "
                  "please try again")

    while True:
        quantity = input("Please enter the quantity: ")

        if quantity.isdigit() and int(quantity) >= 0:                                   # checks for +ve and numeric values
            break
        else:
            print("Error: negative number or non-numeric character entered "
                  "please try again")

    shoe = Shoe(country, code, product, int(cost), int(quantity))   # create a shoe object from
    shoe_list.append(shoe)                                          # attributes and append to list
    update_file()                                                   # update the file to reflect changes in the program
    print("Product added to File successfully!")


# This function will iterate over the shoes list and
# print the details of the shoes returned from the __str__
# function. Organises data in a table format
# by using Python’s tabulate module.
def view_all():
    shoe_table = []                                     # table buffer for use with the tabulate module

    for shoe in shoe_list:                              # loop through all the shoe objects in the list and
        shoe_table.append((shoe.get_obj_list()))        # and add its attributes to the table buffer

    print("\n")
    print(tabulate(shoe_table, headers=headings_list))  # print tabulate function


# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Asks the user if they
# want to add to this quantity of shoes and then updates it.
# This quantity is updated on the file for this shoe.
# Because the quantity_buffer is derived from shoe_list it is the same size therefore its indexing is
# identical provided that the shoe order is not re-arranged in the list.
def re_stock():
    quantity_buffer = []                                              # list buffer to store quantities

    for index in range(0, len(shoe_list)):                            # loop through list of shoes
        quantity_buffer.append(shoe_list[index].get_quantity())       # store the shoe quantity into the list buffer

    min_quantity = min(quantity_buffer)                               # find the maximum quantity in the list buffer
    index_min_quantity = quantity_buffer.index(min_quantity)          # find the index of the maximum quantity
    shoe_min_quantity = shoe_list[index_min_quantity]                 # use this index to find the shoe with the largest

    # print minimum qty stock
    print(f"\nMinimum quantity stock is: "
          f"{shoe_min_quantity.__str__()}")

    while True:
        option = input("Would you like to add quantity to this stock? [y or n] :")
        if option.lower() == 'y':
            while True:
                quantity = int(input("Please enter how many items you would like to add to this stock: "))
                if quantity >= 0:                                       # check number is non-negative
                    shoe_list[index_min_quantity].add_stock(quantity)   # add stock to the object in the list
                    update_file()                                       # update the text file to reflect these changes
                    print("Stock updated successfully")                 # let user know stock has been adjusted
                    break
                else:
                    print("Invalid input: please enter a positive numerical quantity!")
        elif option.lower() == 'n':
            break
        else:
            print("Error: invalid command please try again!")


# This function will search for a shoe from the list
# using the shoe code and return this object so that it will be printed.
def search_shoe():
    shoe_code = str(input("\nPlease enter shoe-code: "))
    shoe_found = False                              # flag to indicate if shoe was found

    for shoe in shoe_list:                          # loop through all shoes in the list
        if shoe.get_code() == shoe_code:            # if the current shoes code matches the one that the user entered
            searched_shoe = shoe                    # save the shoe object and...
            print(f"Shoe Details for {shoe_code}:")
            print(searched_shoe.__str__())          # ....print the saved shoe object to output console
            shoe_found = True                       # set flag to indicate shoe code was found
    if not shoe_found:                              # if shoe is not found print appropriate message to output console
        print("Searched shoe not found in stock!")


# This function will calculate the total value for each item.
# value = cost * quantity.
# Prints this information on the console for all the shoes.
def value_per_item():
    print("\nValues per Item: ")
    print("────────────────────────────────────────────────────────────────────────────────")
    for shoe in shoe_list:                                                      # for each shoe in the list
        value = shoe.get_cost() * shoe.get_quantity()                           # workout its value
        print(shoe.__str__())
        print("value = " + str(value))                                          # and print it to the output console
        print("────────────────────────────────────────────────────────────────────────────────")


# code to determine the product with the highest quantity and
# print this shoe as being for sale.
def highest_qty():
    quantity_buffer = []                                            # list buffer to store quantities
    for index in range(0, len(shoe_list)):                          # loop through list of shoes
        quantity_buffer.append(shoe_list[index].get_quantity())     # store the shoe quantity into the list buffer

    max_quantity = max(quantity_buffer)                             # find the maximum quantity in the list buffer
    index_max_quantity = quantity_buffer.index(max_quantity)        # find the index of the maximum quantity
    shoe_max_quantity = shoe_list[index_max_quantity]               # use this index to find the shoe with the largest
                                                                    # quantity

    print(f"\nThe following shoe has the largest quantity "
          f"in stock and is on sale:\n"
          f"{shoe_max_quantity.__str__()}")                         # print out the shoe details to output console


# start the program ====================================================================================================
read_shoes_data()  # firstly load all the file data to program variable (RAM)

# ==========Main Menu=============
'''
A menu that executes each function above.
'''
while True:
    menu_option = input("\nInventory.py ver 1.0 \n"
                        "Please select one of the option below and press enter:\n"
                        "0 - Load shoe data from file.\n"
                        "1 - Save shoe data to file.\n"
                        "2 - View all shoes on system.\n"
                        "3 - Search Shoe details by its code.\n"
                        "4 - Print value of each shoe stock to screen.\n"
                        "5 - Print highest quantity shoe stock.\n"
                        "6 - Add shoe to file.\n"
                        "7 - Re-stock lowest quantity shoe stock.\n"
                        "e - Exit program.\n"
                        ": ")

    match menu_option:
        case '0':
            read_shoes_data()
        case '1':
            update_file()
            print("\nShoe data saved to file successfully")
        case '2':
            view_all()
        case '3':
            search_shoe()
        case '4':
            value_per_item()
        case '5':
            highest_qty()
        case '6':
            capture_shoes()
        case '7':
            re_stock()
        case 'e':
            print("Exiting program")
            break
        case _:
            print("Error: invalid option, please try again!")