def CheckEven(No):
    return (No%2==0)

def Increment(No):
    return No+2

def filterX(Arr,Function_Name):
    Result=[]
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result=[]
    for no in Arr:
        Value=Function_Name(no)
        Result.append(Value)
    return Result

def ReduceX(Arr):
    sum=0
    for i in Arr:
        sum=sum+i
    return sum

def main():
    Arr=[2,3,1,6,4,5,11,16,20]

    print("Original Data : ",Arr)

    Data_Filter=list(filterX(Arr,CheckEven))
    print("Filtering Data : ",Data_Filter)

    Data_map=list(mapX(Data_Filter,Increment))
    print("Data after mapping : ",Data_map)

    ret = ReduceX(Data_map)
    print("Data after reduce : ", ret)

if __name__=="__main__":
    main()