def Add(*Values):
    sum=0
    for no in Values:
        sum=sum+no
    return sum


def main():
    Ans=Add(10,11,2,4,53,6,54,7,54,4,5,6)
    print("Addition is : ",Ans)


if __name__=="__main__":
    main()