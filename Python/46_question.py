
class Numbers():
    def __init__(self):
        pass
       

    def accept(self):
        lst=[]
        no=int(input("How many numbers you want: "))
        for i in range(0,no,1):
            n=int(input())
            lst.append(n)
        return lst


def main():
    
    obj=Numbers()
    list=obj.accept()
    print(list)


if __name__=="__main__":
    main()