Stack = []
top = -1
maxSize = 10

def push(data):
    global top 
    if not isFull():
        top += 1
        Stack.append(data)

def pop():
    global top
    if not isEmpty():
        top -= 1
        return Stack.pop()

def peek():
    global top
    if not isEmpty():
        return Stack[top]

def isEmpty():
    if top == -1:
        print("Stack underflow")
        return True
        
    else:
        return False

def isFull():
    if top == maxSize - 1:
        print("Stack overflow")
        return True
        
    else:
        return False
    

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
push(11)
print(pop())
print(peek())

print(Stack)

