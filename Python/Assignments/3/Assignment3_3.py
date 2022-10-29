def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def Min(lst):
    mx=99999999
    for no in lst:
        if(no<mx):
            mx=no
    return mx

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)
    minmum=Min(Lst)
    print(minmum)

if __name__=="__main__":
    main()