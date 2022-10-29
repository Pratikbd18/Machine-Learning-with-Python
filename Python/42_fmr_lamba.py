from functools import reduce

def Accept_List(iSize):
    Data_Input=[]
    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    return Data_Input


def filterX(Helper_Function,Data):
    Result=[]
    for no in Data:
        if(Helper_Function(no)==True):
            Result.append(no)
    return Result



def mapX(Helper_Function,Data):
    Result=[]
    for no in Data:
        Result.append(Helper_Function(no))
    return Result



def ReduceX(Helper_Function,Data):
    sum=0
    for no in Data:
        sum=Sum(sum,no)
    return sum


def main():
    print("Enter number of elements you want to insert : ")

    iSize=int(input())
    Data=Accept_List(iSize)

    Data_Filter=filter((lambda No:No%2==0),Data)
    print(Data_Filter)

    Data_Map=map((lambda no: no*2),Data_Filter)
    print(Data_Map)

    Data_Reduce=reduce((lambda A,B : A+B),Data_Map)
    print(Data_Reduce)


if __name__=="__main__":
    main()