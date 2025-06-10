import mysql.connector

def driverregister(driver):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command = "INSERT INTO `drivers`(`Name`, `Address`, `Email`, `Contact`, `License_no`, `Username`, `Password`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (driver.get_name(), driver.get_address(), driver.get_email(), driver.get_contact(), driver.get_license_no(), driver.get_username(), driver.get_password())
        cursor.execute(command, values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()

        return True
    except Exception as error:
        print(f"{error}")
        return False



def login_driver(driver):
    result = None
    try:
        dbConnect = mysql.connector.connect(host="localhost", user="root", password="", database="bibek_taxi_booking")

        cursor = dbConnect.cursor()
        command = "SELECT * FROM drivers WHERE `username`=%s and `password`=%s"
        values = (driver.get_username(),driver.get_password())
        cursor.execute(command, values)
        result = cursor.fetchone()
        cursor.close()
        dbConnect.close()

        return result
    except Exception as error:
        print(f"{error}")
        return result


