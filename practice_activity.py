from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)



label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title = " Open Text File", filetype=(("text File", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file) 
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragraph=text_file.read()
    mytext.insert(END,paragraph)
    text_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt","w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update","Success")
    
def closeWindow():
    root.destroy()

open_button=Button(root,command=openFile,text= "open")
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root,text="Save", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)

exit_button=Button(root,text="Close", command=closeWindow)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)

root.mainloop()