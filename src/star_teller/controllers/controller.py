from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from core.star_sign import star_sign

from pathlib import Path
import sys, os


class StarTeller(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Star Teller")

        # Adjust UI file path when running on
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            ui_path = os.path.join(sys._MEIPASS, "ui", "star_teller.ui")
        else:
            base_path = os.path.dirname(__file__)
            ui_path = os.path.join(base_path, "..", "ui", "star_teller.ui")

        uic.loadUi(ui_path, self)

        self.button_get_star_sign.clicked.connect(self.get_star_sign)

    def get_star_sign(self):
        day = self.line_day.text()
        month = self.line_month.text()
        year = self.line_year.text()
        result = star_sign(year, month, day)
        self.label_star_sign.setText(result)
