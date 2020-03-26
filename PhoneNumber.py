def create_phone_number(n):
    s= "".join(list(map(str,n)))
    return "({}) {}-{}".format(s[:3],s[3:6],s[6:])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))