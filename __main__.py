import tkinter

top = tkinter.Tk()

TITLE = "Game Math Calculator"
WIDTH = 600
HEIGHT = 400

top.title(TITLE)
top.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+400+10")

def calculate(event):
    height = float(height_box.get())
    airtime = float(airtime_box.get())
    falltime = airtime / 2
    g = 2 * height / falltime ** 2
    v = g * falltime

    gravity_box.config(state="normal")
    gravity_box.delete(0, tkinter.END)
    gravity_box.insert(0, str(g))
    gravity_box.config(state="disabled")
    
    vel_box.config(state="normal")
    vel_box.delete(0, tkinter.END)
    vel_box.insert(0, str(v))
    vel_box.config(state="disabled")

    
height_label = tkinter.Label(text="Jump Height:")
height_label.place(x=20, y=20)
height_box = tkinter.Entry(width=10, justify="center")
height_box.place(x=110, y=20)
height_box.bind("<Return>", calculate)

airtime_label = tkinter.Label(text="Airtime:")
airtime_label.place(x=20, y=50)
airtime_box = tkinter.Entry(width=10, justify="center")
airtime_box.place(x=110, y=50)
airtime_box.bind("<Return>", calculate)

gravity_label = tkinter.Label(text="Gravity:")
gravity_label.place(x=20, y=80)
gravity_box = tkinter.Entry(width=10, justify="center")
gravity_box.place(x=110, y=80)
gravity_box.config(state="disabled")

vel_label = tkinter.Label(text="Jump Vel:")
vel_label.place(x=20, y=110)
vel_box = tkinter.Entry(width=10, justify="center")
vel_box.place(x=110, y=110)
vel_box.config(state="disabled")


top.mainloop()
