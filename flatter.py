l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
k = []
def flatter(x):
    
    for i in x:
        if type(i) == list:
            flatter(i)
        else:
            k.append(i)
    return k
    
print(flatter(l))

