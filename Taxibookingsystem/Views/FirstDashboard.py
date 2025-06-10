from tkinter import *
from PIL import ImageTk, Image


class HomeDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry('1300x700')

        # Create a menu
        self.menu = Menu(root)
        root.config(menu=self.menu)

        # Add options to the menu
        self.login_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Login", menu=self.login_menu)
        self.login_menu.add_command(label="Customer", command=self.customer_login)
        self.login_menu.add_command(label="Driver", command=self.driver_login)
        self.login_menu.add_command(label="Admin", command=self.admin_login)
        self.menu.add_command(label="Exit", command=root.destroy)

        # Another frame at the top with a dark background
        self.top_frame = Frame(root, bg="darkblue", padx=10, pady=5)
        self.top_frame.place(x=0, y=0, width=1400, height=50)

        # Label in the top frame
        bibek=Label(self.top_frame, text="Welcome to Taxi Booking System", font=("Helvetica", 16, "bold"), fg="white", bg="darkblue")
        bibek.place(x=0,y=0)

        # Frame for entries and labels (Main Content)
        self.main_frame = Frame(root)
        self.main_frame.place(x=0, y=50, relwidth=1, relheight=1)

        # Frame for the background image
        self.photo_frame = Frame(root)
        self.photo_frame.place(x=0, y=0)

        # Add an image to the background
        self.bg_frame = Image.open('../images/tt.jpg')  # Replace with the path to your image
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.main_frame, image=photo)
        self.bg_panel.photo = photo  # Keep a reference to avoid garbage collection
        self.bg_panel.place(x=0,y=0)

    def customer_login(self):
        from LoginWindow import LoginForm
        self.root.destroy()
        new_window = Tk()
        LoginForm(new_window)
        new_window.mainloop()

    def driver_login(self):
        from DriverWindow import DriverLoginForm
        self.root.destroy()
        new_window = Tk()
        DriverLoginForm(new_window)
        new_window.mainloop()

    def admin_login(self):
        from AdminLogin import AdminLoginForm
        self.root.destroy()
        new_window = Tk()
        AdminLoginForm(new_window)
        new_window.mainloop()

if __name__ == "__main__":
    root = Tk()
    HomeDashboard(root)
    root.mainloop()
