def split(word):
    return list(word)

def longest(s1, s2):
    return "".join(sorted(list(set(split(s1)+split(s2)))))

print(longest("aretheyhere", "yestheyarehere"))