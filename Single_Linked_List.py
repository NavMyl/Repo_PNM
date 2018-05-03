class Node(object):

    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

    def setnext(self,next):
        self.next=next

    def getnext(self):
        return self.next

    def setdata(self, data):
        self.next = data

    def getdata(self):
        return self.data

    def HasNext(self):
        return self.next!=Null


my_node=Node()
print my_node.hasnext()
