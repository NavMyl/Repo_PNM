class Stack(object):
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit

    def size(self):
        return len(self.stk)

    def IsEmptyStack(self):
        if len(self.stk) <= 0:
            print 'Stack is Empty!'
            return 0

    def IsFullStack(self):
        if len(self.stk) <= self.limit:
            print 'Stack is Full!'

    def  Push(self,item):
        if len(self.stk) >= self.limit:
            print 'Stack is Full!'
        else:
            self.stk.append(item)
            print 'Element is Inserted!', self.stk

    def pop(self):
        if len(self.stk) <= 0:
            print 'Stack is Empty!'
        else:
            self.stk.pop()

    def peek(self):
        return self.stk[-1]

my_stack = Stack(5)
my_stack.Push("10")
my_stack.Push("20")
my_stack.Push("30")
my_stack.Push("40")
my_stack.Push("50")
my_stack.Push("60")
my_stack.Push("70")
my_stack.Push("80")
print my_stack.peek()
print my_stack.pop()