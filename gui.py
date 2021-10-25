import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import DISABLED, NORMAL
from zeep import Client



client = Client(wsdl='http://localhost:8000/calculator/?wsdl')



def calculate():
    pass 

def clear_fields():
    text_score1.delete(1.0 , 'end')
    text_score2.delete(1.0 , 'end')  
    text_result.delete(1.0 , 'end')


root = tk.Tk()
root.geometry("300x275")
text_score1 = tk.Text(root, height=1 , width=7 )
text_score1.grid(columnspan=1 , row=1 , column=2 ,pady= 10 , padx=5)

text_score2 = tk.Text(root, height=1 , width=7 )
text_score2.grid(columnspan=1 , row=1 , column=3, pady= 10, padx= 5)


btn_1 = tk.Button(root , text="+" ,width=5 , font=("arial",14)  , command=lambda: evaluation("+"))
btn_1.grid(row=2 , column=1 , padx=4)

btn_2 = tk.Button(root , text="-" ,width=5 , font=("arial",14)  , command=lambda: evaluation("-"))
btn_2.grid(row=2 , column=2 , padx=4)

btn_3 = tk.Button(root , text="*" ,width=5 , font=("arial",14)  , command=lambda: evaluation("*"))
btn_3.grid(row=2 , column=3 , padx=4)

btn_3 = tk.Button(root , text="/" ,width=5 , font=("arial",14)  , command=lambda: evaluation("/"))
btn_3.grid(row=2 , column=4 , padx=4)


text_result = tk.Text(root, height=2 , width=16 )
text_result.grid(columnspan=5 , row=3 , column=1, pady= 10, padx= 5)


btn_clear = tk.Button(root , text="C" ,width=5 , font=("arial",14)  , command=lambda :clear_fields())
btn_clear.grid(row=5 , columnspan=10 , pady=6)


root.mainloop()



