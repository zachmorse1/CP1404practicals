"""CP1404/CP5632 Practical - Silver service taxi class"""


from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Repesent a Sil Service Taxi"""ver
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a SilverServiceTaxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Returns a string representation of a silver taxi service"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
