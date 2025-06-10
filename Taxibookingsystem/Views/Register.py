from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Controllers.CustomerManagement import register
from Models.CustomerModel import Customer
from Views.LoginWindow import LoginForm


class RegistrationForm():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1166x718')
        self.root.state('zoomed')
        self.root.resizable(0, 0)

        # Background Image
        img = Image.open('../images/o.jpg')
        self.bg_image = ImageTk.PhotoImage(img)

        # Set the dimensions of the image
        img_width, img_height = img.size

        self.canvas = Canvas(root, width=img_width, height=img_height)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)

        #Right Frame
        self.frame = Frame(self.root,width=550,height=600)
        self.frame.place(x=750,y=70)

        #Left Frame
        self.lframe = Frame(self.root, width=550, height=590)
        self.lframe.place(x=200, y=75)

        self.lfrmbg_frame = Image.open('../images/s.jpg')
        photo = ImageTk.PhotoImage(self.lfrmbg_frame)
        self.lfrmbg_panel = Label(self.lframe, image=photo)
        self.lfrmbg_panel.image = photo
        self.lfrmbg_panel.place(x=0,y=0,width=550, height=590)

        self.txt = "Customer Register"
        self.heading = Label(self.frame, text=self.txt, font=('times', 25, 'bold'))
        self.heading.place(x=150, y=30)

        self.F_Name=Label(self.frame, text='Name:', font=('Times New Roman', 16))
        self.F_Name.place(x=20,y=100)

        self.Emal=Label(self.frame, text='Email:', font=('Times New Roman', 16))
        self.Emal.place(x=20,y=150)

        self.Phonen_no=Label(self.frame, text='Contact:', font=('Times New Roman', 16))
        self.Phonen_no.place(x=20,y=200)

        self.address_label=Label(self.frame, text='Address:', font=('Times New Roman', 16))
        self.address_label.place(x=20,y=250)

        self.User_name=Label(self.frame, text='Username:', font=('Times New Roman', 16))
        self.User_name.place(x=20,y=300)

        self.Pass=Label(self.frame, text='Password:', font=('Times New Roman', 16))
        self.Pass.place(x=20,y=350)

        self.PAYMent = Label(self.frame, text='Payment Method:', font=('Times New Roman', 16))
        self.PAYMent.place(x=20, y=400)

        #--------Entry--------------
        #First Name
        self.fname = Entry(self.frame,font=('Times New Roman', 16), textvariable=StringVar())
        self.fname.place(x=200,y=100)

        #Email
        self.eml = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.eml.place(x=200,y=150)

        #Contact
        self.cntct = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.cntct.place(x=200,y=200)

        #Username
        self.address = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.address.place(x=200,y=250)

        #Username
        self.usr = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.usr.place(x=200,y=300)

        #Password
        self.pas = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.pas.place(x=200,y=350)

        # PaymentMethod
        self.payment = Entry(self.frame, font=('Times New Roman', 16), textvariable=StringVar())
        self.payment.place(x=200, y=400)


        # #----------Button--------
        # #Register
        self.Register = Button(self.frame, text='Register', command=self.register_customer, font=('Times New Roman', 16), bg='Green', fg='white')
        self.Register.place(x=200,y=500)

        # #Back
        self.Back = Button(self.frame, text='Back', command=self.back_login, font=('Times New Roman', 16), bg='Green', fg='white')
        self.Back.place(x=300,y=500)

    def back_login(self):
        from LoginWindow import LoginForm
        self.root.destroy()
        new_window = Tk()
        LoginForm(new_window)
        new_window.mainloop()


    def register_customer(self):
        if not all(
                [self.fname.get(), self.eml.get(), self.cntct.get(), self.address.get(), self.usr.get(), self.pas.get(),
                 self.payment.get()]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        Name = self.fname.get()
        Paymentmethod = self.payment.get()
        Address = self.address.get()
        Email = self.eml.get()
        Contact = self.cntct.get()
        Username = self.usr.get()
        Password = self.pas.get()

        if all([Name, Paymentmethod, Address, Email, Contact, Username, Password]):
            # Check if the email contains "@gmail.com"
            if "@gmail.com" not in Email:
                messagebox.showerror("Error", "Email must contain @gmail.com")
                return

            customer = Customer(name=Name, email=Email, address=Address, username=Username, contact=Contact,
                                password=Password, payment_method=Paymentmethod)
            registered = register(customer)
            if registered:
                messagebox.showinfo("Registered", "Customer has been registered")
                # Open the login page
                new_window = Tk()
                LoginForm(new_window)
                self.root.destroy()
            else:
                messagebox.showinfo("Error", "Error")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # ... (rest of your code)


def reg():
    root = Tk()
    reg_form = RegistrationForm(root)
    root.mainloop()

if __name__ == '__main__':
    reg()
