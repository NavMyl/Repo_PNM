class Node():
    def __init__(self,data,next):
        self.data=data
        self.next=None

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next=next

    def getData(self):
        return self.data

    def setdata(self,data):
        self.data = data



class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0

    def NodeSize(self):
        return self.size

    def addNode(self,data):
        new_node = Node(data,self.head)
        self.head=new_node
        self.size+=1
        return True

    def printNode(self):
        curr = self.head
        #print self.head
        while curr:
            print(curr.data)
            curr = curr.getNext()


if  __name__== '__main__':

    LList = LinkedList()
    print("Inserting")
    print(LList.addNode(10))
    print(LList.addNode(25))
    print(LList.addNode(50))
    print("Printing")
    LList.printNode()
    print("Size")
    print(LList.NodeSize())
