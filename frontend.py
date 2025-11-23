from tkinter import *
from tkinter import messagebox
from backend import PasswordManagerBe

class PasswordManagerGUI:
    def __init__(self, master) -> None:
        """Initializing GUI Attribute for master"""
        self.master = master
        self.master.title('Password Manager')
        self.master.configure(padx=50, pady=50)
        self.master.resizable(False, False)
        # self.master.configure(background='#ECECEC')
        self.password_be = PasswordManagerBe()

        #logo
        self.canvas = Canvas(self.master, width=200, height=200)
        self.logo = PhotoImage(file='logo.png')
        self.canvas.create_image(100,100, image= self.logo)
        self.canvas.grid(row=0, column=1)

        #Labels
        self.website_label = Label(self.master, text='Website:').grid(row=1, column=0)
        self.email_label = Label(self.master, text='E-mail:').grid(row=2, column=0)
        self.Password_label = Label(self.master, text='Password:').grid(row=3, column=0)

        #Entries
        self.website_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()

        self.website_entry = Entry(self.master, width=39, textvariable=self.website_var)
        self.website_entry.grid(row=1, column=1, columnspan=3, sticky='nsew')

        self.email_entry = Entry(self.master, width=39, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky='nsew')
        
        self.password_entry = Entry(self.master, width=24, textvariable=self.password_var)
        self.password_entry.grid(row=3, column=1, columnspan=2, sticky='nsew')

        #buttons
        self.generate_button = Button(self.master, text='Generate', command=self.generate_password)
        self.generate_button.grid(row=3, column=3, padx=5)

        self.add_button = Button(self.master, text='Add', command=self.save_data)
        self.add_button.grid(row=4, column=1, sticky='nsew', pady=5)

        self.search_button = Button(self.master, text='Search', command=self.search_password)
        self.search_button.grid(row=4, column=3, sticky='nsew', pady=5)
        
        self.clear_button = Button(self.master, text='Clear', command=self.clear)
        self.clear_button.grid(row=4, column=2, sticky='nsew', padx=5, pady=5)


    def generate_password(self):
        password = self.password_be.generate_password()
        self.password_entry.delete(0,'end')
        self.password_entry.insert(0, password)
    

    def save_data(self):
        if len(self.website_var.get()) == 0 or len(self.email_var.get()) == 0 or len(self.password_var.get()) == 0:
            messagebox.showinfo(title='Warning', message='Please make sure you have not left any field empty!')
        else:
            self.password_be.save_data(self.website_var.get(), self.email_var.get(), self.password_var.get())
            self.clear()
            messagebox.showinfo(title='Success', message='Successfully inserted!')


    def search_password(self):
        result = self.password_be.search_data(self.website_var.get())
        if result is None:
            messagebox.showinfo(title='Warning', message='We could not find password for this website')
        else:
            self.email_entry.delete(0, 'end')
            self.email_entry.insert(0, result[2])
            self.password_entry.delete(0, 'end')
            self.password_entry.insert(0, result[3])


    def clear(self):
        self.website_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')



def main():
    main_window = Tk()
    password_manager = PasswordManagerGUI(main_window)

    main_window.mainloop()