taco = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


def taqueria(tdict):
    cost = 0
    while True:

        try:
            x = input("give your order\n").lower()
            cost = cost + tdict[x]
            print("Total: $", cost)
        except EOFError:
            return print(cost)
        except KeyError:
            continue


taqueria(taco)
