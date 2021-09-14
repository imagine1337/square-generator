import random
def randsquare():
    x1=random.randint(0,600)
    x2=random.randint(0,600)
    y1=random.randint(0,400)
    y2=random.randint(0,400)
    if x1>x2:
        a1=[x1,x2]
    else:
        a1=[x2,x1]
    if y1>y2:
        a2=[y1,y2]
    else:
        a2=[y2,y1]
    return a1,a2
