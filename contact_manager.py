from contact import Contact
from validation import Validation
from file_handler import FileHandler

class ContactManager:
    def __init__(self):
        self.contacts = FileHandler.load_contacts()
        self.phone_numbers = set(contact.phone for contact in self.contacts)

    def add_contact(self, name, email, phone, address):
        # Validate inputs
        name = Validation.validate_name(name)
        email = Validation.validate_email(email)
        phone = Validation.validate_phone(phone)
        address = Validation.validate_address(address)

        # Check for duplicate phone number
        if phone in self.phone_numbers:
            raise ValueError("Phone number already exists in contacts.")
        
        # Create and add contact
        new_contact = Contact(name, email, phone, address)
        self.contacts.append(new_contact)
        self.phone_numbers.add(phone)

        # Save to file
        FileHandler.save_contacts(self.contacts)
        return new_contact
    
    def view_contacts(self):
        return self.contacts
    
    def search_contacts(self, query):
        query = query.lower()
        return [
            contact for contact in self.contacts
            if (query in contact.name.lower() or
                query in contact.email.lower() or
                query in contact.phone or
                query in contact.address.lower())
        ]
    
    def remove_contact(self, phone):
        # Validate phone number
        phone = Validation.validate_phone(phone)

        # Find and remove contact
        for contact in self.contacts[:]:
            if contact.phone == phone:
                self.contacts.remove(contact)
                self.phone_numbers.remove(phone)

                # Update file 
                FileHandler.save_contacts(self.contacts)
                return True
            
        return False
    
    