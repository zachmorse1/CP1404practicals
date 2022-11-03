CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Stores details about guitars."""
    def __init__(self, name, year, cost):
        """Creates a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns details of guitar in a string."""
        return f"{self.name},{self.year},{self.cost:,.2f}"

    def get_age(self):
        """Determines age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if a guitar is vintage (over 50 years old)."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting guitars by year."""
        return self.year < other.year


