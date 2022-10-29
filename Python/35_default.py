def Area(Radius,PI=3.14):
    Result=PI*Radius*Radius
    return Result

def main():
    Rvalue=10.5
    PIvalue=3.14

    Ans=Area(Rvalue,PIvalue)  #positional
    print("area of circle is :",Ans)

    Ans=Area(PI=PIvalue,Radius=Rvalue)  #key
    print("area of circle is :",Ans)

    Ans=Area(10.5)  #default
    print("area of circle is :",Ans)

    Ans=Area(Radius=10.5)  #default+Keyword
    print("area of circle is :",Ans)

    Ans=Area(Radius=10.5,PI=7.10)  #keyword
    print("area of circle is :",Ans)
    

if __name__ == "__main__":
    main()