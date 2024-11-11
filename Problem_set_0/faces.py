# user input
x = input('give me them emoticons\n')

# a function called convert that acccepts a string as input and returns the same input with :) converted to emojis


def convert(x):
    # to detect if the input has emoticons
    if ":)" in x:
        # replacing them
        # breaking the string by the emoticon position
        y = x.split(':)')
        # joining the string back with emoji
        z = '🙂'.join(y)
    else:
        z = x
    if ":(" in z:
        a = z.split(':(')
        b = '🙁'.join(a)
    else:
        b = z
    return b


print(convert(x))
