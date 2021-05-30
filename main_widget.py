from  tkinter import *
from Draw import paint
from segments import *

Segments = []

for i in range(5):
    new_segment = segment("P"+str(i),i*100,100)
    Segments.append(new_segment)

root = Tk()

button = Button(root,text = 'draw',command = lambda: paint(Segments) )
button.pack()
root.mainloop()