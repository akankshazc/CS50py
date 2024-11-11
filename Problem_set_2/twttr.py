x = input("well, say something?\n")
y = []
for char in x:
    if char not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        y.append(char)
z = "".join(y)
print(z)
