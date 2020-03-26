def find_even_index(arr):
    n=-1
    for i in range(len(arr)):
        if(sum(arr[:i])==sum(arr[i+1:])):
            n=i
            break;
    return n

print(find_even_index([0,0,0,0]))