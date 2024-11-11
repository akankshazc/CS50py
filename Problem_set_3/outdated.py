month = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

# to check if the input is valid or not


def check():
    while True:
        ex = input("give me a date\n")
        if ',' in ex or '/' in ex:
            outdated(ex)
            break
        else:
            continue


def outdated(x):
    try:
        # if date in 12/13/1989 format
        if "/" in x:
            x = x.split("/")
            return print("{}-{}-{}".format(x[2], x[0], x[1]))

        # if date in december 13, 1989 format
        if "," in x:
            x = x.split()
            y = ","
            for ch in x:
                if y in ch:
                    x[x.index(ch)] = ch.replace(y, '')
            return print("{}-{}-{}".format(x[2], month[x[0]], x[1]))
    except KeyError:
        return None


check()
