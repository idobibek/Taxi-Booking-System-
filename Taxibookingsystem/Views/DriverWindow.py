from tkinter import *
from PIL import ImageTk, Image
from Controllers.DriverManagement import login_driver
from Models.DriverModel import Driver
from tkinter import messagebox


class DriverLoginForm():
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.resizable(False, False)

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

        # Loginin frame
        self.drvlgn_frame = Frame(self.root, bg='#040405', width=925, height=600)
        self.drvlgn_frame.place(x=200, y=70)

        self.drvtxt = "WELCOME"
        self.drvheading = Label(self.drvlgn_frame, text=self.drvtxt, font=('times', 25, 'bold'), bg='#040405', fg='white')
        self.drvheading.place(x=150, y=30, width=300, height=30)

        # left side image
        self.drvside_image = Image.open('../images/Bg.png')
        photo = ImageTk.PhotoImage(self.drvside_image)
        self.drvside_image_lbl = Label(self.drvlgn_frame, image=photo, bg='#040405')
        self.drvside_image_lbl.image = photo
        self.drvside_image_lbl.place(x=15, y=100)

        # SignIn image
        self.drvsignin_image = Image.open('../images/hyy.png')
        photo = ImageTk.PhotoImage(self.drvsignin_image)
        self.drvsignin_image_lbl = Label(self.drvlgn_frame, image=photo, bg='#040405')
        self.drvsignin_image_lbl.image = photo
        self.drvsignin_image_lbl.place(x=645, y=100)

        self.drvsign_in_lbl = Label(self.drvlgn_frame, text='Sign In', bg='#040405', fg='white', font=('times', 17, 'bold'))
        self.drvsign_in_lbl.place(x=680, y=200)

        # Username
        self.drvusername_lbl = Label(self.drvlgn_frame, text='Username', bg='#040405', fg='#4f4e4d',
                                  font=('times', 13, 'bold'))
        self.drvusername_lbl.place(x=570, y=250)

        self.drvusername_entry = Entry(self.drvlgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('times', 12, 'bold'))
        self.drvusername_entry.place(x=570, y=285, width=270)

        self.drvusername_line = Canvas(self.drvlgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.drvusername_line.place(x=570, y=309)

        # password
        self.drvpassword_lbl = Label(self.drvlgn_frame, text='Password', bg='#040405', fg='#4f4e4d',
                                  font=('times', 13, 'bold'))
        self.drvpassword_lbl.place(x=570, y=330)

        self.drvpassword_entry = Entry(self.drvlgn_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69',
                                    font=('times', 12, 'bold'))
        self.drvpassword_entry.place(x=570, y=366, width=270)

        self.drvpassword_line = Canvas(self.drvlgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.drvpassword_line.place(x=570, y=390)

        # login button
        self.drvlgn_button = Image.open('../images/btn1.png')
        photo = ImageTk.PhotoImage(self.drvlgn_button)
        self.drvlgn_button_label = Label(self.drvlgn_frame, image=photo, bg='#040405')
        self.drvlgn_button_label.image = photo
        self.drvlgn_button_label.place(x=570, y=420)
        self.drvlogin = Button(self.drvlgn_button_label, text='LOGIN', font=("times", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                            command=self.loginuser)
        self.drvlogin.place(x=20, y=15)

        # Forgot password
        self.drvforgot_button = Button(self.drvlgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.drvforgot_button.place(x=650, y=490)

        # Sign Up
        self.drvsign_label = Label(self.drvlgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"), relief=FLAT,
                                borderwidth=0, background="#040405", fg='white')
        self.drvsign_label.place(x=625, y=545)

        self.drvsignup_button_label = Button(self.drvlgn_frame, text="SignUp", command=self.signup, bg='#040405',
                                          cursor="hand2", borderwidth=0, activebackground="#040405", fg='#00FFFF',
                                          font=("yu gothic ui", 11, "bold underline"))
        self.drvsignup_button_label.place(x=750, y=540, width=75, height=30)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='../images/hide.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='../images/show.png')

        self.drvshow_button = Button(self.drvlgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.drvshow_button.place(x=850, y=366)

    def show(self):
        self.drvhide_button = Button(self.drvlgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.drvhide_button.place(x=850, y=366)
        self.drvpassword_entry.config(show='')

    def hide(self):
        self.drvshow_button = Button(self.drvlgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.drvshow_button.place(x=850, y=366)
        self.drvpassword_entry.config(show='*')

    def signup(self):
        from DriverRegister import DriverRegistrationForm
        self.root.destroy()
        new_window = Tk()
        DriverRegistrationForm(new_window)
        new_window.mainloop()

    def loginuser(self):
        username = self.drvusername_entry.get()
        password = self.drvpassword_entry.get()

        driver = Driver(username=username, password=password)
        driver_login = login_driver(driver)
        if driver_login is not None:
            import Global
            Global.driver_information = driver_login
            messagebox.showinfo("Welcome", "Welcome")
            from DriverDashboard import DriverDashboard
            self.root.destroy()
            new_root = Tk()
            DriverDashboard(new_root)
            new_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password. Please try again.")

    def logout(self):
        from FirstDashboard import HomeDashboard
        self.root.destroy()
        root = Tk()
        HomeDashboard(root)
        root.mainloop()
def page():
    root = Tk()
    DriverLoginForm(root)
    root.mainloop()


if __name__ == '__main__':
    page()
