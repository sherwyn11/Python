final=[]
gchart=[]
new=[]
pro=[]
pid=[]

class Process:

    i=1

    def inp(self):
        self.at=(int(input(f"Enter arrival time of process {i+1}: ")))
        self.bt=(int(input(f"Enter burst time of process {i+1}: ")))
        self.id=Process.i
        self.ct=0
        self.tat=0
        self.wt=0
        self.check=0
        Process.i+=1

    def sorting(self,final,n):
        flag=0
        for i in range(0,n):
            if(final[i].at!=0):
                flag=1
                break
            else:
                flag=0

        if(flag==0):
            for j in range(len(final)):
                swapped = False
                i = 0
                while (i<len(final)-1):
                    if (final[i].bt>final[i+1].bt):
                        final[i],final[i+1] = final[i+1],final[i]
                        swapped = True
                    i = i+1
                if (swapped == False):
                    break
        else:
            for j in range(len(final)):
                swapped = False
                i = 0
                while (i<len(final)-1):
                    if (final[i].at>final[i+1].at):
                        final[i],final[i+1] = final[i+1],final[i]
                        swapped = True
                    i = i+1
                if (swapped == False):
                    break

    def sortbt(self,pro,n):
        for j in range(len(pro)):
            swapped = False
            i = 0
            while (i<len(pro)-1):
                if (pro[i].bt>pro[i+1].bt):
                    pro[i],pro[i+1] = pro[i+1],pro[i]
                    swapped = True
                i = i+1
            if (swapped == False):
                break
        return pro

    def work(self,final,n):
        run=0
        count=0
        t=0
        new=final.copy()
        sum=final[0].at
        gchart.append(final[0].at)
        new[0].check=1
        pid.append(new[0].id)
        while(count<n):

            i=0
            if(run==0):
                sum=sum+new[0].bt
                run=1
            else:
                sum=sum+new[t].bt
                t+=1
            x=pid.pop(0)
            for ids in range(0,n):
                if(x==final[ids].id):
                    final[ids].ct=sum

            x=new.pop(0)
            for j in range(0,len(new)):
                if(sum>=new[j].at and new[j].check==0):
                    new[j].check=1
                    pro.append(new[j])
                    flag=1
            if(flag==1):
                for j in range(len(pro)):
                    swapped = False
                    i = 0
                    while (i<len(pro)-1):
                        if (pro[i].bt>pro[i+1].bt):
                            pro[i],pro[i+1] = pro[i+1],pro[i]
                            swapped = True
                        i = i+1
                    if (swapped == False):
                        break
                new=pro.copy()
            for j in range(0,len(new)):
                pid.append(new[j].id)
            gchart.append(sum)
            count+=1

        tats=0
        for i in range(0,n):
            final[i].tat=final[i].ct-final[i].at
            tats=tats+final[i].tat
        print("Total TAT =",tats)

        wts=0
        for i in range(0,n):
            final[i].wt=final[i].tat-final[i].bt
            wts=wts+final[i].wt

        print("Total WT =",wts)

        print("Avg TAT is",tats/n)
        print("Avg WT is",wts/n)
        print("Gantt Chart :")
        print(gchart)

n=int(input("Enter number processes : "))
for i in range(0,n):
    b=Process()
    b.inp()
    final.append(b)

b.sorting(final,n)
b.work(final,n)

'''
Enter number processes : 4
Enter arrival time of process 1: 1
Enter burst time of process 1: 4
Enter arrival time of process 2: 2
Enter burst time of process 2: 2
Enter arrival time of process 3: 0
Enter burst time of process 3: 8
Enter arrival time of process 4: 3
Enter burst time of process 4: 3
Total TAT = 42
Total WT = 25
Avg TAT is 10.5
Avg WT is 6.25
Gantt Chart :
[0, 8, 10, 13, 17]

-----------------------------------------
Enter number processes : 4
Enter arrival time of process 1: 0
Enter burst time of process 1: 21
Enter arrival time of process 2: 0
Enter burst time of process 2: 3
Enter arrival time of process 3: 0
Enter burst time of process 3: 6
Enter arrival time of process 4: 0
Enter burst time of process 4: 2
Total TAT = 50
Total WT = 18
Avg TAT is 12.5
Avg WT is 4.5
Gantt Chart :
[0, 2, 5, 11, 32]
'''
