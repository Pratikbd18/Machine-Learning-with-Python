def CheckEven(No):
    if(No%2==0):
        return True
    else:
        return False
    
def CheckEvenX(No):
    return (No%2==0)

CheckEvenXX= lambda No : No%2==0

def main():
    ret =CheckEvenXX(10)

    if(ret==True):
        print("Even Number")
    else:
        print("Odd Number")


if __name__=="__main__":
    main()