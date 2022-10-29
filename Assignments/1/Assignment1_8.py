def star(n):
    for i in range(0,n):
        print("*",end=" ")

def main():
    n=int(input())
    star(n)

if "__main__"==__name__:
    main()