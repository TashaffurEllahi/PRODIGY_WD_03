import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("\nContact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n----- Contact List -----")
    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name : {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")

# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        contact_num = int(input("\nEnter contact number to edit: ")) - 1

        if 0 <= contact_num < len(contacts):
            contacts[contact_num]["Name"] = input("New Name: ")
            contacts[contact_num]["Phone"] = input("New Phone: ")
            contacts[contact_num]["Email"] = input("New Email: ")

            save_contacts(contacts)
            print("\nContact updated successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        contact_num = int(input("\nEnter contact number to delete: ")) - 1

        if 0 <= contact_num < len(contacts):
            deleted = contacts.pop(contact_num)
            save_contacts(contacts)
            print(f"\n{deleted['Name']} deleted successfully!")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")

# Main Program
def main():
    contacts = load_contacts()

    while True:
        print("\n====== Contact Management System ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()