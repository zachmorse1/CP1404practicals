"""
CP1404 - Prac 7
Estimate - 15 minutes
Actual time taken - 20 minutes

"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r+") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    add_guitars(guitars)
    display_guitars(guitars)
    save_file(guitars)


def save_file(contents):
    """Saves file content to a file passed to it"""
    with open(FILENAME, "w", encoding="utf8") as out_file:
        for content in contents:
            print(f"{content}", file=out_file)


def add_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("\nName: ")


def display_guitars(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
