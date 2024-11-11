# asking the user
x = input(
    "what is the answer to the great question of life, the universe and everything?\n")

if x.lower() == "forty two" or x.lower() == "forty-two" or x == "42":
    print("Yes")
else:
    print("No")
