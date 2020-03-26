def split(word):
    return list(word)

def accum(s):
    s=list(enumerate(split(s.lower())))
    a=[]
    a.append(s[0][1].upper())
    
    for i,c in s:
        a.append('-')
        for j in range(i):
            if(j==0):
                a.append(c.upper())
            a.append(c)
    a.pop(-(len(a)-2))
    return "".join(a)

print(accum("chad"))




