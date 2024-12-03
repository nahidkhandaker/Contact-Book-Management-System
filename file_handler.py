import csv
import os
from contact import Contact

class FileHandler:
    @staticmethod
    def save_contacts(contacts, filename = 'contacts.csv'):
        # Save contacts to a CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Phone', 'Address'])
            for contact in contacts:
                writer.writerow([
                    contact.name,
                    contact.email,
                    contact.phone,
                    contact.address
                ])

    @staticmethod
    def load_contacts(filename = 'contacts.csv'):
        # Load contacts from a CSV file
        contacts = []
        if not os.path.exists(filename):
            return contacts
        
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            for row in reader:
                if len(row) == 4:
                    contacts.append(Contact(*row))
        return contacts
    
