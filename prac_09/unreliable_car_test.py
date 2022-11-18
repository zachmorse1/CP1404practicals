from prac_09.unreliable_car import UnreliableCar


def main():
    """test unreliable cars"""
    subie = UnreliableCar(name="Subaru", fuel=100, reliability=50)
    beamer = UnreliableCar(name="BMW", fuel=50, reliability=20)
    print(subie.drive(distance=80))
    print(subie)
    print(beamer.drive(distance=50))
    print(beamer)


main()
