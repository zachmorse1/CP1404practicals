"""
CP1404 - Prac 6
Estimate - 30 minutes
Actual time taken - 20 minutes

"""

from guitar import Guitar


def main():
    """Guitar program."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("\nName: ")
    display_guitars(guitars)


def display_guitars(guitars):
    """Displays guitars."""
    if guitars:
        print("\n... snip ...\n")
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    else:
        print("No guitars!")


main()
