import sqlite3
from random import randint, choice, shuffle

class PasswordManagerBe:
    def __init__(self) -> None:
        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS PASSWORDS 
                       (ID INTEGER PRIMARY KEY AUTOINCREMENT, Website TEXT, Email TEXT, Password TEXT)""")

        connection.commit()
        connection.close()

    def save_data(self, website, email, password):
        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO PASSWORDS (Website, Email, Password) 
                            Values (?, ?, ?)""", (website, email, password))

        connection.commit()
        connection.close()

    def search_data(self, website):
        connection = sqlite3.connect('passwords.db')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM PASSWORDS WHERE Website=?""", (website,))
        result = cursor.fetchone()

        connection.commit()
        connection.close()
        return result
    
    def generate_password(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        symbols = "-+=!@#$%^&*"

        letters_list = [choice(letters) for _ in range(1, randint(8, 12))]
        num_list = [choice(nums) for num in range(1, randint(3, 5))]
        symbol_list = [choice(symbols) for symbol in range(1, randint(3, 5))]

        password_list = letters_list + num_list + symbol_list
        shuffle(password_list)
        password = "".join(password_list)
        return password