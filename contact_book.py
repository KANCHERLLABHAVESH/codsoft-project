import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                self.display_contact(contact)

    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print("Enter new details (leave blank to keep current value):")
                contact.name = input(f"Name ({contact.name}): ") or contact.name
                contact.phone = input(f"Phone ({contact.phone}): ") or contact.phone
                contact.email = input(f"Email ({contact.email}): ") or contact.email
                contact.address = input(f"Address ({contact.address}): ") or contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_contact(self, contact):
        print(f"\nName: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(Contact(name, phone, email, address))
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone to search: ")
            manager.search_contact(query)
        elif choice == '4':
            query = input("Enter name or phone to update: ")
            manager.update_contact(query)
        elif choice == '5':
            query = input("Enter name or phone to delete: ")
            manager.delete_contact(query)
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
