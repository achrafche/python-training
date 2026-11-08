seen_space = False
text = input("Text: ")
for c in text:
    if c.isspace():
        seen_space = True
print(seen_space)