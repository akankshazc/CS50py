def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    y = float(d[1:])
    return y


def percent_to_float(p):
    z = float(p[:-1]) / 100
    return z


main()
