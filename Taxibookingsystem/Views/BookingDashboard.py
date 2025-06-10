from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from Models.BookingModel import Booking
from Controllers.BookingController import book
from tkinter import messagebox
import Global

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry('1330x800')
        self.root.resizable(False, False)

        Label(root, text="TAXI BOOKING SYSTEM", font=("Helvetica", 30, "bold")).place(x=400, y=10)

        # Creating a top frame for the image background
        self.topframe = Frame(self.root, width=825, height=500, bg="black")
        self.topframe.place(x=490,y=70)

        img = Image.open('../images/ss.jpeg')
        self.bg_image = ImageTk.PhotoImage(img)

        # Set the dimensions of the image
        img_width, img_height = img.size

        self.canvas = Canvas(self.topframe, width=img_width, height=img_height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)

        # Pickup Address
        self.Pckupadd=Label(self.root, text="Pickup Address:",font=("Helvetica", 13,"bold"))
        self.Pckupadd.place(x=10, y=80)

        self.pickup_address_entry = Entry(root, font=("Helvetica", 13))
        self.pickup_address_entry.place(x=170, y=80)

        # Drop-off Address
        self.drpadd=Label(self.root, text="Drop-off Address:",font=("Helvetica", 13,"bold"))
        self.drpadd.place(x=10, y=130)

        self.dropoff_address_entry = Entry(self.root, font=("Helvetica", 13))
        self.dropoff_address_entry.place(x=170, y=130)

        # Pickup Date using Calendar Entry
        self.pckdate=Label(root, text="Pickup Date:",font=("Helvetica", 13,"bold"))
        self.pckdate.place(x=10, y=180)

        self.pickup_date_entry = DateEntry(root, width=15, background='darkblue', foreground='white', borderwidth=2)
        self.pickup_date_entry.place(x=170, y=180)

        # Pickup Time using direct input
        Label(root, text="Pickup Time:",font=("Helvetica", 13,"bold")).place(x=10, y=230)
        self.pickup_time_entry = Entry(root, font=("Helvetica", 13), width=15)
        self.pickup_time_entry.place(x=170, y=230)

        # Request Button
        self.requstbtn=Button(self.root, text="Request Taxi", command=self.request_taxi,font=("Helvetica", 16,"bold"),bg="green")
        self.requstbtn.place(x=10, y=280)

        # View Booking Button
        self.vwbtn=Button(root, text="View Booking", command=self.view_booking,font=("Helvetica", 16,"bold"),bg="yellow")
        self.vwbtn.place(x=200, y=280)

        #Logout Button
        self.logoutbtn =Button(self.root, text="logout", command=self.logout, font=("Helvetica", 16,"bold"),bg="red")
        self.logoutbtn.place(x=10, y=600)

    def request_taxi(self):
        pickup_address = self.pickup_address_entry.get()
        dropoff_address = self.dropoff_address_entry.get()
        pickup_date = self.pickup_date_entry.get_date()
        pickup_time = self.pickup_time_entry.get()
        booking = Booking(pickup_address=pickup_address, dropoff_address=dropoff_address, pickup_time=pickup_time,
                          pickup_date=pickup_date, booking_status ="Pending",customer_id=Global.customer_information[0])
        booked = book(booking)
        if booked:
            messagebox.showinfo("Booked", "Thank you for Booking Our Taxi. Have a safe ride")
        else:
            messagebox.showinfo("Error", "Error")

    def view_booking(self):
        from ViewBooking import ViewBooking
        self.root.destroy()
        new_root = Tk()
        ViewBooking(new_root)
        new_root.mainloop()

    def logout(self):
        from LoginWindow import LoginForm
        messagebox.showinfo("logged out","You are logged out")
        self.root.destroy()
        new_root = Tk()
        LoginForm(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    Dashboard(root)
    root.mainloop()
