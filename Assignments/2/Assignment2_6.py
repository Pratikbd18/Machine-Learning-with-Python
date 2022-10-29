def main():
    n=int(input())
    for i in range (0,n):
        for j in range(0,n-i):
            print("*",end=" ")
        print()


if "__main__"==__name__:
    main()