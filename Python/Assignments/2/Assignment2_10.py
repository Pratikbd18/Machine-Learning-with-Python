def main():
    n=int(input())
    sum=0
    for i in str(n):
        sum=int(i)+sum
    print(sum)

if "__main__"==__name__:
    main()