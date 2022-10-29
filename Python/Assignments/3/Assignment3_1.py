def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def Sum(lst):
    sum=0
    for no in lst:
        sum=sum+no
    return sum

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)

    Sum=sum(Lst)
    print(Sum)



if __name__=="__main__":
    main()