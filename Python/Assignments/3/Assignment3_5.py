import MarvellousNum 


def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def ListPrime(lst):
    PrimeList=[]
    for no in lst:
        Count=MarvellousNum.ChkPrime(no)
        if(Count==0):
            PrimeList.append(no)
    return PrimeList

def Sum(lst):
    sum=0
    for no in lst:
        sum=sum+no
    return sum

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)

    Ans=ListPrime(Lst)
    print(Ans)
    sum=Sum(Ans)
    print(sum)

if __name__=="__main__":
    main()


