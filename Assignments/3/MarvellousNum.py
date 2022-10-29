def ChkPrime(no):
    count=0
    if(no>=2):
        if(no==2):
            count=0
        else:
            for i in range(2,no):
                if(no%i==0):
                    count=count+1
    return count

