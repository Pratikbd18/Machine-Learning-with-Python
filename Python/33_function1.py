#function accespts nothing and return nothing
def Demo1():
    print("Inside demo1")


#function accespts one parameter and return nothing
def Demo2(No):
    print('inside demo 2 with argument :',No)

#function accept one parameter and return one parameter
def Demo3(No):
    print("Inside Demo 3 with argument",No)
    return No+2

#function accepts two parameter and return one parameter
def Demo4(No1,No2):
    print("inside demo4")
    Add=No1+No2
    return Add

def Demo5(No1,No2):
    print("inside demo5")
    Add=No1+No2
    Sub=No1-No2
    return Add,Sub


def main():
    Demo1()
    print()

    Demo2("Hello")
    print()

    Ans=Demo3(10)
    print("Return value of Demo3 is : ",Ans)
    print()

    Ans=Demo4(10,11)
    print("Return value is :",Ans)
    print()
    
    Ans1,Ans2=Demo5(10,11)
    print("First Return value is :",Ans1)
    print("Second Return value is :",Ans2)




if __name__=="__main__":
    main()