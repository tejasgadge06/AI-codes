 
rooms = {
    "A": "Dirty",
    "B": "Dirty",
}

location = "A"

while True:
    if location == "A":
        print("Agent is in Room A")
        print("Status of Room A:", rooms["A"])

        if rooms["A"] == "Dirty":
            print("Action: Suck")
            rooms["A"] = "Clean"

        print("Action: Move Right")
        location = "B"

    elif location == "B":
        print("Agent is in Room B")
        print("Status of Room B:", rooms["B"])

        if rooms["B"] == "Dirty":
            print("Action: Suck")
            rooms["B"] = "Clean"

        if rooms["A"] == "Clean" and rooms["B"] == "Clean":
            print("\nBoth rooms are clean")
            print("Action: No-op")
            break
