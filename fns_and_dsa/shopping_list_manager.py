def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
       
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_to_add = input("What would you like to add to the list?: ").strip().lower()
            shopping_list.append(item_to_add)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove = input("which item would you like to remove from list?: ").strip().lower()
            
            if remove in shopping_list:
                shopping_list.remove(remove)
            else:
                print("Item not found, returning to main menu... ")
            pass
        elif choice == '3':
            # Display the shopping list
            print(f"Shopping list: {shopping_list} returning to main menu... ")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()