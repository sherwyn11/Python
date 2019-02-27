tt=[]
n=[]
v=[0,1,2,3,4,5,6,7,9]
nv=[False,False,False,False,False,False,False,False,False,False]

def init():
    for i in range(0,3):
        n=[]
        for j in range(0,3):
            n.append(1)
        tt.append(n)

    print("Enter position in the format: ")
    print("7 8 9")
    print("4 5 6")
    print("1 2 3")

def display():
    for i in range(0,3):
        for j in range(0,3):
            if(tt[i][j]==1):
                print(" ",end=" ")
            else:
                print(tt[i][j],end=" ")
        print()


def checkX():
    if((tt[0][0]=="X" and tt[0][1]=="X" and tt[0][2]=="X")or
        (tt[1][0]=="X" and tt[1][1]=="X" and tt[1][2]=="X")or
        (tt[2][0]=="X" and tt[2][1]=="X" and tt[2][2]=="X")or
        (tt[0][0]=="X" and tt[1][0]=="X" and tt[2][0]=="X")or
        (tt[0][1]=="X" and tt[1][1]=="X" and tt[2][1]=="X")or
        (tt[0][2]=="X" and tt[1][2]=="X" and tt[2][2]=="X")or
        (tt[0][0]=="X" and tt[1][1]=="X" and tt[2][2]=="X")or
        (tt[0][2]=="X" and tt[1][1]=="X" and tt[2][0]=="X")):
        return 1
    else:
        return 0

def checkO():
    if((tt[0][0]=="0" and tt[0][1]=="0" and tt[0][2]=="0")or
        (tt[1][0]=="0" and tt[1][1]=="0" and tt[1][2]=="0")or
        (tt[2][0]=="0" and tt[2][1]=="0" and tt[2][2]=="0")or
        (tt[0][0]=="0" and tt[1][0]=="0" and tt[2][0]=="0")or
        (tt[0][1]=="0" and tt[1][1]=="0" and tt[2][1]=="0")or
        (tt[0][2]=="0" and tt[1][2]=="0" and tt[2][2]=="0")or
        (tt[0][0]=="0" and tt[1][1]=="0" and tt[2][2]=="0")or
        (tt[0][2]=="0" and tt[1][1]=="0" and tt[2][0]=="0")):
        return 1
    else:
        return 0


def inp(c):

    if(c==0):
        while(True):
            a=int(input("Enter position to put X: "))
            if(nv[a]==False):
                if(a==7):
                    tt[0][0]="X"
                    nv[7]=True
                elif(a==8):
                    tt[0][1]="X"
                    nv[8]=True
                elif(a==9):
                    tt[0][2]="X"
                    nv[9]=True
                elif(a==4):
                    tt[1][0]="X"
                    nv[4]=True
                elif(a==5):
                    tt[1][1]="X"
                    nv[5]=True
                elif(a==6):
                    tt[1][2]="X"
                    nv[6]=True
                elif(a==1):
                    tt[2][0]="X"
                    nv[1]=True
                elif(a==2):
                    tt[2][1]="X"
                    nv[2]=True
                else:
                    tt[2][2]="X"
                    nv[3]=True
                break
            else:
                print("Try another position")

    else:
        while(True):
            a=int(input("Enter position to put 0: "))
            if(nv[a]==False):
                if(a==7):
                    tt[0][0]="0"
                    nv[7]=True
                elif(a==8):
                    tt[0][1]="0"
                    nv[8]=True
                elif(a==9):
                    tt[0][2]="0"
                    nv[9]=True
                elif(a==4):
                    tt[1][0]="0"
                    nv[4]=True
                elif(a==5):
                    tt[1][1]="0"
                    nv[5]=True
                elif(a==6):
                    tt[1][2]="0"
                    nv[6]=True
                elif(a==1):
                    tt[2][0]="0"
                    nv[1]=True
                elif(a==2):
                    tt[2][1]="0"
                    nv[2]=True
                else:
                    tt[2][2]="0"
                    nv[3]=True
                break
            else:
                print("Try another location")



init()
i=0
while(i<9 and (checkX()!=1 and checkO()!=1)):
    inp(i%2)
    i=i+1
    display()
if(checkX()==1):
    print("X is winner")
elif(checkO()==1):
    print("0 is winner")
else:
    print("Draw")


