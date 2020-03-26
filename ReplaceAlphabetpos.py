def alphabet_position(text):
    return " ".join(map(str,[ord(x.upper())-64 for x in text if(x.isalpha())]))

print(alphabet_position("The sunset sets at twelve o' clock."))