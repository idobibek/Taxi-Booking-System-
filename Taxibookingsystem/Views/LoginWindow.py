from tkinter import *
from PIL import ImageTk, Image
from Controllers.CustomerManagement import login_customer
from Models.CustomerModel import Customer
from tkinter import messagebox
import Global

class LoginForm():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1166x718')
        self.root.state('zoomed')
        self.root.resizable(0, 0) 

        # Background Image
        self.bg_frame = Image.open('../images/j.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # top frame
        self.topframe = Frame(self.root, width=1800, height=40, bg="black")
        self.topframe.place(x=0, y=0)

        self.out = Button(self.topframe, text="Back", command=self.logout, font=('Times New Roman', 16))
        self.out.place(x=0, y=0)

        #Loginin frame
        self.lgn_frame = Frame(self.root,bg='#040405',width=925,height=600)
        self.lgn_frame.place(x=200,y=70)
        

        self.txt  = "WELCOME"
        self.heading = Label(self.lgn_frame,text= self.txt, font=('times',25,'bold'),bg='#040405', fg='white')
        self.heading.place(x=150, y=30 ,width=300, height=30)

        #left side image
        self.side_image = Image.open('../images/Bg.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_lbl= Label(self.lgn_frame, image=photo,bg='#040405')
        self.side_image_lbl.image = photo
        self.side_image_lbl.place(x=15,y=100)

        #SignIn image
        self.signin_image = Image.open('../images/hyy.png')
        photo = ImageTk.PhotoImage(self.signin_image)
        self.signin_image_lbl= Label(self.lgn_frame, image=photo,bg='#040405')
        self.signin_image_lbl.image = photo
        self.signin_image_lbl.place(x=645, y=100)

        self.sign_in_lbl = Label(self.lgn_frame, text='Sign In',bg='#040405', fg='white',font=('times',17,'bold'))
        self.sign_in_lbl.place(x=680,y=200)

        #Username
        self.username_lbl = Label(self.lgn_frame, text='Username',bg='#040405', fg='#4f4e4d',font=('times',13,'bold'))
        self.username_lbl.place(x=570,y=250)

        self.username_entry = Entry(self.lgn_frame,highlightthickness=0, relief=FLAT ,bg='#040405',fg='#6b6a69',font=('times',12,'bold'))
        self.username_entry.place(x=570,y=285,width=270)

        self.username_line = Canvas(self.lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.username_line.place(x=570,y=309 )

        #password
        self.password_lbl = Label(self.lgn_frame, text='Password',bg='#040405', fg='#4f4e4d',font=('times',13,'bold'))
        self.password_lbl.place(x=570,y=330)

        self.password_entry = Entry(self.lgn_frame,highlightthickness=0, relief=FLAT ,bg='#040405',fg='#6b6a69',font=('times',12,'bold'))
        self.password_entry.place(x=570,y=366,width=270)

        self.password_line = Canvas(self.lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.password_line.place(x=570,y=390 )

        # login button
        self.lgn_button = Image.open('../images/btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=570, y=420)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("times", 13, "bold"), width=25, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.loginuser)
        self.login.place(x=20, y=15)

        # Forgot password
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT, activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=650, y=490)

        #Sign Up 
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),  relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=625, y=545)


        self.signup_button_label = Button(self.lgn_frame,text="SignUp" ,command=self.signup,bg='#040405', cursor="hand2",borderwidth=0, activebackground="#040405",fg='#00FFFF',font=("yu gothic ui", 11, "bold underline"))
        self.signup_button_label.place(x=750, y=540, width=75, height=30)

        
         # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='../images/hide.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='../images/show.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=366)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=850, y=366)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=850, y=366)
        self.password_entry.config(show='*')

    def signup(self):
        from Register import RegistrationForm
        self.root.destroy()
        new_window = Tk()
        RegistrationForm(new_window)
        new_window.mainloop()

    def loginuser(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        customer = Customer(username=username,password=password)
        customer_login = login_customer(customer)

        if customer_login is not None:
            Global.customer_information = customer_login
            messagebox.showinfo("Welcome","Login Successfully")
            from BookingDashboard import Dashboard
            self.root.destroy()
            new_window = Tk()
            Dashboard(new_window)
            new_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password. Please try again.")

    def logout(self):
        from FirstDashboard import HomeDashboard
        self.root.destroy()
        new_window = Tk()
        HomeDashboard(new_window)
        new_window.mainloop()
def page():
    root = Tk()
    LoginForm(root)
    root.mainloop()

if __name__ == '__main__':
    page()
