class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Phone: {self.phone_number}, Email: {self.email}"

def load_contacts(contacts):
    contacts = []
    with open('contacts.txt', 'r') as file:
        for line in file:
            first_name, last_name, phone_number, email = line.strip().split(',')
            contact = Contact(first_name, last_name, phone_number, email)
            contacts.append(contact)
    return contacts

def search(contacts, search_name):
    found = False
    print(f"{'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email':<30}")
    print("-" * 75)
    for contact in contacts:
        if contact.first_name == search_name or contact.last_name == search_name:
            print(f"{contact.first_name:<15} {contact.last_name:<15} {contact.phone_number:<15} {contact.email:<30}")
            found = True
    if not found:
        print(f"No contact found with the name {search_name}")

def sort_contacts(contacts):
    if len(contacts) <= 1:
        return contacts
    less_than = []
    greater_than = []
    pivot = contacts[0]
    for contact in contacts[1:]:  # Start from the second element
        if contact.first_name <= pivot.first_name:
            less_than.append(contact)
        else:
            greater_than.append(contact)
    return sort_contacts(less_than) + [pivot] + sort_contacts(greater_than)

def display_contacts(contacts):
    print(f"{'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email':<30}")
    print("-" * 75)
    for contact in contacts:
        print(f"{contact.first_name:<15} {contact.last_name:<15} {contact.phone_number:<15} {contact.email:<30}\n")

def remove_contact(contacts, first_name, last_name):
    found = False
    for contact in contacts:
        if contact.first_name == first_name and contact.last_name == last_name:
            contacts.remove(contact)
            print(f"Contact {first_name} {last_name} has been removed.")
            found = True
            break
    if not found:
        print(f"No contact found with the name {first_name} {last_name}")

def add_contact(contacts, first_name, last_name, phone_number, email):
    found = False  # Initialize the found variable to track if the contact already exists
    
    # Check if a contact with the same first and last name already exists
    for contact in contacts:
        if contact.first_name == first_name and contact.last_name == last_name:
            print(f"Contact {first_name} {last_name} already exists.")
            found = True
            break

    if not found:
        # Create a new contact and add it to the list
        new_contact = Contact(first_name, last_name, phone_number, email)
        contacts.append(new_contact)
        print(f"Contact {first_name} {last_name} has been added.")



# MAIN CODE
# Load contacts from the file
contacts_list = load_contacts('contacts.txt')

print("Welcome to phoneBook\nMenu\n1) Display Contacts\n2) Search Contacts\n3) Remove Contact\n4) Add Contact\n5) Exit\n")
while True:
    option = input("Select Menu Option: ")
    if option == '1':
        sorted_list = sort_contacts(contacts_list)
        display_contacts(sorted_list)
    elif option == '2':
        search_name = input("Enter first or last name to search: ")
        search(contacts_list, search_name)
    elif option == '3':
        first_name = input("Enter the first name of the contact to remove: ")
        last_name = input("Enter the last name of the contact to remove: ")
        remove_contact(contacts_list, first_name, last_name)
    elif option == '4':
        first_name = input("Enter the first name of the contact to add: ")
        last_name = input("Enter the last name of the contact to add: ")
        phone_number = input("Enter the phone number of the contact to add: ")
        email = input("Enter the email of the contact to add: ")   
        add_contact(contacts_list, first_name, last_name, phone_number, email)    
    elif option == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option selected.")
