# Task 25: Store Inventory Manager
#
# - Define three subprograms:
#   - `addItem` that takes a list (inventory) and adds a new item with a name and quantity.
#   - `displayInventory` that prints all items in the inventory list.
#   - `saveInventory` that writes the inventory list to a file named "inventory.txt" with each item on a new line.
# - The main program should:
#   - Initialise an empty list for inventory.
#   - Allow the user to add items to the inventory by entering a name and quantity.
#   - Ask if the user wants to view the current inventory and display it if they do.
#   - Ask if the user wants to save the inventory to a file, then call `save_inventory` if confirmed.
# - Output the inventory list to the screen and save it to a file.

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
inventory = []

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

def addItem(inventory, name, quantity):
    """Adds an item with a name and quantity to the inventory list."""
    inventory.append({"name": name, "quantity": quantity})
    print(f"Item '{name}' with quantity {quantity} added to the inventory.")


def displayInventory(inventory):
    """Prints each item and its quantity from the inventory list."""
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Current inventory:")
        for item in inventory:
            print(f"- {item['name']}: {item['quantity']}")


def saveInventory(inventory):
    """Saves each item in the inventory list to a file called 'inventory.txt'."""
    try:
        with open("inventory.txt", "w") as file:
            for item in inventory:
                file.write(f"{item['name']} - {item['quantity']}\n")
        print("Inventory has been saved to 'inventory.txt'.")
    except Exception as e:
        print(f"An error occurred while saving the inventory: {e}")


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Initialise an empty inventory
print("Welcome to the Store Inventory Manager!")
inventory = []

while True:
    # Prompt user for action
    print("\n1. Add an item to the inventory.")
    print("2. View the current inventory.")
    print("3. Save the inventory to a file.")
    print("4. Exit.")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add item to inventory
        name = input("Enter the name of the item: ")
        try:
            quantity = int(input("Enter the quantity of the item: "))
            addItem(inventory, name, quantity)
        except ValueError:
            print("Invalid input. Quantity must be a number.")
    elif choice == "2":
        # View inventory
        displayInventory(inventory)
    elif choice == "3":
        # Save inventory to file
        saveInventory(inventory)
    elif choice == "4":
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
