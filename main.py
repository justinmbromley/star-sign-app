import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

from src.star_teller import star_sign

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), './ui/star_sign.ui')
        uic.loadUi(ui_path, self)
        self.setWindowTitle("Star Teller")

        self.button_get_star_sign.clicked.connect(self.get_star_sign)

    def get_star_sign(self):
        day = self.line_day.text()
        month = self.line_month.text()
        year = self.line_year.text()
        result = star_sign(year, month, day)
        self.label_star_sign.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(__file__), './resources/star.png')
    app.setWindowIcon(QIcon(icon_path))
    my_app = MyApp()
    my_app.show()

    sys.exit(app.exec())
