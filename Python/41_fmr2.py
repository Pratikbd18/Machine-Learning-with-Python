def Accept_List(iSize):
    Data_Input=[]
    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    return Data_Input

def CheckEven(No):
    return(No%2==0)

def filterX(Helper_Function,Data):
    Result=[]
    for no in Data:
        if(Helper_Function(no)==True):
            Result.append(no)
    return Result

def MultiplyX(no):
    return no*2

def mapX(Helper_Function,Data):
    Result=[]
    for no in Data:
        Result.append(Helper_Function(no))
    return Result

def Sum(A,B):
    return A+B

def ReduceX(Helper_Function,Data):
    sum=0
    for no in Data:
        sum=Sum(sum,no)
    return sum


def main():
    print("Enter number of elements you want to insert : ")

    iSize=int(input())
    Data=Accept_List(iSize)

    Data_Filter=filterX(CheckEven,Data)
    print(Data_Filter)

    Data_Map=mapX(MultiplyX,Data_Filter)
    print(Data_Map)

    Data_Reduce=ReduceX(Sum,Data_Map)
    print(Data_Reduce)


if __name__=="__main__":
    main()