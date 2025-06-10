from tkinter import *
from tkinter import ttk
import mysql.connector

class Driverinfo:
    def __init__(self, root):
        self.root = root
        self.root.title("Drivers")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        self.tree = ttk.Treeview(self.root, columns=(
            'Driver Id', 'Name', 'Status'), show='headings')

        self.tree.heading('Driver Id', text='Driver Id')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Status', text='Status')

        self.tree.column('Driver Id', width=100)
        self.tree.column('Name', width=100)
        self.tree.column('Status', width=90)

        self.tree.place(x=0, y=0, height=300, width=300)

        try:
            dbConnect = mysql.connector.connect(host="localhost", user="root", password="", database="bibek_taxi_booking")
            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM drivers")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=(row[0], row[1], row[8]))  # Assuming 'Status' is at index 2

        except Exception as err:
            print(f"{err}")

if __name__ == '__main__':
    root = Tk()
    Driverinfo(root)
    root.mainloop()
