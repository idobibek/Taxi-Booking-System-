from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import mysql.connector
import Global
from BookingDashboard import Dashboard
from Controllers.BookingController import update, cancel
from Models.BookingModel import Booking


class ViewBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry('1350x900')
        self.root.resizable(False, False)

        # Another frame at the top with a dark background
        top_frame = Frame(root)
        top_frame.place(x=0, y=0, relwidth=1)

        # Label in the top frame
        Label(top_frame, text="Welcome to Taxi Booking System", font=("Helvetica", 20, "bold")).grid(row=0, column=0, padx=10, pady=5)

        # Frame for entries and labels (Main Content)
        main_frame = Frame(root)
        main_frame.place(x=0, y=50, relwidth=1, relheight=1)

        # Pickup Address
        Label(main_frame, text="Pickup Address:", font=("Helvetica", 13)).place(x=10, y=10)
        self.pickup_address_entry = Entry(main_frame, font=("Helvetica", 13))
        self.pickup_address_entry.place(x=150, y=10)

        # Drop-off Address
        Label(main_frame, text="Drop-off Address:", font=("Helvetica", 13)).place(x=10, y=50)
        self.dropoff_address_entry = Entry(main_frame, font=("Helvetica", 13))
        self.dropoff_address_entry.place(x=150, y=50)


        # Pickup Date using normal Entry
        Label(main_frame, text="Pickup Date:", font=("Helvetica", 13)).place(x=10, y=90)
        self.pickup_date_entry = Entry(main_frame, font=("Helvetica", 13))
        self.pickup_date_entry.place(x=150, y=90)

        # Pickup Time using normal Entry
        Label(main_frame, text="Pickup Time:", font=("Helvetica", 13)).place(x=10, y=130)
        self.pickup_time_entry = Entry(main_frame, font=("Helvetica", 13))
        self.pickup_time_entry.place(x=150, y=130)

        self.booking_id_field = Entry(main_frame, font=("Helvetica", 13))
        self.booking_id_field.place(x=1500, y=5000,width=100,height=35)

        # Buttons for actions
        Button(main_frame, text="Update", command=self.on_update, width=15, height=2).place(x=10, y=170)
        Button(main_frame, text="Cancel", command=self.on_cancel, width=15, height=2).place(x=160, y=170)
        Button(main_frame, text="Back", command=self.on_back, width=15, height=2).place(x=310, y=170)

        # Treeview to display bookings
        columns = ("Booking ID", "Pickup Address", "Dropoff Address", "Date", "Time", "Status")
        self.tree = Treeview(main_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.place(x=10, y=250)
        self.tree.bind("<<TreeviewSelect>>", self.selectedRow)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bibek_taxi_booking"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM bookings WHERE `customer_id`={Global.customer_information[0]}")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        except Exception as err:
            print(f"{err}")

    def on_update(self):
        pickup_address = self.pickup_address_entry.get()
        dropoff_address = self.dropoff_address_entry.get()
        pickup_date = self.pickup_date_entry.get()
        pickup_time = self.pickup_time_entry.get()
        booking_id = self.booking_id_field.get()
        booking =Booking(pickup_address=pickup_address, dropoff_address=dropoff_address, pickup_time=pickup_time,
                        pickup_date=pickup_date,booking_id=booking_id)
        updated =update(booking)
        if updated:
            messagebox.showinfo("Updated", "Your information is updated ")
            self.root.destroy()
            new_root = Tk()
            ViewBooking(new_root)
            new_root.mainloop()
        else:
            messagebox.showinfo("Error", "Error")

    def on_cancel(self):
        booking_id = self.booking_id_field.get()
        booking = Booking(booking_id)
        updated =cancel(booking)
        if updated:
            messagebox.showinfo("Updated", "Your information is deleted ")
            self.root.destroy()
            new_root = Tk()
            ViewBooking(new_root)
            new_root.mainloop()
        else:
            messagebox.showinfo("Error",  "Unable to cancel the booking in the database.")


    def on_back(self):
        self.root.destroy()
        new_root = Tk()
        Dashboard(new_root)
        new_root.mainloop()

    def selectedRow(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")

        if values:
            self.pickup_address_entry.delete(0, "end")
            self.pickup_address_entry.insert(0, values[1])

            self.dropoff_address_entry.delete(0, "end")
            self.dropoff_address_entry.insert(0, values[2])

            self.pickup_date_entry.delete(0, "end")
            self.pickup_date_entry.insert(0, values[3])

            self.pickup_time_entry.delete(0, "end")
            self.pickup_time_entry.insert(0, values[4])

            self.booking_id_field.delete(0, "end")
            self.booking_id_field.insert(0, values[0])


if __name__ == "__main__":
    root = Tk()
    app = ViewBooking(root)
    root.mainloop()
