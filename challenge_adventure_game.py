venues = {0: {"desc": "You are now sitting in front of a screen learning Python",
              "exits": {},
              "named_exits": {}},
          1: {"desc": "You are now standing at the end of a road before a small brick building",
              "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
              "named_exits": {"2": 2, "3": 3, "5": 5, "4": 4, "0": 0}},
          2: {"desc": "You are now at the top of a hill",
              "exits": {"N": 5, "Q": 0},
              "named_exits": {"5": 5, "0": 0}},
          3: {"desc": "You are now inside a building, a well house for a small stream",
              "exits": {"W": 1, "Q": 0},
              "named_exits": {"1": 1, "0": 0}},
          4: {"desc": "You are now in a valley beside a stream",
              "exits": {"N": 1, "W": 2, "Q": 0},
              "named_exits": {"1": 1, "2": 2, "0": 0}},
          5: {"desc": "You are now in a forest",
              "exits": {"W": 2, "S": 1, "Q": 0},
              "named_exits": {"2": 2, "1": 1, "0": 0}}
          }

user_input = {"QUIT":  "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST":  "E",
              "WEST":  "W".upper()}

loc = 1
while True:
    available_exits = ", ".join(venues[loc]["exits"].keys())
    print(venues[loc]["desc"])

    if loc == 0:
        print("Thank you for playing this adventure game, maybe next time!")
        break
    else:
        all_exits = venues[loc]["exits"].copy()
        all_exits.update(venues[loc]["named_exits"])

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
