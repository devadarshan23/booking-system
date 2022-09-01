import tkinter as tk
from functools import partial 
window=tk.Tk()
def add(n1,n2):
    m1=(n1.get())
    m2=(n2.get())
    print(m1,m2)

number1 = tk.StringVar()  
number2 = tk.StringVar()
entryNum1 = tk.Entry(window, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(window, textvariable=number2).grid(row=2, column=2)

call_result = partial(add,number1, number2)  
  
buttonCal = tk.Button(window, text="Calculate", command=call_result).grid(row=3, column=0)  
  
window.mainloop() 
