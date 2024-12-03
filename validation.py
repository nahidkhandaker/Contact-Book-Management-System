class Validation:
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        return name.strip()
    
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("Email must be a valid email address.")
        return email.strip()
    
    @staticmethod
    def validate_phone(phone):
        try:
            phone_str = str(phone).replace('-','').replace(' ', '')
            if not phone_str.isdigit():
                raise ValueError
            return phone_str
        except ValueError:
            raise ValueError("Phone number must contain only digits.")
        
    @staticmethod
    def validate_address(address):
        if not isinstance(address, str):
            raise ValueError("Address must be a string.")
        return address.strip()
    
    