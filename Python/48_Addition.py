class Numbers():
    def __init__(self):
        self.Size=0
        self.Arr=list()

    def accept(self):
        self.Size=int(input("How many numbers you want: "))
        print("Enter Elemets: ")
        value=0
        for i in range(0,self.Size):
            value=int(input())
            self.Arr.append(value)
    
    def Display(self):
        print("Elements from list are: ")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum=0
        for i in range(0,self.Size):
            Sum=Sum+self.Arr[i]
        return Sum


def main():
    
    obj=Numbers()
    obj.accept()
    obj.Display()
    
    Output=obj.Summation()
    print("Sum of all elements: ",Output)
    
if __name__=="__main__":
    main()