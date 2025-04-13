contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            print(f"Found: Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Name'] = input("Enter new name: ")
            contact['Phone'] = input("Enter new phone number: ")
            contact['Email'] = input("Enter new email: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact List Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()
