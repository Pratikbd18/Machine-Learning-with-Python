def divisibleby5(num):
    if(num%5==0):
        print("Divisible By 5")
    else:
        print("Not Divisible")

def main():
    num=int(input())
    divisibleby5(num)

if "__main__"==__name__:
    main()