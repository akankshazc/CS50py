def fuel():

    x = input("give me a fraction?\n")

    try:
        y = x.split("/")
        z = round((int(y[0]) / int(y[1])) * 100)

        if z < 1:
            return print("E")
        elif z > 99:
            return print("F")
        else:
            return print(z, "%")
    except ValueError:
        x = input("give me a fraction?\n")
        fuel()
    except ZeroDivisionError:
        x = input("give me a fraction?\n")
        fuel()


fuel()
