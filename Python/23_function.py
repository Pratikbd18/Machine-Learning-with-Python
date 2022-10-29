def factorials(no):
    i=1
    print("Factors of",no,"Are : ")
    while(i<=int(no/2)):
        if(no%i==0):
            print(i)
        i=i+1
def main():

    no=int(input())

    factorials(no)




    
if __name__=="__main__":
    main()