def chknum(num):
    if(num%2==0):
        print("Given Num is Even Number")

    else:
        print("Odd Number")

def main():
    num=int(input("Enter a number : "))
    chknum(num)

if "__main__"==__name__:
    main()
