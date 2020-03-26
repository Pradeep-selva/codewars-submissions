def find_outlier(integers):
    
    f=0
    k=0
    n=0
    for i in range(1,len(integers)-1):
        if(integers[i]%2!=0 and integers[i-1]%2==0 and integers[i+1]%2==0):
            return integers[i]
        elif(integers[i]%2==0 and integers[i-1]%2!=0 and integers[i+1]%2!=0):
            return integers[i]
    
    if((integers[0]%2)!= (integers[1]%2)):
            return integers[0]
    elif((integers[len(integers)-1]%2)!= (integers[len(integers)-2]%2)):
        return integers[len(integers)-1]
                
    return None

print(find_outlier([2,4,6,8,10,3]))