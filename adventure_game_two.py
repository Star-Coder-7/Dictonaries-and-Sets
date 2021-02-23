venues = {0: "Now, you are relaxing in front of a screen learning Python",
          1: "Now, you are standing at the end of a road before a small brick building",
          2: "Now, you are at the top of a hill",
          3: "Now, you are inside a building, a well house for a small stream",
          4: "Now, you are in a valley beside a stream",
          5: "Now, you are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

named_exits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
               2: {"5": 5},
               3: {"1": 1},
               4: {"1": 1, "2": 2},
               5: {"2": 2, "1": 1}}

user_input = {"QUIT":     "Q",
              "NORTH":    "N",
              "SOUTH":    "S",
              "EAST":     "E",
              "WEST":     "W",
              "ROAD":     "1",
              "HILL":     "2",
              "BUILDING": "3",
              "VALLEY":   "4",
              "FOREST":   "5".upper()}

# print(venues[0].split())
# print(venues[3].split(","))
# print(' '.join(venues[0].split()))

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(venues[loc])

    if loc == 0 or loc == "":
        print("Thank you for playing this adventure game!")
        break
    else:
        all_exits = exits[loc].copy()
        all_exits.update(named_exits[loc])

    direction = input("The available exits are " + available_exits + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in user_input:
                direction = user_input[word]

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("Sorry, you cannot exit in this direction / there is no such direction.")
