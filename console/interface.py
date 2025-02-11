from tkinter import *


def update_text_color(enabled, text_widget):
    if text_widget == 1:
        if enabled:
            text_widget1.config(fg="green")
        else:
            text_widget1.config(fg="red")

    elif text_widget == 2:
        if enabled:
            text_widget2.config(fg="green")
        else:
            text_widget2.config(fg="red")

    elif text_widget == 3:
        if enabled:
            text_widget3.config(fg="green")
        else:
            text_widget3.config(fg="red")

    elif text_widget == 4:
        if enabled:
            text_widget4.config(fg="green")
        else:
            text_widget4.config(fg="red")

    else:
        if enabled:
            text_widget5.config(fg="green")
        else:
            text_widget5.config(fg="red")


def start_tkinter():
    global middle_label
    global text_widget1, text_widget2, text_widget3, text_widget4, text_widget5
    window = Tk()
    window.geometry('600x400')
    window.resizable(False, False)
    window.title('SPARTAN')

    #icon = PhotoImage(file='console/logo.png')
#    window.iconphoto(True, icon)

    window.config(background='#333333')

    #image = icon.subsample(10, 10)
    label = Label(window,
                  text="SPARTAN",
                  font=("Comic Sans MS", 14),
                  bg="#212121",
                  fg="red",
                  #image=image,
                  compound="left")
    label.pack(pady=20, anchor="n")



    middle_label = Frame(
        window,
        bg="#333333"
    )
    middle_label.place(relx=0.5, rely=0.55, anchor=CENTER)

    # Primul text (F2 - portocaliu)
    text_widget1 = Text(middle_label, font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="red", bd=0, height=2,
                        width=40)
    text_widget1.insert("insert", "Press ")
    text_widget1.insert("insert", "F2", ("highlight",))  # F2 cu altă culoare
    text_widget1.insert("insert", " to ENABLE/DISABLE ak spray")
    text_widget1.tag_configure("highlight", foreground="orange")
    text_widget1.config(state=DISABLED)
    text_widget1.grid(row=0, column=0, padx=10, pady=2)

    text_widget1.tag_configure("center", justify="center")
    text_widget1.tag_add("center", "1.0", "end")

    # Al doilea text (F3 - portocaliu)
    text_widget2 = Text(middle_label, font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="red", bd=0, height=2,
                        width=40)
    text_widget2.insert("insert", "Press ")
    text_widget2.insert("insert", "F3", ("highlight",))  # F3 cu altă culoare
    text_widget2.insert("insert", " to ENABLE/DISABLE")
    text_widget2.insert("insert", " thompson", ("highlight2",))
    text_widget2.insert("insert", " spray")
    text_widget2.tag_configure("highlight", foreground="orange")
    text_widget2.tag_configure("highlight2", foreground="#6e3700")
    text_widget2.config(state=DISABLED)
    text_widget2.grid(row=1, column=0, padx=10, pady=2)


    text_widget2.tag_configure("center", justify="center")
    text_widget2.tag_add("center", "1.0", "end")


    # Al treilea text (F4 - portocaliu)
    text_widget3 = Text(middle_label, font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="red", bd=0, height=2,
                        width=40)
    text_widget3.insert("insert", "Press ")
    text_widget3.insert("insert", "F4", ("highlight",))  # F4 cu altă culoare
    text_widget3.insert("insert", " to ENABLE/DISABLE")
    text_widget3.insert("insert", " mp5", ("highlight2",))
    text_widget3.insert("insert", " spray")
    text_widget3.tag_configure("highlight", foreground="orange")
    text_widget3.tag_configure("highlight2", foreground="#004e73")
    text_widget3.config(state=DISABLED)
    text_widget3.grid(row=2, column=0, padx=10, pady=2)

    text_widget3.tag_configure("center", justify="center")
    text_widget3.tag_add("center", "1.0", "end")


    # Al patrulea text (F5 - portocaliu)
    text_widget4 = Text(middle_label, font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="red", bd=0, height=2,
                        width=40)
    text_widget4.insert("insert", "Press ")
    text_widget4.insert("insert", "F5", ("highlight",))  # F4 cu altă culoare
    text_widget4.insert("insert", " to ENABLE/DISABLE")
    text_widget4.insert("insert", " lr300", ("highlight2",))
    text_widget4.insert("insert", " spray")
    text_widget4.tag_configure("highlight", foreground="orange")
    text_widget4.tag_configure("highlight2", foreground="cyan")
    text_widget4.config(state=DISABLED)
    text_widget4.grid(row=3, column=0, padx=10, pady=2)

    text_widget4.tag_configure("center", justify="center")
    text_widget4.tag_add("center", "1.0", "end")



# Al patrulea text (F6 - portocaliu)
    text_widget5 = Text(middle_label, font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="red", bd=0, height=2,
                        width=40)
    text_widget5.insert("insert", "Press ")
    text_widget5.insert("insert", "F6", ("highlight",))  # F4 cu altă culoare
    text_widget5.insert("insert", " to ENABLE/DISABLE")
    text_widget5.insert("insert", " SAR", ("highlight2",))
    text_widget5.insert("insert", " spray")
    text_widget5.tag_configure("highlight", foreground="orange")
    text_widget5.tag_configure("highlight2", foreground="#a06522")
    text_widget5.config(state=DISABLED)
    text_widget5.grid(row=4, column=0, padx=10, pady=2)

    text_widget5.tag_configure("center", justify="center")
    text_widget5.tag_add("center", "1.0", "end")





    credits_label = Label(
        window,
        text=" input.sensitivity 0.8333 || input.ads_sensitivity 0.8333 || fov 90",
        font=("Comic Sans MS", 10, "italic"),
        bg="#333333",
        fg="white"
    )
    credits_label.pack(side=BOTTOM, pady=10)


    window.mainloop()
