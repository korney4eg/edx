class Queue(object):
    def __init__(self):
        self.vals=[]

    def insert(self,e):
        self.vals.append(e)

    def remove(self):
        if len(self.vals)>0:
            x = self.vals[0]
            del self.vals[0]
            return x
        else:
            raise ValueError()
