import mysql

def loginadmin(admin):

    result = None
    try:
        dbConnect = mysql.connector.connect(host="localhost", user="root", password="", database="bibek_taxi_booking")

        cursor = dbConnect.cursor()
        command = "SELECT * FROM admins WHERE `username`=%s and `password`=%s"
        values = (admin.get_username(),admin.get_password())
        cursor.execute(command, values)
        result = cursor.fetchone()
        cursor.close()
        dbConnect.close()
        return result

    except Exception as error:
        print(f"{error}")
        return result