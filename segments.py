class segment(object):
    def __init__(self,name,start,size):
        self.start = start
        self.size = size
        self.end = start+size
        self.name = name
