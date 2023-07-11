from PIL import Image
from tkinter import Tk, Button, Frame, Label, END, Listbox, Scrollbar
from tkinter import filedialog
from random import randint




window = Tk()
window.title("NFT Art Generator")
window.geometry('640x800')
window.resizable(width = 0, height = 0)


body_frame = Frame(window)
body_frame.pack()
body_list_frame = Frame(window)
body_list_frame.pack(fill="both")


hat_frame = Frame(window)
hat_frame.pack()
hat_list_frame = Frame(window)
hat_list_frame.pack(fill="both")


eye_frame = Frame(window)
eye_frame.pack()
eye_list_frame = Frame(window)
eye_list_frame.pack(fill="both")

shirt_frame = Frame(window)
shirt_frame.pack()
shirt_list_frame = Frame(window)
shirt_list_frame.pack(fill="both")


final_frame = Frame(window)
final_frame.pack()
final_list_frame = Frame(window)
final_list_frame.pack(fill="both")

start_frame = Frame(window)
start_frame.pack()

def body_add_file():
    files = filedialog.askopenfilenames(title= "Select Images files", filetypes=(("png files", "*.png"),("all files","*.*" )), initialdir="C:/")
    for file in files:
        body_list_file.insert(END,file)

def body_del_file():
    for i in reversed(body_list_file.curselection()):
        body_list_file.delete(i)




def hat_add_file():
    files = filedialog.askopenfilenames(title= "Select Images files", filetypes=(("png files", "*.png"),("all files","*.*" )), initialdir="C:/")
    for file in files:
        hat_list_file.insert(END,file)

def hat_del_file():
    for i in reversed(hat_list_file.curselection()):
        hat_list_file.delete(i)

def eye_add_file():
    files = filedialog.askopenfilenames(title= "Select Images files", filetypes=(("png files", "*.png"),("all files","*.*" )), initialdir="C:/")
    for file in files:
        eye_list_file.insert(END,file)

def eye_del_file():
    for i in reversed(eye_list_file.curselection()):
        eye_list_file.delete(i)


def shirt_add_file():
    files = filedialog.askopenfilenames(title= "Select Images files", filetypes=(("png files", "*.png"),("all files","*.*" )), initialdir="C:/")
    for file in files:
        shirt_list_file.insert(END,file)

def shirt_del_file():
    for i in reversed(shirt_list_file.curselection()):
        shirt_list_file.delete(i)


#get folder where we save the files
def find_final_destination():
    folder = filedialog.askdirectory()
    if folder is None:
        return
    final_list_file.delete(0,END)
    final_list_file.insert(0,folder)




def random_selector(list):
    rand = randint(0,(len(list)-1)) #creates random number within the index of the list 
    random_item = list[rand]
    random_image = Image.open(random_item)
    return random_image


def start():


    body_images = []
    hat_images = []
    eye_images = []
    shirt_images = []
    destination_list = []

    for a in body_list_file.get(0,END):
        body_images.append(a)        
    for a in hat_list_file.get(0,END):
        hat_images.append(a)
    for a in eye_list_file.get(0,END):
        eye_images.append(a)
    for a in shirt_list_file.get(0,END):
        shirt_images.append(a)
    for a in final_list_file.get(0,END):
        destination_list.append(a)

    body_final = Image.open(body_images[0])
    destination_final = destination_list[0]

    #creat new image
    for i in range(0,10):#input_amount
        new_image = body_final.copy()

        new_hat = random_selector(hat_images)
        new_eye_accessory = random_selector(eye_images)
        new_shirt = random_selector(shirt_images)

        new_image.paste(new_hat, (0, 0),new_hat)
        new_image.paste(new_eye_accessory, (0, 0),new_eye_accessory)
        new_image.paste(new_shirt, (0, 0),new_shirt)

        #new_image.show()
        
        letter = str(i+1)

        destination = destination_final +"/"+ letter + ".png"

        new_image.save(destination,"PNG")



 #Image.open(a)











button21 =  Button(body_frame, text = "Add Images", height = 1, bg = "white", font = ("Arial", 10), command = body_add_file)
button21.grid(row=1, column=0,padx=10,pady=10)

label1 = Label(body_frame, text="Default Body", font=('Arial',20))
label1.grid(row=1,column=1,padx=10,pady=10)

button23 =  Button(body_frame, text = "Clear List", height = 1, bg = "red", font = ("Arial", 10), command = body_del_file)
button23.grid(row=1, column=3,padx=10,pady=10)


body_list_file = Listbox(body_list_frame, selectmode = "extended", height = 1)
body_list_file.pack(side="left", fill = "both", expand = True)




#hat


button21 =  Button(hat_frame, text = "Add Images", height = 1, bg = "white", font = ("Arial", 10),command=hat_add_file)
button21.grid(row=2, column=0,padx=10,pady=10)


label2 = Label(hat_frame, text="Hat", font=('Arial',20))
label2.grid(row=2,column=1,padx=10,pady=10)


button23 =  Button(hat_frame, text = "Clear List", height = 1, bg = "red", font = ("Arial", 10),command=hat_del_file)
button23.grid(row=2, column=3,padx=10,pady=10)


hat_scrollbar = Scrollbar(hat_list_frame)
hat_scrollbar.pack(side="right", fill="y")

hat_list_file = Listbox(hat_list_frame, selectmode = "extended", height = 5, yscrollcommand=hat_scrollbar.set)
hat_list_file.pack(side="left", fill = "both", expand = True)
hat_scrollbar.config(command=hat_list_file.yview)


#eye


button31 =  Button(eye_frame, text = "Add Images", height = 1, bg = "white", font = ("Arial", 10),command=eye_add_file)
button31.grid(row=3, column=0,padx=10,pady=10)

label3 = Label(eye_frame, text="Eye Accessory", font=('Arial',20))
label3.grid(row=3,column=1,padx=10,pady=10)


button33 =  Button(eye_frame, text = "Clear List", height = 1, bg = "red", font = ("Arial", 10),command=eye_del_file)
button33.grid(row=3, column=3,padx=10,pady=10)

eye_scrollbar = Scrollbar(eye_list_frame)
eye_scrollbar.pack(side="right", fill="y")

eye_list_file = Listbox(eye_list_frame, selectmode = "extended", height = 5, yscrollcommand=eye_scrollbar.set)
eye_list_file.pack(side="left", fill = "both", expand = True)
eye_scrollbar.config(command=eye_list_file.yview)


#shirt


button41 =  Button(shirt_frame, text = "Add Images", height = 1, bg = "white", font = ("Arial", 10),command=shirt_add_file)
button41.grid(row=4, column=0,padx=10,pady=10)

label4 = Label(shirt_frame, text="Shirt", font=('Arial',20))
label4.grid(row=4,column=1,padx=10,pady=10)

button43 =  Button(shirt_frame, text = "Clear List", height = 1, bg = "red", font = ("Arial", 10),command=shirt_del_file)
button43.grid(row=4, column=3,padx=10,pady=10)

shirt_scrollbar = Scrollbar(shirt_list_frame)
shirt_scrollbar.pack(side="right", fill="y")

shirt_list_file = Listbox(shirt_list_frame, selectmode = "extended", height = 5, yscrollcommand=shirt_scrollbar.set)
shirt_list_file.pack(side="left", fill = "both", expand = True)
shirt_scrollbar.config(command=shirt_list_file.yview)


#final link
button51 =  Button(final_frame, text = "Add Location", height = 1, bg = "white", font = ("Arial", 10), command= find_final_destination)
button51.grid(row=5, column=0,padx=10,pady=10)

label52 = Label(final_frame, text="File Destination", font=('Arial',20))
label52.grid(row=5,column=1,padx=10,pady=10)


# button53 =  Button(final_frame, text = "Clear", height = 1, bg = "red", font = ("Arial", 10))
# button53.grid(row=5, column=3,padx=10,pady=10)

final_list_file = Listbox(final_list_frame, selectmode = "extended", height = 1)
final_list_file.pack(side="left", fill = "both", expand = True)


#start button
start_button =  Button(start_frame, text = "!!!START!!!", height = 1, bg = "green", font = ("Arial", 20), command=start)
start_button.grid(row=6, column=2,padx=10,pady=10)




window.mainloop()    # last