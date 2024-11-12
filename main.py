from PyQt6.QtWidgets import QApplication, QWidget
from main_window import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__name__":
    main()