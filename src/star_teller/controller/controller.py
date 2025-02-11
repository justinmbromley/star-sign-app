import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

from star_teller.core.star_sign import star_sign

class StarTeller(QWidget):
    def __init__(self) -> None:
        # Initialising the QWidget
        super().__init__()
        # super(StarTeller, self).__init__()
        
        # set up the window title
        self.setWindowTitle("Star Teller")

        # Linking to the ui
        uic.loadUi("ui/star_teller.ui", self)

        self.button_get_star_sign.clicked.connect(self.get_star_sign)

    def get_star_sign(self):
        day = self.line_day.text()
        month = self.line_month.text()
        year = self.line_year.text()
        result = star_sign(year, month, day)
        self.label_star_sign.setText(result)
