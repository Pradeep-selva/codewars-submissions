def spin_words(sentence):
    return " ".join(["".join(list(reversed(x))) if len(x)>=5 else x for x in sentence.split() ])

print(spin_words("Hey wollef sroirraw"))