venues = {0: "Now, you are relaxing in front of a screen learning Python",
          1: "Now, you are standing at the end of a road before a small brick building",
          2: "Now, you are at the top of a hill",
          3: "Now, you are inside a building, a well house for a small stream",
          4: "Now, you are in a valley beside a stream",
          5: "Now, you are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(venues[loc])

    if loc == 0 or loc == "zero".casefold():
        print("Thank you for playing this adventure game!")
        break

    direction = input("The available exits are " + available_exits + " ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Sorry, you cannot exit in this direction / there is no such direction.")
