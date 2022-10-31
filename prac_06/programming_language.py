"""
CP1404 - Prac 6
Estimate - 20 minutes
Actual time taken - 15 minutes

"""


class ProgrammingLanguage:
    """Programming Language"""
    def __init__(self, name, typing, reflection, year):
        """Creates a Programming Language based on values passed to it"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return if a programming language is dynamic or not."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string of a Programming Language."""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
