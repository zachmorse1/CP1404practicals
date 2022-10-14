COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "banana yellow": "#ffe135", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                  "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

colour_code = input("Enter colour code: ").lower()
while colour_code != "":
    try:
        print(colour_code, "is", COLOUR_TO_CODE[colour_code])
    except KeyError:
        print("Invalid code")
    colour_code = input("Enter colour code: ").lower()
