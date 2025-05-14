import sys
from PyQt6.QtWidgets import QApplication
from controllers.controller import StarTeller
from PyQt6.QtGui import QIcon
from resource_pkg.resource import resource_path


def main() -> None:
    # Create one instance of a QApplication
    app = QApplication(sys.argv)

    # Set up the app's icon
    # app.setWindowIcon(QIcon(resource_path("../../resources/icons/star.png")))
    app.setWindowIcon(QIcon("src/star_teller/resources/icons/star.png"))

    window = StarTeller()
    window.show()

    # Start event loop and exits cleanly
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
