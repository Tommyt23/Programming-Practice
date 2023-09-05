class Stack:
    def __init__(self, maxSize):
        self.stack = []
        self.top = -1
        self.maxsize = maxSize
        
    def push(self, data):
        if not self.isFull():
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
    
    def isEmpty(self):
        if self.top == -1:
            print("Stack underflow")
            return True
            
        else:
            return False
        
    def isFull(self):
        if self.top == self.maxsize - 1:
            print("Stack overflow")
            return True
            
        else:
            return False
        

stack = Stack(10)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.push(11)
print(stack.pop())
print(stack.peek())


