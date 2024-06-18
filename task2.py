class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)
        if found_contacts:
            print("Matching Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, phone, new_contact):
        for contact in self.contacts:
            if contact.name == name and contact.phone == phone:
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name, phone):
        for contact in self.contacts:
            if contact.name == name and contact.phone == phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContacts")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact = Contact(name, phone)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter phone number of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_contact = Contact(new_name, new_phone)
            contact_book.update_contact(name, phone, new_contact)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            phone = input("Enter phone number of the contact to delete: ")
            contact_book.delete_contact(name, phone)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
