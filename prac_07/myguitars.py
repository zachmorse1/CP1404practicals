"""
CP1404 - Prac 7
Estimate - 15 minutes
Actual time taken - 20 minutes

"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    # test = Guitar("Fender Stratocaster", 2014, 765.4)
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
        guitars.sort()
        for guitar in guitars:
            print(guitar)


main()
