from  tkinter import *
from Draw import paint
from segments import *

Holes = []
Holes_count = 0
memory_size = 0


root = Tk()
root.geometry("700x700")
root.title('memeory segmentation')

label1 = Label(root,text="enter memory size")
label1.grid(row=0,column=0)
memory_size_entry = Entry(root)
memory_size_entry.grid(row=0,column=1,pady=5)

submit_memory_size = Button(root,text='submit', command= lambda : get_memory_size(memory_size_entry))
submit_memory_size.grid(row=0,column=2)






def get_memory_size(memory_size_entry):
    memory_size =int(memory_size_entry.get()) 
    
    
    add_holes = Button(root,text="Add Hole",command = get_holes,pady=10)
    add_holes.grid(row=5, column=0)
    



def get_holes():
    

    label1 = Label(root,text="enter hole start:")
    label1.grid(row=5,column=1)
    hole_start_entry = Entry(root)
    hole_start_entry.grid(row=5,column=2)

    label1 = Label(root,text="enter hole size:")
    label1.grid(row=5,column=3)
    hole_size_entry = Entry(root)
    hole_size_entry.grid(row=5,column=4)

    submit_hole = Button(root,text="Submit Hole",command= lambda : submit_holes(hole_start_entry,hole_size_entry))
    submit_hole.grid(row=5,column=5)
    Add_process = Button(root,text="Add_process",pady=10,command=get_processes)
    Add_process.grid(row=9,column=0)


    

def submit_holes(hole_start_entry,hole_size_entry):
    global Holes_count
     
    start = int(hole_start_entry.get())
    size = int(hole_size_entry.get())

    hole_name = "Hole"+str(Holes_count)

    Holes_count = Holes_count +1

    new_hole = segment(name=hole_name,start=start,size=size)

    Holes.append(new_hole)

    
    

def get_processes():
    label1 = Label(root,text="Enter number of segments")
    label1.grid(row=9,column=1)
    segments_number_entry = Entry(root)
    segments_number_entry.grid(row=9,column=2)

    submit_segments_number = Button(root,text='submit')
    submit_segments_number.grid(row=9,column=3)


def get_segments():
    print('')















root.mainloop()