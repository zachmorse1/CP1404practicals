"""
CP1404 - Prac 6
Estimate - 40 minutes
Actual time taken - 30 minutes

"""

from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 20.99)
    print(gibson)
    print(another_guitar)
    print(gibson.get_age())
    print(gibson.is_vintage())
    print(another_guitar.get_age())
    print(another_guitar.is_vintage())


main()
