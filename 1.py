class Stack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        if len(self.data )== 0:
            return True
        else:
            return False
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if len(self.data)== 0:
            return "Empty stack"
        else:
            return self.data.pop()
    def size(self):
        return len(self.data)
    def top(self):
        return self.data[-1]
    def getData(self):
        return self.data
            
class Queue:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def first(self,item):
        return self.data[0]
    def size(self):
        return len(self.data)
    

q = Queue()
q.enqueue('Abreham the')
q.enqueue('Abeselom Tsegazeab')
q.enqueue('Chunu Chuni')
print(q.dequeue())
# print(q.dequeue())
