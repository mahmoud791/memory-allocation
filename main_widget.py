from Draw import paint
from tkinter import*
from Utilities import *

memory_size = 0 
process_count = 0
segment_count = 0
hole_number = 0
Old_Processes_count = 0

Ram = []
Holes = []
Old_Processes = []



root = Tk() 
root.title("Memory Allocator")
root.geometry("800x500")



def get_memory_size():
    global memory_size
    try:
        memory_size = int(memory_size_entry.get())
        memory_size_entry.config(state='disabled')
        submit_memory_size.config(state='disabled')
        allocate_hole_button.config(state='normal',command=Allocate_Hole,bg='light green')
        add_hole_button.config(state='normal',command=Add_Hole,bg='blue')
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

    try:
        start = int(Hole_start_entry.get())
        size = int(Hole_size_entry.get())
        name = "Hole"
        new_hole = segment(name=name,start=start,size=size)
        
        if(hole_addition_validity(Holes=Holes,new_hole=new_hole,memory_size=memory_size)):
            Holes.append(new_hole)
            Hole_addition_message.set("Hole "+str(hole_number)+" is added succecfully")
            hole_number = hole_number + 1
            Hole_size_entry.delete(0,END)
            Hole_start_entry.delete(0,END)
            Hole_start_entry.insert(0,"enter hole start")
            Hole_size_entry.insert(0,"enter hole size")
        else:
            Hole_addition_message.set("Hole position or size is invalid")
        

        
    
    except ValueError:
         Hole_addition_message.set("invalid input")

    
def Allocate_Hole():
    global Ram,Old_Processes_count
    Holes.sort(key=lambda x:x.start)
    start_index = 0
    for hole in Holes:
        old = segment('Old Process '+str(Old_Processes_count),start_index,hole.start - start_index)
        Old_Processes.append(old)
        Old_Processes_count +=1
        start_index = hole.end
    
    old = segment("Old Process "+str(Old_Processes_count),start_index,memory_size-start_index)
    Old_Processes.append(old)

    

    for process in Old_Processes:
        Ram.append(process)
    
    for hole in Holes:
        Ram.append(hole)

    Ram.sort(key=lambda x:x.start)
    Ram = delete_rubbish(Ram)
    Ram = merge_holes(Ram)

    new_process_button.config(state='normal',bg="light green",command=New_process)
    segment_name_entry.config(state='normal')
    segment_size_entry.config(state='normal')
    process_number_entry.config(state='normal')
    add_segment_button.config(state='normal',bg="blue",command=Add_segments)
    deallocate_button.config(state='normal',bg='red',command=Deallocate_recent_process)
    deallocate_old_button.config(state='normal',bg='orange',command=Deallocate_old_process)
    draw_button.config(state='normal',command= lambda: paint(Ram),bg="yellow")
    Hole_start_entry.config(state='disabled')
    Hole_size_entry.config(state='disabled')
    add_hole_button.config(state='disabled')
    allocate_hole_button.config(state='disabled')
        
    
def Add_segments():
    global process_count,segment_count
    global Ram

    

    segment_name = "P"+str(process_count)+":"+str(segment_name_entry.get())

    try:
        segment_size = int(segment_size_entry.get())
    
    except ValueError:
        segment_entry_message.set("invalid input")
        return


    algorithm = chosen_algorithm.get()
    segment_name_entry.delete(0,END)
    segment_size_entry.delete(0,END)

    new_segment = segment(name=segment_name,start=0,size=segment_size)

    result = Allocate_segment(Ram=Ram,new_segment=new_segment,algorithm=algorithm)
    
    if (result != None):
        Ram = result
        Ram = delete_rubbish(Ram)
        segment_count = segment_count + 1
        segment_label.set("Segment "+str(segment_count)+" of process "+str(process_count)+" :")
        segment_entry_message.set("segment added successfully")
    else:
        segment_entry_message.set('segment '+str(segment_count)+" of process "+str(process_count)+" doesn't fit, process will not be allocated")
        Ram = deallocate_process(process_number=process_count,Ram=Ram)
        segment_count = 0
        segment_label.set("Segment "+str(segment_count)+" of process "+str(process_count)+" :")


def New_process():
    global process_count,segment_count

    process_count +=1
    segment_count = 0

    process_label.set("Process: "+str(process_count))
    segment_label.set("Segment "+str(segment_count)+" of process "+str(process_count)+" :")

def Deallocate_recent_process():
    global Ram
    
    try:
        process_number = int(process_number_entry.get())
    except ValueError:
        return

    Ram = deallocate_process(process_number=process_number,Ram=Ram)
    process_number_entry.delete(0,END)

def Deallocate_old_process():
    global Ram
    
    try:
        process_number = int(process_number_entry.get())
    except ValueError:
        return

    Ram = deallocate_old_process(process_number=process_number,Ram=Ram)
    process_number_entry.delete(0,END)






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
allocate_hole_button.grid(row=4,column=2)
Hole_addition_message = StringVar()
Hole_addition_message.set("")
label_3 = Label(root,textvariable=Hole_addition_message).grid(row=5,column=2)
#################################################################################


########################### process entry partion ###############################
process_label = StringVar()
segment_label = StringVar()
segment_entry_message = StringVar()
chosen_algorithm = StringVar()
chosen_algorithm.set('First Fit')
label_1 = Label(root,textvariable=process_label).grid(row=7,column=1)
label_2 = Label(root,textvariable=segment_label).grid(row=8,column=1)
label_6 = Label(root,text="Segment Name: ").grid(row=9,column=0)
label_7 = Label(root,text="Segment Size: ").grid(row=9,column=2)
label_8 = Label(root,textvariable=segment_entry_message).grid(row=10,column=2)
process_label.set("Process: "+str(process_count))
segment_label.set("Segment "+str(segment_count)+" of process "+str(process_count)+" :")
segment_entry_message.set('')
new_process_button = Button(root,text="New Process",state='disabled')
segment_name_entry = Entry(root,state='disabled')
segment_size_entry = Entry(root,state='disabled')
Algorithm_menu = OptionMenu(root,chosen_algorithm,'First Fit','Best Fit','Worst Fit')
add_segment_button = Button(root,text='Add Segment',state='disabled')
new_process_button.grid(row=7,column=2)
segment_name_entry.grid(row=9,column=1)
segment_size_entry.grid(row=9,column=3)
Algorithm_menu.grid(row=7,column=3)
add_segment_button.grid(row=9,column=4)
##################################################################################


################################### Deallocate process ###########################
label_5 = Label(root,text="Deallocate Process: ").grid(row=11,column=1)
label_9 =Label(root,text="process number:").grid(row=12,column=0)
process_number_entry = Entry(root,state='disabled')
deallocate_button = Button(root,text="Deallocate recent process",state='disabled')
deallocate_old_button = Button(root,text="Deallocate old process ",state='disabled')
process_number_entry.grid(row=12,column=1)
deallocate_button.grid(row=12,column=3)
deallocate_old_button.grid(row=12,column=4)
##################################################################################

################################ Draw ############################################
draw_button = Button(root,text="Draw RAM",state='disabled')
draw_button.grid(row=14,column=2)
##############################################################################




root.mainloop()