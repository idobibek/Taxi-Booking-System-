class Customer:
    def __init__(self, customer_id=0, name=None, address=None, email=None, contact=None, payment_method=None, username=None, password=None):
        self._customer_id = customer_id
        self._name = name
        self._address = address
        self._email = email
        self._contact = contact
        self._payment_method = payment_method
        self._username = username
        self._password = password

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
