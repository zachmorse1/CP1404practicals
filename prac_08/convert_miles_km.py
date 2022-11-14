"""
CP1404 Prac 8
Convert miles to kilometres program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KILOMETRES_CONVERSION = 1.60934


class MilesToKilometres(App):
    """App to convert miles to kilometres"""
    output = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        Window.size = (500, 200)
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self, value):
        """Handles calculation and outputs to output label"""
        self.output = str(round(self.convert_to_number(value) * MILES_TO_KILOMETRES_CONVERSION, 3))

    def handle_increment(self, old_number, value_change):
        """Handles increment of input number by up and down buttons"""
        new_number = self.convert_to_number(old_number) + value_change
        self.root.ids.input_number.text = str(new_number)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometres().run()
