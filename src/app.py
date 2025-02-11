import sys
import os
from PyQt6.QtWidgets import QApplication
from star_teller.controller.controller import StarTeller
from PyQt6.QtGui import QIcon

def main() -> None:
    # Create one instance of a QApplication
    app = QApplication(sys.argv)
    
    # Set up the app's icon
    app.setWindowIcon(QIcon("resources/icons/star.png"))

    window = StarTeller()
    window.show()
    
    # Start event loop and exits cleanly
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
