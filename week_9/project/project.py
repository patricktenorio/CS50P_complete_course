#pip install tk
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox

#pip install Pillow
from PIL import Image, ImageTk

# pip install os-win
import os

#pip install stegano
from stegano import lsb


# TKINTER GUI APP -------------------------------------------------
root = Tk()
root.title(" Message Masker")
root.geometry("700x730+150+180")
root.resizable(False, False)
root.configure(bg="#fff791")


## FUNC SHOW IMAGE ------------------------------------------------
def main():
    global filename
    filename = filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title = 'Select Image File',
        filetype = (("PNG File", "*.png"), ("JPG File", "*.jpg"), ("All File", "*.txt")))

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=585, height=395)
    lbl.image = img
    my_message.delete(1.0, END)


## FUNC SAVE ------------------------------------------------------
def Save():
    global secret
    secret_message = my_message.get(1.0, END)

    try:
        if secret_message == "\n":
            messagebox.showerror("Message box", "No message detected!\nPlease enter a message to continue.")
        else:
            secret = lsb.hide(str(filename), secret_message)
            messagebox.showinfo("Message box", 'Your message was successfuly added!\n\nA new image with "(!)" in it filename was successfuly saved.\nYou can replace the image name anytime.')
            saved_filename = filename.split(".")
            secret.save(f"{saved_filename[0]}(!).png")
            my_message.delete(1.0, END)
    except NameError:
        messagebox.showerror("Message box", "No image detected!\nPlease add an image.")


## FUNC SHOW ------------------------------------------------------
def Show():
    try:
        show_message = lsb.reveal(filename)
        my_message.delete(1.0, END)
        if show_message == None:
            messagebox.showwarning("Message box", "This image has no secret message.")
        else:
            my_message.insert(END, show_message)
            messagebox.showinfo("Message box", 'Secret message reveled!')
    except NameError:
        messagebox.showerror("Message box", "No image detected!\nPlease add an image.")


## FUNC CLEAR -----------------------------------------------------
def Clear():
    my_message.delete(1.0, END)


## ICON -----------------------------------------------------------
image_icon = PhotoImage(file="icons/favicon.png")
root.iconphoto(False, image_icon)


## TITLE ----------------------------------------------------------
Label(root, text="SECRET MESSAGE", bg="#fff791", fg="#21201d", font="unispace 20 bold").place(x=50, y=40)


## IMAGE FRAME ----------------------------------------------------
img_frame = Canvas(root, bd=3, bg="#21201d", width=590, height=400, relief=GROOVE)
img_frame.place(x=50, y=80)

lbl = Label(img_frame, bg="black")
lbl.place(x=5, y=5)


## TEXT BOX -------------------------------------------------------
Label(text="Enter your message below:", bg="#fff791", fg="#21201d", font="unisoft 9").place(x=50, y=530)

text_box = Frame(root, bd=3, width=600, height=100, bg="#f2f2f2", relief=GROOVE)
text_box.place(x=50, y=550)

my_message = Text(text_box, font="Roboto 15", bg="#f2f2f2", fg="black", relief=GROOVE, wrap=WORD)
my_message.place(x=0, y=0, width=580, height=95)

scroll_bar = Scrollbar(text_box)
scroll_bar.place(x=576, y=0, height=93)

scroll_bar.configure(command=my_message.yview)
my_message.configure(yscrollcommand=scroll_bar.set)


## OPEN IMG BUTTON ------------------------------------------------
Button(
    text="Open Image", width=11, height=1, bg="#3cd5ea", font="unispace 8", command=main).place(x=560, y=55)


## HIDE MSG BTN ---------------------------------------------------
Button(
    text="Hide\nMessage", width=9, height=2, bg="#fd678a", font="unispace 8", command=Save).place(x=50, y=655)


## SHOW MSG BTN ---------------------------------------------------
Button(
    text="Show\nMessage", width=9, height=2, bg="#09ffa9", font="unispace 8", command=Show).place(x=130, y=655)


## CLEAR BUTTON ---------------------------------------------------
Button(
    text="Clear\nTextbox", width=9, height=2, bg="#3cd5ea", font="unispace 8", command=Clear).place(x=210, y=655)



if __name__ == "__main__":
    root.mainloop()