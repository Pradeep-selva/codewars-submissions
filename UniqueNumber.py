def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[len(arr)-1]==arr[len(arr)-2] else arr[len(arr)-1]

print(find_uniq([ 3, 10, 3, 3, 3 ]))