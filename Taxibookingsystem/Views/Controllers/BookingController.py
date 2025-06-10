import mysql.connector

def book(booking):
    try:
        dbConnect = mysql.connector.connect(host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command = "INSERT INTO `bookings`(`pickup_address`,`dropoff_address`, `pickup_date`, `pickup_time`, `booking_status`, `customer_id`) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (booking.get_pickup_address(),booking.get_dropoff_address(),booking.get_pickup_date(),booking.get_pickup_time(),booking.get_booking_status(),booking.get_customer_id())
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()

        return True
    except Exception as error:
        print(f"{error}")
        return False

def update(booking):
    try:
        dbConnect = mysql.connector.connect( host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command="UPDATE `bookings` SET `pickup_address`=%s,`dropoff_address`=%s,`pickup_date`=%s,`pickup_time`=%s WHERE booking_id=%s"
        values = (booking.get_pickup_address(),booking.get_dropoff_address(),booking.get_pickup_date(),booking.get_pickup_time(),
                         booking.get_booking_id())
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
        return False

def cancel(booking):
    try:
        dbConnect = mysql.connector.connect( host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command="DELETE FROM `bookings` WHERE booking_id=%s"
        values =(booking.get_booking_id(),)
        cursor.execute(command,values)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
        return False


def complete(ride):
    try:
        dbConnect = mysql.connector.connect(host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command = "UPDATE bookings SET `booking_status`='Completed' WHERE `booking_id`=%s"
        command2 = "UPDATE drivers SET `Status`='Available' WHERE `driver_id`=%s"
        values = (ride.get_booking_id(),)
        values2 = (ride.get_driver_id(),)
        cursor.execute(command,values)
        cursor.execute(command2,values2)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
        return False

def assign(driver):
    try:
        dbConnect = mysql.connector.connect(host="localhost",user="root",password="",database="bibek_taxi_booking")
        cursor = dbConnect.cursor()
        command = "UPDATE bookings SET `driver_id`=%s WHERE `booking_id`=%s"
        command2 = "UPDATE drivers SET `Status`='Booked' WHERE `driver_id`=%s"
        values = (driver.get_driver_id(),driver.get_booking_id())
        values2 = (driver.get_driver_id(),)
        cursor.execute(command,values)
        cursor.execute(command2,values2)
        dbConnect.commit()
        cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
        return False
