# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:35:01 2023

@author: 109511286
"""

import tkinter as tk

def SetValue():
    # 設定label上顯示的字為var，把label放到第一個frame上面
    tk.Label(f1, textvariable=var, height=3).grid(column=0, row=1)

def Click(num): # 當按下按鈕時，在label上顯示相應的數字或運算符
    current = var.get()
    if current == 'ERROR':
        Clear()
        var.set(num)
    else:
        if current == '0': # 如果之前顯示的是0，可以直接更新為新數字或運算符
            if num in ['x', '/']:
                var.set(current + num)
            else: 
                var.set(num)
        else:
            # 如果之前有數字，新輸入的數字或運算符會被追加在後面
            var.set(current + num)

def Clear(): # 清除label的內容
    var.set('0')

def Calculate():
    expression = var.get()

    try:
        num1 = ""
        num2 = ""
        op = ""
        for char in expression:
            # 判斷輸入的是數字或運算符
            if char.isdigit() or ((char == expression[0] or op != "") and char == '-'): # 讀到負號(不為運算符)或數字
                if op == "": # 且還沒讀到運算符號
                    num1 += char
                else: # 讀到運算符號運算符號後
                    num2 += char
            elif char in ['+', '-', 'x', '/']:
                op = char

        # 執行計算
        num1 = int(num1) # num1 str轉成int
        num2 = int(num2) if num2 else 0 # num2 str轉成int

        if op == '+': # 加法運算
            result = num1 + num2
        elif op == '-': # 減法運算
            result = num1 - num2
        elif op == 'x': # 乘法運算
            result = num1 * num2
        elif op == '/': # 除法運算
            if num2 == 0: # X/0，顯示錯誤訊息
                var.set('ERROR')
                return
            result = num1 // num2
        
        # 將計算結果顯示在標籤上
        var.set(str(result))

    except ValueError:
        # 處理非整數輸入的情況
        var.set('ERROR')

if __name__ == "__main__":
    # 創建主視窗
    window = tk.Tk()
    window.title("Lab4")
    
    # 創建兩個frame用於放置標籤和按鈕
    f1 = tk.Frame(window) # 在上面放label顯示結果
    f2 = tk.Frame(window) # 在下面放button
    f1.pack()
    f2.pack()
    
    # 將最初的顯示數字設定為0
    var = tk.StringVar()
    var.set('0')
    
    SetValue()

    # 按鈕的配置
    buttons = [
        ('7', 0, 2), ('8', 1, 2), ('9', 2, 2), ('x', 3, 2),
        ('4', 0, 3), ('5', 1, 3), ('6', 2, 3), ('-', 3, 3),
        ('1', 0, 4), ('2', 1, 4), ('3', 2, 4), ('+', 3, 4),
        ('0', 0, 5), ('C', 1, 5), ('=', 2, 5), ('/', 3, 5)
    ]

    # 創建按鈕並設置對應的功能
    for (text, x, y) in buttons:
        if text == '=':
            btn = tk.Button(f2, text=text, borderwidth=5, width=6, height=2, command=Calculate)
        elif text == 'C':
            btn = tk.Button(f2, text=text, borderwidth=5, width=6, height=2, command=Clear)
        else:
            btn = tk.Button(f2, text=text, borderwidth=5, width=6, height=2, command=lambda t=text: Click(t))
        btn.grid(column=x, row=y)

    window.mainloop()
