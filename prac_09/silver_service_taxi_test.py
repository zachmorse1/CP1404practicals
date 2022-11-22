from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Silver Service Taxi test"""
    taxi1 = SilverServiceTaxi(name="taxi1", fuel=100, fanciness=2)
    taxi1.drive(18)
    print(taxi1)
    print(taxi1.get_fare())


main()
