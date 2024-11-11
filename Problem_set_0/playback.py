# ask the user for input
x = input("enter for fast speech\n")


# function that takes user input and does the slow playback thing
def playback(x):
    y = x.split()
    z = '...'.join(y)
    return z


print(playback(x))
