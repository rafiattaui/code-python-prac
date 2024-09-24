# Variables and import
choice = 0
groceries = []
from time import sleep
from regex import match

# Print welcome messages
print("Welcome to the grocery list manager!")
print("------------------------------------")

# Do choices
while choice != 5:
    
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Reset")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
             newitem = input("Enter the item: ")
             if match(r"^[a-zA-Z0-9]+$", newitem ):
                groceries.append(newitem)
                print(groceries)
                sleep(1.5)
             else: print("Invalid input, must be a string") ; sleep(1.5)
             
        case 2: print(groceries); sleep(1.5)
        
        case 3:
            if len(groceries) == 0:
                print("No items in list")
            else:
                print(groceries) 
                delitem = input("Enter the item to be removed: ")
                if delitem in groceries:
                    groceries.remove(delitem)
                    print(groceries)
                else: print("Item not in grocery list!")

        case 4: groceries = [] ; print("List reset!"); sleep(1.5)
        case 5: break

print("Bye!")
