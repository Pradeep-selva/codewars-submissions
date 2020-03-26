def is_valid_walk(walk):
    v,h=(0,0)
    distance=0
    for i in walk:
        if(i=='n'):
            v+=1
            distance+=1
        elif(i=='s'):
            v-=1
            distance+=1
        elif(i=='w'):
            h-=1
            distance+=1
        else:
            h+=1
            distance+=1
    
    return True if(distance==10 and v==0 and h==0) else False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
    