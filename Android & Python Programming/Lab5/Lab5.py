# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:15:49 2023

@author: 109511286
"""

import tkinter as tk
from tkinter import messagebox
import pickle
from PIL import Image, ImageTk

# 登入按鈕功能
def login():
    # 獲取使用者輸入的帳號和密碼
    username = entry_username.get()
    password = entry_password.get()

    try:
        # 嘗試讀取帳號資料
        with open('accounts.pickle', 'rb') as file:
            accounts = pickle.load(file)
            # 檢查帳號是否存在，並驗證密碼是否正確
            if username in accounts:
                if accounts[username] == password:
                    # 若帳號密碼正確，顯示登入成功訊息
                    messagebox.showinfo("Login", "Login Successful")
                else:
                    # 若密碼錯誤，顯示錯誤訊息
                    messagebox.showerror("Login", "Incorrect Password")
            else:
                # 若帳號不存在，詢問是否要根據輸入建立新帳號
                response = messagebox.askyesno("User does not exist.", "Do you want to create an account by your input?")
                if response:
                    # 直接將新帳號寫入pickle檔
                    accounts[username] = password
                    with open('accounts.pickle', 'wb') as file:
                        pickle.dump(accounts, file)
    except FileNotFoundError:
        # 若找不到檔案，詢問是否建立新帳號
        response = messagebox.askyesno("No accounts found.", "Do you want to create an account by your input?")
        if response:
            # 如果找不到帳號檔案，則建立新的帳號pickle檔
            accounts = {username: password}
            with open('accounts.pickle', 'wb') as file:
                pickle.dump(accounts, file)

def open_signup_window():
    # 開啟註冊視窗
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")
    
    # 註冊按鈕功能
    def signup():
        # 獲取新帳號和密碼，並確認是否一致
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()
        confirm_password = entry_confirm_password.get()

        try:
            try:
                with open('accounts.pickle', 'rb') as file:
                    accounts = pickle.load(file)
            except EOFError:
                accounts = {}
        except FileNotFoundError:
            accounts = {}
 
        # 檢查帳號是否已存在，以及兩次密碼輸入是否一致
        if new_username in accounts:
            # 若帳號已存在，顯示錯誤訊息
            messagebox.showerror("Sign Up", "Username already exists")
        elif new_password != confirm_password:
            # 若密碼不一致，顯示錯誤訊息
            messagebox.showerror("Sign Up", "Passwords do not match")
        else:
            # 將新帳號寫入pickle檔
            accounts[new_username] = new_password
            with open('accounts.pickle', 'wb') as file:
                pickle.dump(accounts, file)
            messagebox.showinfo("Sign Up", "Registration Successful")
            signup_window.destroy()
    
    # 帳號、密碼輸入框及按鈕
    label_new_username = tk.Label(signup_window, text="New Username:")
    label_new_username.grid(column=0, row=0, padx=10, pady=10)
    entry_new_username = tk.Entry(signup_window)
    entry_new_username.grid(column=1, row=0, padx=10, pady=10)

    label_new_password = tk.Label(signup_window, text="New Password:")
    label_new_password.grid(column=0, row=1, padx=10, pady=10)
    entry_new_password = tk.Entry(signup_window, show="*")
    entry_new_password.grid(column=1, row=1, padx=10, pady=10)

    label_confirm_password = tk.Label(signup_window, text="Confirm Password:")
    label_confirm_password.grid(column=0, row=2, padx=10, pady=10)
    entry_confirm_password = tk.Entry(signup_window, show="*")
    entry_confirm_password.grid(column=1, row=2, padx=10, pady=10)

    button_signup = tk.Button(signup_window, text="Sign Up", command=signup)
    button_signup.grid(column=1, row=3, padx=0, pady=10)

if __name__ == "__main__":
    # 創建主視窗
    window = tk.Tk()
    window.title('Lab5')
    window.geometry('400x400')
    
    # 登入介面
    f1 = tk.Frame(window)
    f2 = tk.Frame(window)
    f1.pack()
    f2.pack()
    
    # 載入圖片並顯示在介面上
    image1 = Image.open('image.jpg').resize((400, 225))
    image1 = ImageTk.PhotoImage(image1)
    label_image = tk.Label(f1, image=image1)
    label_image.pack()
    
    # 帳號、密碼輸入框及按鈕
    label_username = tk.Label(f2, text="Username:")
    label_username.grid(column=0, row=0, padx=10, pady=10)
    entry_username = tk.Entry(f2)
    entry_username.grid(column=1, row=0, padx=10, pady=10)
    
    label_password = tk.Label(f2, text="Password:")
    label_password.grid(column=0, row=1, padx=10, pady=10)
    entry_password = tk.Entry(f2, show="*")
    entry_password.grid(column=1, row=1, padx=10, pady=10)
    
    button_login = tk.Button(f2, text="Log In", command=login)
    button_login.grid(column=0, row=2, padx=0, pady=10)
    
    button_signup = tk.Button(f2, text="Sign Up", command=open_signup_window)
    button_signup.grid(column=1, row=2, padx=0, pady=10)
    
    window.mainloop()