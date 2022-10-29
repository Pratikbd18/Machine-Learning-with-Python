def Accept(n):
    lst=[]
    for i in range(0,n):
        no=int(input())
        lst.append(no)
    return lst
    
def freq(lst,no):
    count=0
    for i in lst:
        if(i==no):
            count=count+1
    print(count)



def main():
    No=int(input("Enter how many number you want to insert: "))
    Lst=Accept(No)

    Key=int(input("Enter key u want to insert: "))
    
    freq(Lst,Key)

if __name__=="__main__":
    main()