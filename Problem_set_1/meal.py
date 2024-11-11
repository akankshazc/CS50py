# asking the time
x = input("what time is it?\n")

# formatting the time
y = x.split(":")
a, b = int(y[0]), int(y[1])
# print(a, b)

# what to eat
if a == 7:
    print("breakfast time")
elif a == 8 and b == 00:
    print("breakfast time")

if a == 12:
    print("lunch time")
elif a == 13 and b == 00:
    print("lunch time")

if a == 18:
    print("dinner time")
elif a == 19 and b == 00:
    print("dinner time")
