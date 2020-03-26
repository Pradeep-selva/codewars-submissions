def is_isogram(string):
    return True if sorted(list(set(string.lower())))==sorted(list(string.lower())) else False

print(is_isogram("Dermatoglyphics"))
