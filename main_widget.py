from Draw import paint
from tkinter import*
from typing import Sized
from segments import *

memory_size = 0 
process_count = 0
segment_count = 0
hole_number = 0

Ram = []
Holes = []
Old_Processes = []

root = Tk() 
root.title("Memory Allocator")
root.geometry("600x300")



def get_memory_size():
    global memory_size
    try:
        memory_size = int(memory_size_entry.get())
        memory_size_entry.config(state='disabled')
        submit_memory_size.config(state='disabled')
        allocate_hole_button.config(state='normal',command=Allocate_Hole)
        add_hole_button.config(state='normal',command=Add_Hole)
        Hole_size_entry.config(state='normal')
        Hole_start_entry.config(state='normal')
        Hole_start_entry.insert(0,"enter hole start")
        Hole_size_entry.insert(0,"enter hole size")
        memory_size_entry_message.set("Memory size is "+str(memory_size))
        
    except ValueError:
        memory_size_entry_message.set("invalid input")


def Add_Hole():
    global hole_number

    Hole_addition_message.set("")
    start = int(Hole_start_entry.get())
    size = int(Hole_size_entry.get())
    name = "Hole"+str(hole_number)
    hole_number = hole_number + 1
    new_hole = segment(name=name,start=start,size=size)
    
    if(hole_addition_validity(Holes=Holes,new_hole=new_hole)):
        Holes.append(new_hole)
    else:
        Hole_addition_message.set("Hole position is invalid, overlapping with other hole")
    Hole_start_entry.delete(0,END)
    Hole_size_entry.delete(0,END)
    
def Allocate_Hole():
    Holes.sort(key=lambda x:x.start)
    start_index = 0
    for hole in Holes:
        old = segment('Old Process',start_index,hole.start - start_index)
        Old_Processes.append(old)
        start_index = hole.end
    
    old = segment("Old Process",start_index,memory_size-start_index)
    Old_Processes.append(old)

    if Old_Processes[0].end == 0:
        del Old_Processes[0]

    for process in Old_Processes:
        Ram.append(process)
    
    for hole in Holes:
        Ram.append(hole)

    Ram.sort(key=lambda x:x.start)

    new_process_button.config(state='normal')
    segment_name_entry.config(state='normal')
    segment_size_entry.config(state='normal')
    add_segment_button.config(state='normal')
    process_number_entry.config(state='normal')
    deallocate_button.config(state='normal')
    draw_button.config(state='normal',command= lambda: paint(Ram))
    Hole_start_entry.config(state='disabled')
    Hole_size_entry.config(state='disabled')
    add_hole_button.config(state='disabled')
    allocate_hole_button.config(state='disabled')
        
    


    

########################### memory size partition ################################
space = Label(root,text="  ").grid(row=0,column=0)
memory_size_entry = Entry(root)
memory_size_entry.insert(0,"enter memory size")
memory_size_entry.grid(row=0,column=2,pady=10)
submit_memory_size = Button(root,text="Submit",command=get_memory_size)
submit_memory_size.grid(row=0,column=4)
memory_size_entry_message = StringVar()
memory_size_entry_message.set("")
label_4 = Label(root,textvariable=memory_size_entry_message).grid(row=1,column=2)
###################################################################################


########################## Hole entry partion #####################################
Hole_start_entry = Entry(root,state='disabled')
Hole_size_entry = Entry(root,state='disabled')
add_hole_button = Button(root,text="Add Hole",state='disabled')
allocate_hole_button = Button(root,text="Allocate_Holes",state='disabled')
Hole_start_entry.grid(row=3,column=1)
Hole_size_entry.grid(row=3,column=3)
add_hole_button.grid(row=3,column=4)
allocate_hole_button.grid(row=5,column=2)
Hole_addition_message = StringVar()
Hole_addition_message.set("")
label_3 = Label(root,textvariable=Hole_addition_message).grid(row=4,column=2)
#################################################################################


########################### process entry partion ###############################
process_label = StringVar()
segment_label = StringVar()
chosen_algorithm = StringVar()
chosen_algorithm.set('First Fit')
label_1 = Label(root,textvariable=process_label).grid(row=7,column=1)
label_1 = Label(root,textvariable=segment_label).grid(row=8,column=1)
process_label.set("Process: "+str(process_count))
segment_label.set("Segment: "+str(segment_count))
new_process_button = Button(root,text="New Process",state='disabled')
segment_name_entry = Entry(root,state='disabled')
segment_size_entry = Entry(root,state='disabled')
Algorithm_menu = OptionMenu(root,chosen_algorithm,'First Fit','Best Fit','Worst fit')
add_segment_button = Button(root,text='Add Segment',state='disabled')
new_process_button.grid(row=7,column=4)
segment_name_entry.grid(row=9,column=1)
segment_size_entry.grid(row=9,column=2)
Algorithm_menu.grid(row=9,column=3)
add_segment_button.grid(row=9,column=4)
##################################################################################


################################### Deallocate process ###########################
label_5 = Label(root,text="Deallocate Process: ").grid(row=11,column=1)
process_number_entry = Entry(root,state='disabled')
deallocate_button = Button(root,text="Deallocate",state='disabled')
process_number_entry.grid(row=12,column=1)
deallocate_button.grid(row=12,column=3)
##################################################################################

################################ Draw ############################################
draw_button = Button(root,text="Draw RAM",state='disabled')
draw_button.grid(row=14,column=2)
##############################################################################




root.mainloop()