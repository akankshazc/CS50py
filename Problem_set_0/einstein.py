# input from the user in kg (integer)
x = input("how many kgs you want to convert to energy \n")

# function that outputs the energy from the mass (in joules)


def einstein(x):
    Energy = int(x) * 9 * 10**16
    return Energy


print(einstein(x))
