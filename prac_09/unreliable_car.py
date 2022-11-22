""""CP1404/CP5632 Practical - Unreliable car class"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an unreliable car object"""
    def __init__(self, reliability: float, **kwargs):
        """Initializes an unreliable car"""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive unreliable car a passed distance"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        return super().drive(distance)

