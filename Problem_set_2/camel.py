import re

# prompting the user for the name of the variable in camel case
x = input("give your camel name? \n")

# a function that takes camel case as input and returns snake case


def snake_case(str):
    # creating a list for all the camel words
    camel_list = []

    # adding the first lower case word in camel
    for char in str:
        if (char.isupper()):
            y = str.index(char)
            camel_list.append(str[:y])
            break

    # making another list of all the upper case words
    camel_list_2 = re.findall('[A-Z][^A-Z]*', str)

    # appending the words to the camel list in lower case
    for c in camel_list_2:
        camel_list.append(c.lower())

    # making the snake string
    return '_'.join(camel_list)


print(snake_case(x))
