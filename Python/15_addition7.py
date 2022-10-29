print("application to demonstrate industrial programming")

def Addition(Value1, Value2):
    ans = Value1 + Value2
    return ans

def main():
    print("Enter first number:")
    no1=int(input())
    print("Enter sec number:")
    no2=int(input())

    sum = Addition(no1,no2)

    print("Addition is:", sum)

if __name__=="__main__":  
    main()