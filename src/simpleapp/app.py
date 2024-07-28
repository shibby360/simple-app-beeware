"""
first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def random_number(widget):
    import random as r
    widget.text = r.randint(0, 10)

class simpleapp(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box()
        
        self.button = toga.Button("New number", on_press=random_number)
        main_box.add(self.button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return simpleapp()
