from tkinter import *


def update_text_color(enabled):
    if enabled:
        middle_label.config(fg="green")
    else:
        middle_label.config(fg="red")


def start_tkinter():
    global middle_label

    window = Tk()
    window.geometry('600x400')
    window.title('SPARTAN')

    icon = PhotoImage(file='logo.png')
    window.iconphoto(True, icon)

    window.config(background='#333333')

    image = icon.subsample(10, 10)
    label = Label(window,
                  text="SPARTAN",
                  font=("Comic Sans MS", 14),
                  bg="#212121",
                  fg="red",
                  image=image,
                  compound="left")
    label.pack(pady=20, anchor="n")



    middle_label = Label(
        window,
        text="Press F2 to ENABLE/DISABLE ak spray",
        font=("Comic Sans MS", 16, "bold"),
        bg="#333333",
        fg="red"
    )
    middle_label.place(relx=0.5, rely=0.5, anchor=CENTER)





    credits_label = Label(
        window,
        text="CREDITS: catalan",
        font=("Comic Sans MS", 10, "italic"),
        bg="#333333",
        fg="white"
    )
    credits_label.pack(side=BOTTOM, pady=10)


    window.mainloop()
