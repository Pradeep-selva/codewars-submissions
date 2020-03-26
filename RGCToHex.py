def alphaCheck(ch):
    return ch.isalpha()
def rgb(r, g, b):
    if(r<0):
        r=0
    if(g<0):
        g=0
    if(b<0):
        b=0
    if(r>255):
        r=255
    if(g>255):
        g=255
    if(b>255):
        b=255
    
    r=str(hex(r))[2:].upper()
    g=str(hex(g))[2:].upper()
    b=str(hex(b))[2:].upper()
    
    if(len(r)==1):
        r="0"+r
    if(len(g)==1):
        g="0"+g
    if(len(b)==1):
        b="0"+b

    return "{}{}{}".format(r,g,b)

print(rgb(0,0,0))
