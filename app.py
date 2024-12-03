from contact_manager import ContactManager

def display_menu():
    print("\n  Contact Book Management System  ")
    print("-----------------------------------")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

def app():
    manager = ContactManager()

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                # Add Contact
                print("\n  Add New Contact  ")
                print("-------------------")
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                address = input("Enter Address: ")

                try:
                    contact = manager.add_contact(name, email, phone, address)
                    print("\nContact Added Successfully!")
                    print(contact)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == '2':
                # View All Contacts
                contacts = manager.view_contacts()
                if not contacts:
                    print("\nNo contacts found.")
                else:
                    print("\n  All Contacts  ")
                    for contact in contacts:
                        print("\n" + str(contact))
                        print("-" * 30)

            elif choice == '3':
                # Search Contact
                query = input("\n Enter Search term: ")
                results = manager.search_contacts(query)

                if not results:
                    print("\nNo contacts found.")
                else:
                    print("\n  Search Results  ")
                    for contact in results:
                        print("\n" + str(contact))
                        print("-" * 30)

            elif choice == '4':
                # Remove Contacts
                phone = input("\nEnter phone number to remove: ")

                if manager.remove_contact(phone):
                    print("\nContact removed successfully!")
                else:
                    print("\nNo contacts found in this phone number")

            elif choice == '5':
                # Exit
                print("\nThank you for using Contact Book Management System")
                break

            else:
                print("\nInvalid choice. Please choose a valid option (1-5).")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()


