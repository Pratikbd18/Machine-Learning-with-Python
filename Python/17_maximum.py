#application to find maximum number
def max(no1 , no2):
    if(no1>no2):
        return no1
    else:
        return no2

def main():

    print("Enter first number : ")
    no1=input()
    print("Enter second number : ")
    no2=input()

    ans = max(int(no1),int(no2))

    print("Max value is : ",ans)

if __name__=="__main__":   
    main()
    