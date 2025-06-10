class Driver:
    def __init__(self, driver_id=0, name=None, address=None, email=None, contact=None, license_no=None, username=None, password=None,status=None
                 ):
        self._driver_id = driver_id
        self._name = name
        self._address = address
        self._email = email
        self._contact = contact
        self._license_no = license_no
        self._username = username
        self._password = password
        self._status = status

    # Getter methods
    def get_driver_id(self):
        return self._driver_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_contact(self):
        return self._contact

    def get_license_no(self):
        return self._license_no

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_status(self):
        return self._status

    # Setter methods
    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_email(self, email):
        self._email = email

    def set_contact(self, contact):
        self._contact = contact

    def set_license_no(self, license_no):
        self._license_no = license_no

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_status(self, status):
        self._password = status

