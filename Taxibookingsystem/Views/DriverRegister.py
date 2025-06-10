from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Controllers.DriverManagement import driverregister
from Models.DriverModel import Driver

class DriverRegistrationForm():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1166x718')
        self.root.state('zoomed')
        self.root.resizable(0, 0)

        # Background Image
        img = Image.open('../images/blue.jpg')
        self.bg_image = ImageTk.PhotoImage(img)

        # Set the dimensions of the image
        img_width, img_height = img.size

        self.canvas = Canvas(root, width=img_width, height=img_height)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)

        # Right frame
        self.frame = Frame(self.root, width=600, height=600)
        self.frame.place(x=750, y=70)

        # Left Frame
        self.lframe = Frame(self.root, width=550, height=590, bg="")
        self.lframe.place(x=200, y=75)

        self.lfrmbg_frame = Image.open('../images/s.jpg')
        photo = ImageTk.PhotoImage(self.lfrmbg_frame)
        self.lfrmbg_panel = Label(self.lframe, image=photo)
        self.lfrmbg_panel.image = photo
        self.lfrmbg_panel.place(x=0, y=0, width=550, height=590)

        self.txt = "Driver Registration"
        self.heading = Label(self.frame, text=self.txt, font=('times', 25, 'bold'))
        self.heading.place(x=100, y=30)

        # Labels
        self.F_Name = Label(self.frame, text='Name:', font=('Times New Roman', 16))
        self.F_Name.place(x=20, y=100)

        self.Emal = Label(self.frame, text='Email:', font=('Times New Roman', 16))
        self.Emal.place(x=20, y=150)

        self.Phonen_no = Label(self.frame, text='Contact:', font=('Times New Roman', 16))
        self.Phonen_no.place(x=20, y=200)

        self.address_label = Label(self.frame, text='Address:', font=('Times New Roman', 16))
        self.address_label.place(x=20, y=250)

        self.User_name = Label(self.frame, text='Username:', font=('Times New Roman', 16))
        self.User_name.place(x=20, y=300)

        self.Pass = Label(self.frame, text='Password:', font=('Times New Roman', 16))
        self.Pass.place(x=20, y=350)

        self.License_no = Label(self.frame, text='License_no:', font=('Times New Roman', 16))
        self.License_no.place(x=20, y=400)

        # Entry widgets
        self.fname = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.fname.place(x=200, y=100)

        self.eml = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.eml.place(x=200, y=150)

        self.cntct = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.cntct.place(x=200, y=200)

        self.address = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.address.place(x=200, y=250)

        self.usr = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.usr.place(x=200, y=300)

        self.pas = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.pas.place(x=200, y=350)

        self.L_no = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.L_no.place(x=200, y=400)

        # Buttons
        self.Register = Button(self.frame, text='Register', command=self.register_driver, font=('Times New Roman', 16),
                               bg='Green', fg='white')
        self.Register.place(x=200, y=500)

        self.Back = Button(self.frame, text='Back', command=self.back_login, font=('Times New Roman', 16),
                           bg='Green', fg='white')
        self.Back.place(x=300, y=500)

    def back_login(self):
        from DriverWindow import DriverLoginForm
        self.root.destroy()
        new_window = Tk()
        DriverLoginForm(new_window)
        new_window.mainloop()



    def register_driver(self):
        # Validate that no fields are left blank
        if not all(
                [self.fname.get(), self.eml.get(), self.cntct.get(), self.address.get(), self.usr.get(), self.pas.get(),
                 self.L_no.get()]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Extract values from the entry widgets
        Name = self.fname.get()
        Address = self.address.get()
        Email = self.eml.get()
        Contact = self.cntct.get()
        Username = self.usr.get()
        Password = self.pas.get()
        License_no = self.L_no.get()


        # Check if all values are non-empty before proceeding with registration
        if all([Name, Address, Email, Contact, Username, Password, License_no]):

            if "@gmail.com" not in Email:
                messagebox.showerror("Error", "Email must contain @gmail.com")
                return

            driver = Driver(name=Name, email=Email, address=Address, contact=Contact, username=Username,password=Password, license_no=License_no)
            registered = driverregister(driver)
            if registered:
                messagebox.showinfo("Registered", "Driver has been registered")
                from LoginWindow import LoginForm
                self.root.destroy()
            else:
                messagebox.showinfo("Error", "Error")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

def drireg():
    root = Tk()
    form= DriverRegistrationForm(root)
    root.mainloop()

if __name__ == '__main__':
    drireg()
