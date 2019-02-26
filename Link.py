
class Link:
    data=0
    next=None
    start=None

    def addEnd(self,ptr):
        self.data=int(input("Enter data"))
        self.next=None
        if(Link.start==None):
            Link.start=self
        else:
            ptr=Link.start
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=self

        #return Link.start

    def addBegin(self,ptr):
        self.data=int(input("Enter data"))
        self.next=None
        if(Link.start==None):
            Link.start=self
        else:
            self.next=Link.start
            Link.start=self

        #return Link.start

    def delete(self,ptr):
        a=int(input("Enter data"))
        pre=Link.start
        ptr=Link.start
        if(Link.start==None):
            print("Linked list empty")
        elif(Link.start.data==a):
            Link.start=ptr.next
            print(a,"is removed")
        elif(ptr.next==None and ptr.data==a):
            print(a,"is removed")
            Link.start=None
        else:
            while(ptr.next!=None and a!=ptr.data):
                pre=ptr
                ptr=ptr.next
            if(ptr.next==None and a==ptr.data):
                pre.next=None
            elif(ptr.next==None and a!=ptr.data):
                print("Not present")
            else:
                pre.next=ptr.next
                ptr.next=None
                print(a,"is removed")




    def disp(self,ptr):
        ptr=Link.start
        while(ptr!=None):
            print(ptr.data)
            ptr=ptr.next





a=Link()
b=Link()
c=Link()
d=Link()
e=Link()
f=Link()
g=Link()
ptr=Link()
a.addEnd(ptr)
b.addBegin(ptr)
c.delete(ptr)
d.addBegin(ptr)
e.addEnd(ptr)
f.addEnd(ptr)
f.disp(ptr)

'''
Enter data1
Enter data2
Enter data2
2 is removed
Enter data3
Enter data4
Enter data5
3
1
4
5
'''
