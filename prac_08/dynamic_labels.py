"""
CP1404 Prac 8
Dynamic labels exercise
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamic labels app"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Bob", "Jerry", "Ben", "Zoe", "Margaret"]

    def build(self):
        """Build the kivy app from the kv file"""
        self.title = "Dynamic labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.display_labels()
        return self.root

    def display_labels(self):
        """Creates labels from list of names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
