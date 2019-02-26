avail=[]
need=[]
ma=[]
alloc=[]
proc=[]
work=[]
finish=[]
notfinish=[]

def init(m,n):
    for i in range(0,n):
        finish.append(False)
    for j in range(0,n):
        work.append(0)

def maxx(m,n):
    for i in range(0,n):
        proc=[]
        for j in range(0,m):
            a=int(input("Enter max for process: "))
            proc.append(a)

        ma.append(proc)
    print("Max is:")
    print(ma)

def needs(m,n):
    for i in range(0,n):
        proc=[]
        for j in range(0,m):
            proc.append(ma[i][j]-alloc[i][j])
        need.append(proc)
    print("Need is:")
    print(need)

def allo(m,n):
    for i in range(0,n):
        proc=[]
        for j in range(0,m):
            a=int(input("Enter allocation for process: "))
            proc.append(a)

        alloc.append(proc)
    print("Allocation is:")
    print(alloc)

def av(m,n):
    for j in range(0,m):
        a=int(input("Enter available for process: "))
        avail.append(a)
    print("Available is:")
    print(avail)

def safety(m,n):
    flag=0
    flag2=0
    flag1=0
    count=0
    proc=[]
    for i in range(0,n):
        for j in range(0,m):
            if(finish[i]==False and need[i][j]<=avail[j]):
                flag1=1
            else:
                flag1=0
                break
        if(flag1==1):
            for j in range(0,m):
                avail[j]=avail[j]+alloc[i][j]

            finish[i]=True
            proc.append(i)
        else:
            count=count+1
            notfinish.append(i)


    flag1=0
    while(flag2!=1):
        for i in range(0,count):
            x=notfinish[0]
            for j in range(0,m):
                if(need[x][j]<=avail[j]):
                    flag1=1
                else:
                    flag1=0
                    break
            if(flag1==1):
                for j in range(0,m):
                    avail[j]=avail[j]+alloc[x][j]

                finish[x]=True
                proc.append(x)
                notfinish.remove(x)
            else:
                notfinish.append(x)
        if(len(notfinish)==0):
            flag2=1


    print("New available is:")
    print(avail)
    print("Process order to avoid deadlock is:")
    print(proc)



n=int(input("Enter no of processes: "))
m=int(input("Enter no of resources: "))
maxx(m,n)
allo(m,n)
init(m,n)
needs(m,n)
av(m,n)
safety(m,n)

'''
Enter no of processes: 5
Enter no of resources: 3
Enter max for process: 7
Enter max for process: 5
Enter max for process: 3
Enter max for process: 3
Enter max for process: 2
Enter max for process: 2
Enter max for process: 9
Enter max for process: 0
Enter max for process: 2
Enter max for process: 2
Enter max for process: 2
Enter max for process: 2
Enter max for process: 4
Enter max for process: 3
Enter max for process: 3
Max is:
[[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
Enter allocation for process: 0
Enter allocation for process: 1
Enter allocation for process: 0
Enter allocation for process: 2
Enter allocation for process: 0
Enter allocation for process: 0
Enter allocation for process: 3
Enter allocation for process: 0
Enter allocation for process: 2
Enter allocation for process: 2
Enter allocation for process: 1
Enter allocation for process: 1
Enter allocation for process: 0
Enter allocation for process: 0
Enter allocation for process: 2
Allocation is:
[[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
Need is:
[[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]
Enter available for process: 3
Enter available for process: 3
Enter available for process: 2
Available is:
[3, 3, 2]
New available is:
[10, 5, 7]
Process order to avoid deadlock is:
[1, 3, 4, 0, 2]

----------------------------------------------------------------

Enter no of processes: 4
Enter no of resources: 3
Enter max for process: 4
Enter max for process: 3
Enter max for process: 1
Enter max for process: 2
Enter max for process: 1
Enter max for process: 4
Enter max for process: 1
Enter max for process: 3
Enter max for process: 3
Enter max for process: 5
Enter max for process: 4
Enter max for process: 1
Max is:
[[4, 3, 1], [2, 1, 4], [1, 3, 3], [5, 4, 1]]
Enter allocation for process: 1
Enter allocation for process: 0
Enter allocation for process: 1
Enter allocation for process: 1
Enter allocation for process: 1
Enter allocation for process: 2
Enter allocation for process: 1
Enter allocation for process: 0
Enter allocation for process: 3
Enter allocation for process: 2
Enter allocation for process: 0
Enter allocation for process: 0
Allocation is:
[[1, 0, 1], [1, 1, 2], [1, 0, 3], [2, 0, 0]]
Need is:
[[3, 3, 0], [1, 0, 2], [0, 3, 0], [3, 4, 1]]
Enter available for process: 3
Enter available for process: 3
Enter available for process: 0
Available is:
[3, 3, 0]
New available is:
[8, 4, 6]
Process order to avoid deadlock is:
[0, 2, 1, 3]
'''
