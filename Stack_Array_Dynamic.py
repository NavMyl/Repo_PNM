class Stack(object):
    def __init__(self,limit=10):
        self.stck=[]
        self.limit=limit

    def size(self):
        return len(self.stck)

    def IsEmptyStack(self):
        if len(self.stck) <= 0:
            print 'Stack is Empty!'
            return 0

    def IsFullStack(self):
        if len(self.stck) <= self.limit:
            print 'Stack is Full!'

    def  Push(self,item):
        if len(self.stck) >= self.limit:
            self.resizeStack()
        self.stck.append(item)
        print 'Element is Inserted!', self.stck

    def pop(self):
        if len(self.stck) <= 0:
            print 'Stack is Empty!'
        else:
            self.stck.pop()

    def peek(self):
        if len(self.stck) <= 0:
            print 'Stack is Empty!'
        else:
            return self.stck[-1]

    def resizeStack(self):
       newstck = self.stck
       self.limit=2*self.limit
       self.stck=newstck

my_stack = Stack(5)
my_stack.Push("20")
my_stack.Push("30")
my_stack.Push("40")
my_stack.Push("10")
my_stack.Push("50")
my_stack.Push("60")
print my_stack.peek()