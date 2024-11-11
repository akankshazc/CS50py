# ask for input
x = input("greet me\n")

# check for greeting
if x.strip().lower() == "hello":
    print("$0")
elif x.strip().lower()[0] == "h":
    print("$20")
else:
    print("$100")
