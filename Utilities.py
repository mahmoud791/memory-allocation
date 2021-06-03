class segment(object):
    def __init__(self,name,start,size):
        self.start = start
        self.size = size
        self.end = start+size
        self.name = name

    def update_end(self):
        self.end = self.start +self.size





def hole_addition_validity(Holes,new_hole,memory_size):
    for hole in Holes:
        if new_hole.start >= hole.start and new_hole.start < hole.end:
            return False


    if(new_hole.start >= memory_size or new_hole.start < 0):
        return False

    if(new_hole.end > memory_size):
        return False



    return True



def Allocate_segment(Ram,new_segment,algorithm):

    if(algorithm == "First Fit"):
        for i in range(len(Ram)):
            if(Ram[i].name[0]=="H" and Ram[i].size >= new_segment.size):
                
                new_segment.start = Ram[i].start
                new_segment.update_end()
                Ram[i].start = new_segment.end
                Ram[i].size = Ram[i].size - new_segment.size
    
                Ram.insert(i,new_segment)
                return Ram

    
    elif(algorithm == "Best Fit"):
        minimum_size = 10000000
        min = 0
        for i in range(len(Ram)):
            if(Ram[i].name[0]=="H" and Ram[i].size >= new_segment.size):
                if(Ram[i].size < minimum_size):
                    minimum_size = Ram[i].size
                    min = i

        if min == 0:
            return None


        new_segment.start = Ram[min].start
        new_segment.update_end()
        Ram[min].start = new_segment.end
        Ram[min].size -= new_segment.size
        Ram.insert(min,new_segment)
        return Ram


    elif(algorithm == "Worst Fit"):
        maximum_size = 0
        max = 0
        for i in range(len(Ram)):
            if(Ram[i].name[0]=="H" and Ram[i].size >= new_segment.size):
                if(Ram[i].size > maximum_size):
                    maximum_size = Ram[i].size
                    max = i 
        
        if max == 0:
            return None

        new_segment.start = Ram[max].start
        new_segment.update_end()
        Ram[max].start = new_segment.end
        Ram[max].size = Ram[max].size - new_segment.size
        Ram.insert(max,new_segment)
        return Ram



def merge_holes(Ram):
    
    for i in range(len(Ram)-1):
        if(Ram[i].name[0] == "H" and Ram[i+1].name[0]=="H"):
            Ram[i+1].size += Ram[i].size
            Ram[i+1].start = Ram[i].start
            Ram[i+1].update_end()
            Ram[i].size = 0
    
    return delete_rubbish(Ram)
            
            
                  

def delete_rubbish(segments):
    
    clean_segments = []

    for segment in  segments:
        if(segment.size == 0):
            continue
        else:
            clean_segments.append(segment)
    
    return clean_segments
            
               
def deallocate_process(process_number,Ram):

    for i  in range(len(Ram)):
        if(Ram[i].name[1]==str(process_number)):
            Ram[i].name = "Hole"
        
    return merge_holes(Ram)
    

def deallocate_old_process(process_number,Ram):
    
    for i  in range(len(Ram)):
        if(Ram[i].name[-1]==str(process_number)):
            Ram[i].name = "Hole"
        
    return merge_holes(Ram)



    
