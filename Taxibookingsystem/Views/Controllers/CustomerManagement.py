import mysql.connector

def register(customer):
    try:
        dbConnect = mysql.connector.connect(host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command = "INSERT INTO `customer`(`name`, `address`, `email`, `contact`, `payment_method`, `username`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (customer.get_name(), customer.get_address(), customer.get_email(), customer.get_contact(), customer.get_payment_method(), customer.get_username(), customer.get_password())
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()

        return True
    except Exception as error:
        print(f"{error}")
        return False


def login_customer(customer):
    result = None
    try:
        dbConnect = mysql.connector.connect(host="localhost", user="root", password="", database="bibek_taxi_booking")

        cursor = dbConnect.cursor()
        command = "SELECT * FROM customer WHERE `username`=%s and `password`=%s"
        values = (customer.get_username(), customer.get_password())
        cursor.execute(command, values)
        result = cursor.fetchone()
        cursor.close()
        dbConnect.close()

        return result
    except Exception as error:
        print(f"{error}")
        return result

