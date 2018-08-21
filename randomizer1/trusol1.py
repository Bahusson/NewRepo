S="ABBCC"

x=1
while True:
    try:
        S=S.replace(AB,AA, 1)
    except:
        x=1
    try:
        S=S.replace(BA,AA, 1)
    except:
        x=1
    try:
        S=S.replace(CB,CC, 1)
    except:
        x=1
    try:
        S=S.replace(BC,CC, 1)
    except:
        x=1
    try:
        S=S.replace(AA,A, 1)
    except:
        x=1
    try:
        S=S.replace(CC,C, 1)
    except:
        x=1
    if x>0:
        x=0
        continue
    else:
        print(S)
        break
