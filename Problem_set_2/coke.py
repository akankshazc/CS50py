
y = 50

while y > 0:
    x = int(input("Insert coin:\n"))
    if x == 25 or x == 10 or x == 5:
        y = y - x
    print("Amount Due:", y)

if y == 0:
    print("Change owed: ", y)

if y < 0:
    print("Change Owed:", -y)
