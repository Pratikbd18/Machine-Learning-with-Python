#Normal Functions/Named Functions
def Add(No1,No2):
    return No1+No2

#Lambda Function / Unnamed / Annonymous
#lamba parameters : body

AddFunction = lambda A,B: A+B

Ans1=Add(10,11)
Ans2=AddFunction(10,11)

print("Addition using normal fun: ",Ans1)
print("Addition using LAmbda fun: ",Ans2)
print("Type of lamda function is : ",type(AddFunction))