stack=[]

def push(s):
    stack.append(s)

def pop():
    if(len(stack)==0):
        print("Stack is empty")
    else:
        del stack[-1]

def top():
    print(stack[-1])

push(1)
push(2)
push(6)
print(stack)
pop()
top()
print(stack)
