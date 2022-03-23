from tkinter import *
from fileshare import mount
from webexchrome import chromework
from main import *
from PIL import ImageTk, Image

root = Tk()  # Creates window to work with
root.title('Mapco Laptop Setup Tool v1.0')  # Names window
root.iconphoto(False, PhotoImage(file='micon.png'))  # Icon for Window
root.geometry('500x400')  # Initial window size

var = StringVar()  # Global declaration to use StringVar()


def resize_image(event):  # Function scales .png background when window is resized
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('mapco.png')  # Opens image file, creates label, fills available space, and runs resize function
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

menubar = Menu(root)  # Creates menu bar
file_menu = Menu(menubar)
command_menu = Menu(menubar)

file_menu.add_command(  # Adds labels in menu bar, and commands when clicked
    label='Exit',
    command=root.destroy,
)
menubar.add_cascade(
    label="File",
    menu=file_menu
)
command_menu.add_command(
    label='Mount File Shares',
    command=mount,
    )
menubar.add_cascade(
    label="Commands",
    menu=command_menu
)
command_menu.add_command(
    label='Chrome/Webex',
    command=chromework,
    )
command_menu.add_command(
    label='Set default apps',
    command=default,
    )

root.config(menu=menubar)  # Initializes menu
root.mainloop()  # Initializes GUI and loops to run it
