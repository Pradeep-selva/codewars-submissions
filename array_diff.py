def array_diff(a, b):
    b=list(set(b))
    l=[]
    for i in a:
        if i not in b:
            l.append(i)
    
    return l

print(array_diff([1,1,2], [2]))