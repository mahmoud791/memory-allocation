class segment(object):
    def __init__(self,name,start,size):
        self.start = start
        self.size = size
        self.end = start+size
        self.name = name

    def calculate_end(self):
        self.end = self.start +self.size





def hole_addition_validity(Holes,new_hole,memory_size):
    for hole in Holes:
        if new_hole.start >= hole.start and new_hole.start <= hole.end:
            return False


    if(new_hole.start >= memory_size or new_hole.start < 0):
        return False

    if(new_hole.end > memory_size):
        return False



    return True


def segment_addition_validity(Holes,segment): ### this function is completely wrong and needs to be modified
                                              #### the only solution is to allocate segment by and if a segment of the same process 
                                              #doesnt fit , deallocte all the process
    for hole in Holes:
        if(segment.size < hole.size):
            return True
    
    return False
