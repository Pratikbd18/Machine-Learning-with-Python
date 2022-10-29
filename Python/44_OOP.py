# accept 2numbers and perform addition and subtraction

# kay karaych ahe?  => Behaviours(Functions)
# Addtion and Subtraction

# te karayla kay lagnar ahe?  => Characterstics (Data)
# 2 numbers

# class = Characterstics + Behaviours
# class = Data + Functions

class Arithematic:

    def __init__(self ,A,B):
        self.No1=A
        self.No2=B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2

def main():

    print("Enter First No: ")
    Value1=int(input())

    print("Enter Second No: ")
    Value2=int(input())

    obj=Arithematic(Value1,Value2)

    Ans=obj.Add()
    print("Addition is: ",Ans)

    Ans=obj.Sub()
    print("Subtraction is: ",Ans)

if __name__=="__main__":
    main()