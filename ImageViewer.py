
#codemy - image viewer app

from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import os

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r'C:\Users\alexa\Documents\Workspace\Python\Projects - small\Image Viewer\photocameraoutline_80020.ico')



# handles forward button click
def forward(my_label, button_forward, button_back, image_num):
    my_label.grid_forget() # clear the outgoing image
    
    my_label = Label(image=image_list[image_num-1])#image in list is dictated by the parameter passed in, ie the 'image_num+1' or 'image_num-1' below  
    button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, image_num+1))
    button_back = Button(root, text="<", command=lambda: back(my_label, button_forward, button_back, image_num-1))
    
    if image_num == 3:
        button_forward = Button(root, text=">", state=DISABLED)

    
    # re-put the widgets on the screen with every button press / screen update
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # update the status field after button press, showing the current image number in the list
    status = Label(root,text=f"image {image_num} of {len(image_list)}", bd=1, relief="sunken", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



# handles back button click
def back(my_label, button_forward, button_back, image_num):
    my_label.grid_forget() # clear the outgoing image
    
    my_label = Label(image=image_list[image_num-1])#image in list is dictated by the parameter passed in, ie the 'image_num+1' or 'image_num-1' below  
    button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, image_num+1))
    button_back = Button(root, text="<", command=lambda: back(my_label, button_forward, button_back, image_num-1))
    
    if image_num == 1:
        button_back = Button(root, text="<", state=DISABLED)
        
    # re-put the widgets on the screen with every button press / screen update
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # update the status field after button press, showing the current image number in the list
    status = Label(root,text=f"image {image_num} of {len(image_list)}", bd=1, relief="sunken", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)





# declare widgets


# image items
my_pics = Path(r'C:\Users\alexa\Documents\Workspace\Python\Projects - small\Image Viewer\Images')
image_list = []

for k,v in enumerate(os.listdir(my_pics)):
    my_img = ImageTk.PhotoImage(Image.open(Path(my_pics/v))) # use this line (image.open() to use jpg and png with tkinter
    image_list.append(my_img)

my_label = Label(image=image_list[0]) # assign the first image as the initial / default image on the img viewer app



#button items
button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, 2))#lambda to pass something through a button command
button_back = Button(root, text="<", state=DISABLED) # disabled as we are on the first image in the list

#add status bar - showing the current image number in the list
status = Label(root,text=f"image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)



# add widgets to root
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()


