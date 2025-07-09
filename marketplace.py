import csv
import os
import sys
from datetime import datetime

# sets a global variable for the list of categories, add categories with comma and ""
global_category = ["book", "clothing", "gadget", "appliance", "food", "other"]

# sets a timestamp to now(global)




# makes the data type "Item"
class Items:
    def __init__(self, name: str, category, price=0):
        #sets instance variables
        self.name = name
        self.category = category
        self.price = price

    @classmethod
    def input_item(cls):
        name = input("Name: ")
        category = input(f"Category({str(global_category).rstrip("]").lstrip("[").replace("'","")}): ")
        price = float(input("Price: ").rstrip("$"))
        return cls(name, category, price)
    # category error checking
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not category:
            raise ValueError("Please enter a category")
        if category.lower() not in global_category:
            raise ValueError("Invalid Category")
        self._category = category

    # name error checking
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Please enter a name")
        self._name = name
        
    # price error checking
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price must be greater than 0")
        self._price = price


# runs all options with conditionals 
def main():
    while True:
        print("1. Add a product \n"
        "2. Remove a product \n"
        "3. Sort(By Category or Price or Name) \n"
        "4. Find Product Details \n"
        "5. Compare product prices \n"
        "6. Clear CSV file \n"
        "7. Exit")
        answer = input("Choose: ")
        # 1
        if answer.lower() in ["1", "add", "add a product"]:
            add_a_product()

        #2
        if answer.lower() in ["2", "remove", "remove a product"]:
            remove_a_product()

        #3
        if answer.lower() in ["3", "sort", "sort by category", "sort by price"]:
            sort()

        #4 
        if answer.lower() in ["4", "find", "find product details"]:
            find_product_details()

        #5 
        if answer.lower() in ["5", "compare", "compare product prices"]:
            compares_by_price()

        # 6
        if answer.lower() in ["6", "clear", "clear csv file"]:
            clear_file()

        # 7
        if answer.lower() in ["7", "exit", "quit"]:
            exit_the_system()
    
# 1 option, adding a product
def add_a_product():
    while True:
        try:
            item = Items.input_item()
            add_to_csv(item)

        except ValueError as e:
            print(f"Error: {e}")
            continue

        again = input("Would you like to add another object? ")
        if again.lower() not in ["yes", "y", "sure", "ok"]:
            break

# 2 removes a product by name(case insensitive)
def remove_a_product():
    while True: 
        keyname = input("What is the item? ")
        with open("marketplace.csv", newline="") as file:
            reader = list(csv.DictReader(file))
            new_list = [item for item in reader if item["Name"].lower() != keyname.lower()]
            if len(new_list) == len(reader):
                print("Error, No such item")
            else:
                print("Item Removed")
            

        with open("marketplace.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Category", "Price", "Timestamp"])
            writer.writeheader()

            writer.writerows(new_list)
        
        answer = input("Would you like to remove another object? ")
        if answer.lower() not in ["yes", "sure", "ok", "y"]:
            break


# 3 Sorts(By Category or Price or Name)
def sort():
    while True:
        # first asks what to sort by
        sortby = input("Would you like to sort by Category, Price, Name or Timestamp? ").strip()
        if sortby.lower() == "category":
            sort_by_x("Category", str, False)
        
        elif sortby.lower() == "price":
            sort_by_x("Price", float, False)
        
        elif sortby.lower() == "name":
            sort_by_x("Name", str, False)

        elif sortby.lower() == "timestamp":
            sort_by_x("Timestamp",lambda x: datetime.strptime(x, "%Y-%m-%d %I:%M%p") , False)

        else:
            print("Please input a valid sort! ")

        answer = input("Would you like to sort again? ")
        if answer.lower() not in ["y", "yes", "sure", "ok"]:
            return
    


# 4 finds product details
def find_product_details():
    while True:
        name = input("What is the name of the product you want to find? ")
        with open("marketplace.csv") as file:
            reader = list(csv.DictReader(file))
            new_list = [item for item in reader if item["Name"].lower() == name.lower()]
            
            if len(new_list) == 0:
                print("No Item Found, Check spelling?")
                
            else:
                for i in new_list:
                    print(f"Name: {i["Name"]}, Category: {i["Category"]}, Price: {i["Price"]}")

            answer = input("Would You like to find another item? ")
            if answer.lower() not in ["yes", "y", "sure", "ok"]:
                return

# 5 compares product by price
def compares_by_price():
    while True:
        item1 = input("What is the first item you want to compare? ")
        item2 = input("What is the second item you want to compare? ")
        with open("marketplace.csv") as file:
            reader = list(csv.DictReader(file))
            new_list = [item for item in reader if item["Name"].lower() == item1.lower() or item["Name"].lower() == item2.lower()]
            if len(new_list) != 2:
                print("One or more items do not exist...check spelling? ")
            else:
                for i in new_list:
                    if item1.lower() == i["Name"].lower():
                        price1 = float(i["Price"].rstrip("$"))
                    if item2.lower() == i["Name"].lower():
                        price2 = float(i["Price"].rstrip("$"))

                    

                if price1 > price2:
                    print(f"{item1}:{str(price1) + "$"} is greater than {item2}:{str(price2) + "$"}")
                elif price1 < price2:
                    print(f"{item1}:{str(price1) + "$"} is less than {item2}:{str(price2) + "$"}")
                else:
                    print(f"{item1}:{str(price1) + "$"} is equal to {item2}:{str(price2) + "$"}")

        answer = input("Would you like to compare more items? ")
        if answer not in ["y", "yes", "sure", "ok"]:
            return

# 6 just clears the csv file
def clear_file():
    areyousure = input("Are you sure you want to clean the file? ")
    if areyousure not in ["yes", "y", "sure", "ok", "ye"]:
        return
    try:
        with open("marketplace.csv", "w") as file:
            ...
    except:
        print("Error Clearing")
    else:
        print("Successfully cleared")

# 7 exits the system
def exit_the_system():
    sys.exit()

# adds to csv
def add_to_csv(obj):
    timestamp = datetime.now()
    formatted = timestamp.strftime("%Y-%m-%d %I:%M%p")
    
    
    # first checks if item is already added
    with open("marketplace.csv") as file:
        reader = csv.DictReader(file)
        for item in reader:
            if obj.name.lower() == item["Name"].lower():
                print("Sorry, Object already added")
                return 
    
    
    
    filename = "marketplace.csv"
    file_exists = os.path.exists(filename)
    is_empty = not file_exists or os.stat(filename).st_size == 0

    # opens and closes marketplace.csv, adds the dictionary of values
    with open("marketplace.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Category", "Price", "Timestamp"])
        
        # first line is the fieldnames
        if is_empty:
            writer.writeheader()
        
        # writes the key as the fieldnames and the values under like a table
        writer.writerow({
            "Name": obj.name.title().strip(),
            "Category": obj.category.title().strip(),
            "Price": f"{obj.price:.2f}".rstrip("0").rstrip(".") + "$",
            "Timestamp": formatted
        })

# this function sorts by the argument for the parameter sort, datatype(str, int, float), and if its reversed or not
def sort_by_x(sort, datatype=str, reversed=False):
    with open("marketplace.csv") as file:
        reader = list(csv.DictReader(file))
        sorted_version = sorted(reader, key=lambda x: datatype(x[sort].lower().strip().rstrip("$")), reverse=reversed)

    with open("marketplace.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Category", "Price", "Timestamp"])
        writer.writeheader()
        
        for i in sorted_version:
            writer.writerow({

                "Name": i["Name"], 
                "Category": i["Category"],
                "Price": i["Price"],
                "Timestamp": i["Timestamp"]
            })




if __name__ == "__main__":
    main()


