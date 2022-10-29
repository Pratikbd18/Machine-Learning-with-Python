

def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst

def Max(lst):
    mx=0
    for no in lst:
        if(no>mx):
            mx=no
    return mx

def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)
    maxmum=Max(Lst)
    print(maxmum)

if __name__=="__main__":
    main()