
def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def Increment(no):
    return no+10

def FilterX(Lst):
    Result=[]
    for no in Lst:
        if(no>=70):
            Result.append(no)
    return Result

def MapX(Helper_Function,lst):
    list=[]
    for no in lst:
        Ans=Helper_Function(no)
        list.append(Ans)
    return list

def ReduceX(lst):
    product=1
    for no in lst:
        product=product*no
    return product

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)
    print("Input List: ",Lst)

    Filter_Data=FilterX(Lst)
    print("List after filter: ",Filter_Data)

    Map_Data=MapX(Increment,Filter_Data)
    print("List after map: ",Map_Data)

    Reduce_Data=ReduceX(Map_Data)
    print("List after reduce: ",Reduce_Data)

if __name__=="__main__":
    main()