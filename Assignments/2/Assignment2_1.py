def Add(a,b):
    print("Addition is " ,a+b)
def Sub(a,b):
    print("Subtraction is " ,a-b)
def Mult(a,b):
    print("Multipliacation is " ,a*b)
def Div(a,b):
    print("Division is " ,a/b)

def main():
    a=int(input())
    b=int(input())

    Add(a,b)
    Sub(a,b)
    Mult(a,b)
    Div(a,b)

if "__main__"==__name__:
    main()