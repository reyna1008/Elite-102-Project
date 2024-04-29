# This application will allow users to securely manage their banking activities. Users will authenticate using an account number and PIN and will have access to typical banking functions such as checking balances, making deposits, and withdrawing funds. The project will also encompass functionalities for account management, including the creation, modification, and closure of accounts by users or bank administrators.

from replit import db

import sqlite3

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        account_number TEXT NOT NULL,
        pin TEXT NOT NULL,
        balance REAL DEFAULT 0
    )
''')
conn.commit()


print("Hello, Welcome to the Online Banking System")
user_needs = input("What would you like to do?\n 1. Create Account/Sign in\n 2. Check Balance \n 3. Deposit\n 4. Withdraw \n 5. Delete my account ")

db['123456789' + '1234'] = 'reyna'
if user_needs == "1":
  #----https://www.pythontutorial.net/tkinter/tkinter-entry/----box 
  root = tk.Tk()
  root.geometry("300x150")
  root.resizable(False, False)
  root.title('Sign In/Create Account')

  # store account number and pin in database
  email = tk.StringVar()
  password = tk.StringVar()


  def login_clicked():
      """ callback when the login button clicked
      """
      account_number = email.get()

      msg = f'You entered Pin: {account_number} and password: {password.get()}'

      showinfo(
          title='Information',
          message=msg
      )

  # Sign in frame
  signin = ttk.Frame(root)
  signin.pack(padx=10, pady=10, fill='x', expand=True)

  email_label = ttk.Label(signin, text="Account Number:")
  email_label.pack(fill='x', expand=True)

  email_entry = ttk.Entry(signin, textvariable=email)
  email_entry.pack(fill='x', expand=True)
  email_entry.focus()

  password_label = ttk.Label(signin, text="PIN:")
  password_label.pack(fill='x', expand=True)

  password_entry = ttk.Entry(signin, textvariable=password, show="*")
  password_entry.pack(fill='x', expand=True)

  # login button
  login_button = ttk.Button(signin, text="Login", command=login_clicked)
  login_button.pack(fill='x', expand=True, pady=10)

  root.mainloop()

elif user_needs == "2":
  db[user_needs] = '$0.00'
  print("Your balance is: " + db[user_needs])
elif user_needs == "3":
  deposit = input("How much would you like to deposit?")
  print("Ok, you have made a deposit of $" + deposit + " to " + db['123456789' + '1234'] + "'s account")
elif user_needs == "4":
  withdraw = input("How much would you like to withdraw?")
  print("Ok, you have withdraw $" + withdraw + " from " + db['123456789' + '1234'] + "'s account")
elif user_needs == "5":
  print("Ok your account has been officially deleted, please try again to start a new account.")
else:
  print("Please choose a number from the list.")


#--------------------






