

A=[1, 3, 6, 4, 1, 2]

def solution(A):

    lst2=sorted(A)
    x=0
    while True:
        x=x+1
        if x not in lst2:
            return(x)
            break

    pass
