import tkinter

haren = tkinter.Tk()

width, height = haren.winfo_screenwidth(), haren.winfo_screenheight()
bg = tkinter.PhotoImage(file="Coverphoto1.png")

panel1 = tkinter.Label(haren, image=bg)
panel1.pack(side='top', fill='both', expand='yes')

haren.wm_title("Hi Sana")
haren.grid()
yeah=tkinter.Label(haren, text="Developed by Full Mad Haren Sarma")
yeah.pack()
haren.attributes('-fullscreen',True)
#haren.wm_geometry("%dx%d+0+0" % (width, height))
haren.mainloop()
