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


def main():
    
    obj=Numbers()
    obj.accept()
    obj.Display()
    print(obj.Arr)
    
if __name__=="__main__":
    main()