from tkinter import *
from tkinter.ttk import Treeview

import mysql
from PIL import ImageTk, Image

from Controllers.BookingController import assign
from Controllers.DriverManagement import login_driver
from Models.BookingModel import Booking
from Models.DriverModel import Driver
from tkinter import messagebox


class ADashboard():
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.resizable(0, 0)

        self.main_frame = Frame(root, bg="yellow")
        self.main_frame.place(x=0, y=5, height=50, width=1350)


        self.Title = Label(self.main_frame, text="Admin Dashboard", font=("Helvetica", 20, "bold"), bg="yellow")
        self.Title.place(x=10, y=10)

        Label(self.root, text="Pickup Address:", font=("Helvetica", 13,"bold")).place(x=10,y=80)
        self.pickup_address_entry = Entry(self.root, font=("Helvetica", 13))
        self.pickup_address_entry.place(x=150, y=80)

        Label(self.root, text="Dropoff Address:", font=("Helvetica", 13,"bold")).place(x=10, y=120)
        self.dropoff_address_entry = Entry(self.root, font=("Helvetica", 13))
        self.dropoff_address_entry.place(x=150, y=120)

        Label(self.root, text="Pickup Date:", font=("Helvetica", 13,"bold")).place(x=10, y=160)
        self.pickup_date_entry = Entry(self.root, font=("Helvetica", 13))
        self.pickup_date_entry.place(x=150, y=160)

        Label(self.root, text="Pickup Time:", font=("Helvetica", 13,"bold")).place(x=10, y=200)
        self.pickup_time_entry = Entry(self.root, font=("Helvetica", 13))
        self.pickup_time_entry.place(x=150, y=200)


        self.booking_id_field = Entry(self.root, font=("Helvetica", 13))
        self.booking_id_field.place(x=1508, y=2400, width=100, height=35)

        Label(self.root, text="Driver_Id", font=("Helvetica", 13, "bold")).place(x=10, y=240)
        self.driver_id_entry = Entry(self.root, font=("bold", 16), bg="light gray")
        self.driver_id_entry.place(x=150, y=240)

        self.Assign_button = Button(self.root, text="Assign", command=self.assign,font=("Helvetica", 13,"bold"))
        self.Assign_button.place(x=10, y=280)

        self.check_button = Button(self.root, text="Check", command=self.check, font=("Helvetica", 13, "bold"))
        self.check_button.place(x=150, y=280)

        self.logoutbtn = Button(self.root, text="Logout", command=self.logout,font=("Helvetica", 13, "bold"))
        self.logoutbtn.place(x=10, y=600)

        self.tree = Treeview(self.root, columns=(
            'Booking Id', 'Pickup Address', 'Dropoff Address', 'Date', 'Time','Driver_id'),
                                          show='headings')
        self.tree.heading('Booking Id', text='Booking Id')
        self.tree.heading('Pickup Address', text='Pickup Address')
        self.tree.heading('Dropoff Address', text='Dropoff Address')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Driver_id', text='Driver ID')

        self.tree.column('Booking Id', width=80)
        self.tree.column('Pickup Address', width=100)
        self.tree.column('Dropoff Address', width=100)
        self.tree.column('Date', width=80)
        self.tree.column('Time', width=70)
        self.tree.column('Driver_id', width=60)

        self.tree.place(x=400, y=80, width=800, height=500)
        self.tree.bind("<<TreeviewSelect>>", self.selectedRow)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bibek_taxi_booking"
            )
            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM bookings ")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[7]))

        except Exception as err:
            print(f"{err}")

    def selectedRow(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")

        if values:
            self.booking_id_field.delete(0, "end")
            self.booking_id_field.insert(0, values[0])

            self.pickup_address_entry.delete(0, "end")
            self.pickup_address_entry.insert(0, values[1])

            self.dropoff_address_entry.delete(0, "end")
            self.dropoff_address_entry.insert(0, values[2])

            self.pickup_date_entry.delete(0, "end")
            self.pickup_date_entry.insert(0, values[3])

            self.pickup_time_entry.delete(0, "end")
            self.pickup_time_entry.insert(0, values[4])

            self.driver_id_entry.delete(0, "end")
            self.driver_id_entry.insert(0, values[6])

    def assign(self):
        booking_id = self.booking_id_field.get()
        driver_id = self.driver_id_entry.get()

        driver = Booking(booking_id=booking_id, driver_id=driver_id)
        assigned = assign(driver)
        if assigned:
            messagebox.showinfo("Assigned", "Driver has been assigned ")
            self.root.destroy()
            new_root = Tk()
            ADashboard(new_root)
            new_root.mainloop()
        else:
            messagebox.showinfo("Failed", "Failed")

    def check(self):
        from Infodriver import Driverinfo
        new_root=Tk()
        Driverinfo(new_root)
        new_root.mainloop()

    def logout(self):
        from DriverWindow import DriverLoginForm
        messagebox.showinfo("logged out", "You are logged out")
        self.root.destroy()
        new_root = Tk()
        DriverLoginForm(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    ADashboard(root)
    root.mainloop()
