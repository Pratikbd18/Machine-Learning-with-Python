
def main():
    n=int(input())
    lst=[]
    arr=[]
    for i in range(0,n):
        num=int(input())
        lst.append(num)
    print(lst)

    for no in lst:
        if (no%2==0):
            arr.append(no+2)
    print(arr)

    sum=0
    for no in arr:
        sum=sum+no

    print("Sum is with increment of 2",sum)
if __name__=="__main__":
    main()