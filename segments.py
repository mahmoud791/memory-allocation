class segment(object):
    def __init__(self,name,start,size):
        self.start = start
        self.size = size
        self.end = start+size
        self.name = name

    def calculate_end(self):
        self.end = self.start +self.size





def hole_addition_validity(Holes,new_hole):
    for hole in Holes:
        if new_hole.start >= hole.start and new_hole.start <= hole.end:
            return False
        
    return True
