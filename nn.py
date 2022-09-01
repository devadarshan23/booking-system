from tkinter import *
window=Tk()
txt="Hello hi welcome to chennai city. idhu enga ooru indha ooru kulla namma thaaru marru"
text_widget = Text(window)
text_widget.insert('insert',txt)
text_widget.pack(anchor = "w", padx = 50, pady = 50)
window.mainloop()

