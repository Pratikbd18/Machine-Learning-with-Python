def star(n):
    for i in range(0,5):
        for j in range(0,5):
            print("*",end="")
        print()

def main():
    n=int(input())
    star(n)

if "__main__"==__name__:
    main()