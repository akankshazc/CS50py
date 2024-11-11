
grocery = {}
while True:
    try:
        x = input("give grocery items\n").upper()
        if x in grocery.keys():
            grocery[x] += 1
        else:
            grocery[x] = 1

    except EOFError:
        break

for y in grocery.keys():
    print(grocery[y], y)
