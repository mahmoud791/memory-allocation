from tkinter import *

def paint(segments):
    sketch = Tk()    
    sketch.title("memory sketch")
    sketch.geometry("500x1000")
    
    memory_sketch = Canvas(sketch,width=200,height=800,bg="white")
    
    memory_sketch.pack(pady=20)

    memory_sketch.create_text(40,100,text="0")
   
    for i in range(len(segments)):
        memory_sketch.create_text(40,130+(30*i),text=segments[i].end)
        memory_sketch.create_rectangle(50,100+(30*i),150,130+(30*i))
        memory_sketch.create_text(100,115+(30*i),text=segments[i].name)
    
    sketch.mainloop()


