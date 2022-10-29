class Arithematic:
    def __init__(self,A,B):
        print("Inside init method")
        self.no1=A
        self.no2=B

    def Addition(self):
        Ans=self.no1+self.no2
        return Ans

    def Subtrsaction(self):
        Ans=self.no1-self.no2
        return Ans
    
    
def main():
    print("Inside main method")

    obj=Arithematic (11,10)
    Output=obj.Addition()
    print("Addition is: ",Output)

    Output=obj.Subtrsaction()
    print("Subtraction is: ",Output)

    objX=Arithematic(21,20)

if __name__=="__main__":
    print("inside starter")
    main()