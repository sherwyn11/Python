queue=[]

def enque(s):
    queue.append(s)

def deque():
    if(len(queue)==0):
        print("queue is empty")
    else:
        del queue[0]

enque(1)
enque(2)
enque(6)
print(queue)
deque()
print(queue)
