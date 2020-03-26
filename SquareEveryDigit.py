def square_digits(num):
    return int("".join(map(str,[x*x for x in [int(i) for i in str(num)]])))

print(square_digits(1019))