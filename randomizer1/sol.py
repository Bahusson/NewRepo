
Inp=input("Please type your comma separated integers here:" )

lst1=[]
Inp=Inp.split(',')

lst1 = [int(item) for item in Inp]
lst2=sorted(lst1)
print (lst2)
x=0
while True:
    x=x+1
    if x not in lst2:
        print(x)
        break
