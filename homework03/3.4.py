#建立节点对象
class Listnode(object):
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
#创建链表对象
class Linkedlist(object):
    def __init__(self):#先定义头节点的实例化对象
        self.head=None
    # 创建链表
    def create(self,alldata):#alldata是表示一组数据
        self.head=Listnode(alldata[0]) #创建好头节点，把第一个数据给到头结点
        cur=self.head  #cur为移动指针
        for i in alldata[1:]:#根据数据的多少，依次创建后面的节点
            p=Listnode(i)
            cur.next=p
            cur=p
        return self.head #返回一个这个实例化头节点
    #遍历链表
    def travel(self):
        if self.head: #先判断头结点是否为空
            p=self.head
            while p:
                print(p.data,end=' ')
                p=p.next
            print('')
        else:
            return
    #增
    def insert(self,value):
 
        q=Listnode(value) #创建一个节点
        q.next=self.head
        self.head=q #新节点作为头结点

    #删
    def delete(self,value):
        if self.find(value)==0:
            print('不存在')
        else:
            if self.head:
                p=self.head
                while p:
                    if p.next.data==value: #获取到要删除节点的上一个节点
                        p.next=p.next.next #把下一个获取到的节点指向下下个节点
                        print('删除成功')
                        break
                    else:
                        p=p.next
                if p==None:
                    print('删除失败')
            else:
                return None
    #改
    def update(self,old,new):
        if self.find(old)==0:
            print('不存在')
        else:
            if self.head:
                p=self.head
                while p.data!=old:
                    p=p.next
                p.data=new
                print('修改成功')
            else:
                return None
    #查
    def search(self,value):
        if self.head:
            count=1
            p=self.head
            while p:
                if p.data==value:
                    print(f'在第{count}个节点')
                    break
                else:
                    p=p.next
                    count+=1
            if p==None:
                print('不存在')
                return -1
        else:
            return None
    def find(self,value):
        flag=0
        if self.head:
            count=1
            p=self.head
            while p:
                if p.data==value:
                    flag=1
                    break
                else:
                    p=p.next
                    count+=1
            if p==None:
                flag=0
            return flag
        else:
            return None
   
if __name__=='__main__':
    l=Linkedlist()
    data=[1,2,3,4,5]
    l.create(data)
    l.travel()

    print("请输入要增加的数：")
    insnum=input()
    l.insert(int(insnum))
    l.travel()

    print("请输入要删除的数：")
    delnum=input()
    l.delete(int(delnum))
    l.travel()

    print("请输入要修改的数,和修改后的新数，用空格隔开：")
    oldnum,newnum=input().split(" ")
    l.update(int(oldnum),int(newnum))
    l.travel()

    print("请输入要查询的数：")
    searchnum=input()
    l.search(int(searchnum))