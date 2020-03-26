def narcissistic( value ):
    p=len(str(value))
    temp=value
    num=0
    while(value>0):
        digit= value%10
        num=num+digit**p
        value=value/10
    print("{}={}".format(temp,num))
    return True if(temp==num) else False

print(narcissistic(7))