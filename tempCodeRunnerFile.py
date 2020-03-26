def narcissistic( value ):
    p=len(str(value))
    temp=value
    num=0
    while(value>0):
        digit= value%10
        num=num+digit**p
        value=value/10
    return True if(temp==num) else False
