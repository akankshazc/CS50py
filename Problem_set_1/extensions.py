# have a list of all inputs
x = {'.gif': "image/gif", '.jpg': "image/jpeg", '.jpeg': "image/jpeg", '.png': "image/png",
     '.pdf': "application/pdf", '.txt': "text/plain", '.zip': "application/zip"}

# ask for inputs
y = input("give file name\n")

# check if the format is in the list and which one


def extensions(y):
    for format in x.keys():
        if format in y.lower():
            return print(x[format])
    return print("application/octet-stream")


extensions(y)
