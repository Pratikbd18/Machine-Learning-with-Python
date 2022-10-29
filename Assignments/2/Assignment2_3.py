def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

    print("2nd method")
    i=1
    facts=1
    while(i>n+1):
        facts=facts*i
        i=i+1
    print("facts",facts)
    
def main():
    n=int(input())
    fact(n)

if "__main__"==__name__:
    main()