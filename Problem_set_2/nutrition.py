fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew melon": 50,
          "kiwifruit": 90, "lemon": 15, "nectarine": 60, "orange": 80, "peach": 60, "pineapple": 50, "plums": 70, "strawberries": 50,
          "sweet cherries": 100, "tangerine": 50, "watermelon": 80}

x = input("give me a fruit\n").lower()

if x in fruits.keys():
    print("Calories: ", fruits[x])
