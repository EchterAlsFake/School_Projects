
import sys
import time
from PySide6.QtSpatialAudio import QAudioEngine
from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QFont

class ApoRedsBombenPrank(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:red")
        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 50))
        print(f"Executiong dountdown")
        self.countdown()

    def countdown(self):
        while True:
            i = 10
            print("Setting text...")
            self.label.setText(f"Ihr PC wird in {i} Sekunden explodieren")
            time.sleep(1)
            i -= 1



app = QApplication(sys.argv)
fenster = ApoRedsBombenPrank()
fenster.showMaximized()
sys.exit(app.exec())