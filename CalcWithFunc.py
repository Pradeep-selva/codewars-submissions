def zero(exp= -1):
    res=0
    if(exp==-1):
        return '0'
    if(exp[0]=='*'):
        res=0*int(exp[1])
    if(exp[0]=='/'):
        res=int(0/int(exp[1]))
    if(exp[0]=='+'):
        res=0+int(exp[1])
    if(exp[0]=='-'):
        res=0-int(exp[1])
    
    return res

def one(exp= -1):
    res=0
    if(exp==-1):
        return '1'
    if(exp[0]=='*'):
        res=1*int(exp[1])
    if(exp[0]=='/'):
        res=int(1/int(exp[1]))
    if(exp[0]=='+'):
        res=1+int(exp[1])
    if(exp[0]=='-'):
        res=1-int(exp[1])
    
    return res

def two(exp= -1):
    res=0
    if(exp==-1):
        return '2'
    if(exp[0]=='*'):
        res=2*int(exp[1])
    if(exp[0]=='/'):
        res=int(2/int(exp[1]))
    if(exp[0]=='+'):
        res=2+int(exp[1])
    if(exp[0]=='-'):
        res=2-int(exp[1])
    
    return res

def three(exp= -1):
    res=0
    if(exp==-1):
        return '3'
    if(exp[0]=='*'):
        res=3*int(exp[1])
    if(exp[0]=='/'):
        res=int(3/int(exp[1]))
    if(exp[0]=='+'):
        res=3+int(exp[1])
    if(exp[0]=='-'):
        res=3-int(exp[1])
    
    return res

def four(exp= -1):
    res=0
    if(exp==-1):
        return '4'
    if(exp[0]=='*'):
        res=4*int(exp[1])
    if(exp[0]=='/'):
        res=int(4/int(exp[1]))
    if(exp[0]=='+'):
        res=4+int(exp[1])
    if(exp[0]=='-'):
        res=4-int(exp[1])
    
    return res

def five(exp= -1):
    res=0
    if(exp==-1):
        return '5'
    if(exp[0]=='*'):
        res=5*int(exp[1])
    if(exp[0]=='/'):
        res=int(5/int(exp[1]))
    if(exp[0]=='+'):
        res=5+int(exp[1])
    if(exp[0]=='-'):
        res=5-int(exp[1])
    
    return res

def six(exp= -1):
    res=0
    if(exp==-1):
        return '6'
    if(exp[0]=='*'):
        res=6*int(exp[1])
    if(exp[0]=='/'):
        res=int(6/int(exp[1]))
    if(exp[0]=='+'):
        res=6+int(exp[1])
    if(exp[0]=='-'):
        res=6-int(exp[1])
    
    return res

def seven(exp= -1):
    res=0
    if(exp==-1):
        return '7'
    if(exp[0]=='*'):
        res=7*int(exp[1])
    if(exp[0]=='/'):
        res=int(7/int(exp[1]))
    if(exp[0]=='+'):
        res=7+int(exp[1])
    if(exp[0]=='-'):
        res=7-int(exp[1])
    
    return res

def eight(exp= -1):
    res=0
    if(exp==-1):
        return '8'
    if(exp[0]=='*'):
        res=8*int(exp[1])
    if(exp[0]=='/'):
        res=int(8/int(exp[1]))
    if(exp[0]=='+'):
        res=8+int(exp[1])
    if(exp[0]=='-'):
        res=8-int(exp[1])
    
    return res

def nine(exp= -1):
    res=0
    if(exp==-1):
        return '9'
    if(exp[0]=='*'):
        res=9*int(exp[1])
    if(exp[0]=='/'):
        res=int(9/int(exp[1]))
    if(exp[0]=='+'):
        res=9+int(exp[1])
    if(exp[0]=='-'):
        res=9-int(exp[1])
    
    return res

def plus(num):
    return '+'+num
def minus(num):
    return '-'+num
def times(num):
    return '*'+num
def divided_by(num):
    return '/'+num


print(seven(times(five())))