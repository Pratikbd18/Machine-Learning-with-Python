print("Application to demonstrate industrial programming")

import modules

def main():
    print("Value of __name__ from main is : ",__name__)

    print("Enter first number:")
    no1=int(input())

    print("Enter sec number:")
    no2=int(input())

    sum = modules.Addition(no1,no2)

    print("Addition is:", sum)

if __name__=="__main__":   
    main()