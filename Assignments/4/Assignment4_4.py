
def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

Square = lambda no:no*no

def FilterX(Lst):
    Result=[]
    for no in Lst:
        if(no%2==0):
            Result.append(no)
    return Result

def MapX(Helper_Function,lst):
    list=[]
    for no in lst:
        Ans=Helper_Function(no)
        list.append(Ans)
    return list

def ReduceX(lst):
    sum=0
    for no in lst:
        sum=sum+no
    return sum

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)
    print("Input List: ",Lst)

    Filter_Data=FilterX(Lst)
    print("List after filter: ",Filter_Data)

    Map_Data=MapX(Square,Filter_Data)
    print("List after map: ",Map_Data)

    Reduce_Data=ReduceX(Map_Data)
    print("List after reduce: ",Reduce_Data)

if __name__=="__main__":
    main()