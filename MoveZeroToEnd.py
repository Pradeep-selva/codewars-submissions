def move_zeros(array):
    main=[]
    zero=[]
    for i in array:
        if(i==0 and (str(i)=='0' or str(i)=='0.0')):
            zero.append(i)
        else:
            main.append(i)
    
    return main+zero

print(move_zeros([3, 'z', -2, -5, -2, -5, False, 2, 'b', 8, 1, 'x', 0, 0, 0, 0, 0, 0, '0'] ))
print(str(False))