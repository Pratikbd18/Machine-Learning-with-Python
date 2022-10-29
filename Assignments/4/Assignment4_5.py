def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def ChkPrime(no):
    count=0
    if(no>=2):
        if(no==2):
            count=0
        else:
            for i in range(2,no):
                if(no%i==0):
                    count=count+1
    return count

def FilterX(Lst,helper_function):
    Result=[]
    for no in Lst:
        if(helper_function(no)==0):
            Result.append(no)
    return Result

def MapX(lst):
    list=[]
    for no in lst:
        Ans=no*2
        list.append(Ans)
    return list

def ReduceX(lst):
    max=0
    for no in lst:
        if(no>max):
            max=no
    return max

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)
    print("Input List: ",Lst)

    Filter_Data=FilterX(Lst,ChkPrime)
    print("List after filter: ",Filter_Data)

    Map_Data=MapX(Filter_Data)
    print("List after map: ",Map_Data)

    Reduce_Data=ReduceX(Map_Data)
    print("List after reduce: ",Reduce_Data)

if __name__=="__main__":
    main()