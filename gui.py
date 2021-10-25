from tkinter import *
from zeep import Client


 # TODO : Fix equal Button
 # TODO : Fix button_add methode 
 # TODO : Improve UI
 
 
# ! Using Zeep Module to connect to our wsdl file in localhost
client = Client(wsdl='http://localhost:8000/calculator/?wsdl')


# *This methode will be used to clear the Entry data and initializing the global variables to None
def clear_button():
    first_int = None
    second_int = None
    global_operation == None 
    e.delete(0,"end")


def button_add(number):
    if equal == True:
        e.delete(0,"end")
    e.insert("end",number)



# * this methode will store the first number and delete content of entery so we make space for the second number
def button_operation(operation):
    input1 = e.get()
    num = input1
    if num != "" :
        global global_operation 
        global first_int
        
        first_int = int(num)
        global_operation = operation
        e.delete(0,'end')
    else:
        pass

# * Defining the equal methode : 
# * this methode will use the wsdl file from localhost to make the operation choosed
# ! Check out this repo to acces SOAP Service   : https://github.com/qbdq/Calculator_soap_service_django

def equal_operation():
    input2 = e.get()
    num2  = input2
    
    if num2 != "":
        global second_int
        second_int = int(num2)
        if global_operation=="+":
            result = client.service.sum(first_int,second_int)
        elif global_operation=="-":
            result = client.service.minus(first_int,second_int)
        elif global_operation == "*":
            result = client.service.prod(first_int,second_int)
        elif global_operation =="/":
            result = client.service.div(first_int,second_int)
        
        equal = True
        e.delete(0, 'end')
        e.insert(0,result)
    else:
        e.delete(0,"end")
        e.insert(0,first_int)
    
        



# * Creating our root frame and titling it  
root = Tk()
root.title("Calculator using SOAP Services")

e = Entry(root,width=40, borderwidth=5)
e.grid(row=0 , column = 0, columnspan=4, padx=5, pady=5)

button_1  = Button(root , text = "1" ,padx =40 , pady= 20 , command =lambda :button_add(1))
button_2  = Button(root , text = "2" ,padx =40 , pady= 20 , command =lambda :button_add(2))
button_3  = Button(root , text = "3" ,padx =40 , pady= 20 , command =lambda :button_add(3))
button_4  = Button(root , text = "4" ,padx =40 , pady= 20 , command =lambda :button_add(4))
button_5  = Button(root , text = "5" ,padx =40 , pady= 20 , command =lambda :button_add(5))
button_6  = Button(root , text = "6" ,padx =40 , pady= 20 , command =lambda :button_add(6))
button_7  = Button(root , text = "7" ,padx =40 , pady= 20 , command =lambda :button_add(7))
button_8  = Button(root , text = "8" ,padx =40 , pady= 20 , command =lambda :button_add(8))
button_9  = Button(root , text = "9" ,padx =40 , pady= 20 , command =lambda :button_add(9))
button_0  = Button(root , text = "0" ,padx =40 , pady= 20 , command =lambda :button_add(0))

button_clear = Button(root , text = "CLEAR" ,padx =26 , pady= 20 , command =lambda :clear_button())
button_addition   =  Button(root , text = "+"     ,padx =38 , pady= 20 , command =lambda :button_operation('+'))
button_min  =  Button(root , text = "-"     ,padx =38 , pady= 20 , command =lambda :button_operation('-'))
button_prod =  Button(root , text = "*"     ,padx =38 , pady= 20 , command =lambda :button_operation('*'))
button_div  =  Button(root , text = "/"     ,padx =38 , pady= 20 , command =lambda :button_operation('/'))
button_equal = Button(root , text = "="     ,padx =39 , pady= 20 , command =lambda :equal_operation())
# * Adding buttons to the screen 

button_1.grid   (column =0 , row = 3 )
button_2.grid   (column =1 , row = 3 )
button_3.grid   (column =2 , row = 3 )
button_addition.grid (column =3 , row = 3 )

button_4.grid   (column =0 , row = 2 )
button_5.grid   (column =1 , row = 2 )
button_6.grid   (column =2 , row = 2 )
button_min.grid (column =3 , row = 2 )

button_7.grid   (column =0 , row = 1 )
button_8.grid   (column =1 , row = 1 )
button_9.grid   (column =2 , row = 1 )
button_div.grid (column =3 , row = 1)

button_clear.grid (column =0 , row = 4)
button_0.grid     (column =1 , row = 4)
button_equal.grid (column =2 , row = 4)
button_prod.grid  (column =3 , row = 4)

"""






def clear_fields():
    text_score1.delete(1.0 , 'end')
    text_score2.delete(1.0 , 'end')  
    text_result.delete(1.0 , 'end')


def evaluation(operation) -> None:

    input1 = text_score1.get("1.0","end")
    input2 = text_score2.get("1.0","end")
    
    num1  =int(input1)
    num2 = int(input2)
    text_result.config(state=NORMAL)
    if operation == "/":
        text_result.delete(1.0 , 'end')
        result = client.service.div(num1,num2)
        text_result.insert(1.0 , result)
    elif operation =="+":
        text_result.delete(1.0 , 'end')
        result = client.service.sum(num1,num2)
        text_result.insert(1.0 , result)
    elif operation == "-":
        text_result.delete(1.0 , 'end') 
        result = client.service.minus(num1,num2)
        text_result.insert(1.0, result)
    elif operation == "*":
        text_result.delete(1.0 , 'end') 
        result = client.service.prod(num1,num2)
        text_result.insert(1.0, result)
    else:
        text_result.insert(1.0, "error")

    text_result.config(state=DISABLED)


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
"""

root.mainloop()



