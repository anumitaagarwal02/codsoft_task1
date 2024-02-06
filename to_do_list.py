import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title('TO DO LIST!')
root.geometry("500x500")

my_font = Font(
    family="Segoe Print",
    size=30,
    weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="systembuttonface",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)
my_list.pack(side=LEFT,fill=BOTH)


# stuff = ["walk the dog", "rule the world","take a nap","studyyyy"]
# for item in stuff:
#     my_list.insert(END,item)

myscrollbar = Scrollbar(my_frame)
myscrollbar.pack(side= RIGHT,fill=BOTH)
my_list.config(yscrollcommand=myscrollbar.set)
myscrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("helvetica",24),width=26)
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")

    my_list.selection_clear(0,END)


def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")

    my_list.selection_clear(0,END)



def delete_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")== "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1



def save_list():
    file_name=filedialog.asksaveasfilename(
        initialdir="C:/gui/data",
        title="save file",
        filetypes=(
            ("dat files", "*.dat"),
            ("all files","*.*"))


    )
    if file_name:
        if file_name.endswith(".dat"):
           pass
        else:
            file_name=f'{file_name}.dat'
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count,"fg")== "#dedede":
                my_list.delete(my_list.index(count))

            else:
                count+=1
        stuff=my_list.get(0,END)

        output_file = open(file_name,'wb')

        pickle.dump(stuff,output_file)

def open_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/gui/data",
        title="open file",
        filetypes=(
            ("dat files", "*.dat"),
            ("all files","*.*"))

        )
    if file_name:
        my_list.delete(0,END)
        input_file=open(file_name,'rb')

        stuff=pickle.load(input_file)

        for item in stuff:
            my_list.insert(END,item)







def clear_list():
    my_list.delete(0,END)

my_menu =Menu(root)
root.config(menu=my_menu)

file_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="save list",command=save_list)
file_menu.add_command(label="open list",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="clear list",command=clear_list)

delete_button = Button(button_frame,text="DELETE ITEM", command=delete_item)
add_button = Button(button_frame,text="ADD ITEM", command=add_item)
cross_button = Button(button_frame,text="CROSS ITEM", command=cross_item)
uncross_button = Button(button_frame,text="UNCROSS ITEM", command=uncross_item)
delete_crossed_button = Button(button_frame,text="DELETE CROSSED", command=delete_crossed_item)




delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20)
delete_crossed_button.grid(row=0,column=4)

root.mainloop()
