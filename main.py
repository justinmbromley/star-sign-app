import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6 import uic

from src.star_teller import star_sign

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('star_sign.ui', self)
        self.setWindowTitle("Star Teller")

        self.button_get_star_sign.clicked.connect(self.get_star_sign)
        
    def get_star_sign(self):
        day = self.line_day.text()
        month = self.line_month.text()
        year = self.line_year.text()

        print(f"Day: {day}")
        print(f"Month: {month}")
        print(f"Year: {year}")

        result = star_sign(year, month, day)
        print(f"This is the {result}")

        self.label_star_sign.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())