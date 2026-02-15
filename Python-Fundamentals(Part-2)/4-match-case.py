color = input("Enter a color: ")

match color:
    case "red":
        print("The color is red.")
    case "blue":
        print("The color is blue.")
    case "green":
        print("The color is green.")
    case _: # default case
        print("Unknown color.")