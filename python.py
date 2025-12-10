import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget


class SpritRechner(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.berechnung)

    def berechnung(self):
        distance = float(self.ui.spinbox_strecke.text())
        fuel = float(self.ui.spinbox_treibstoffmenge.text())

        ergebnis = (fuel * 100) / distance
        ergebnis = round(ergebnis, 3)

        if ergebnis < 6.0:
            self.ui.label_graphics_view.setPixmap(QPixmap("car_green.svg"))
            self.ui.textBrowser.setHtml(f"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li {{ white-space: pre-wrap; }}
hr {{ height: 1px; border-width: 0; }}
li.unchecked::marker {{ content: "\2610"; }}
li.checked::marker {{ content: "\2612"; }}
</style></head><body style=" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:700; color:#26a269;">Glückwunsch!</span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Ihr Auto hat einen Verbrauch von: {ergebnis}</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">und liegt damit unter dem empfohlenen Verbrauch.</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700; color:#e66100;">Weiter so :)</span></p></body></html>
""")


        else:
            self.ui.label_graphics_view.setPixmap(QPixmap("card_red.svg"))
            self.ui.textBrowser.setHtml(f"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li {{ white-space: pre-wrap; }}
hr {{ height: 1px; border-width: 0; }}
li.unchecked::marker {{ content: "\2610"; }}
li.checked::marker {{ content: "\2612"; }}
</style></head><body style=" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; color:#a51d2d;">Schade</span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Ihr Auto hat einen Verbrauch von: {ergebnis} </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">und liegt damit über dem empfohlenen Verbrauch</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#c061cb;">Bitte ändern!</span></p></body></html>
""")













app = QApplication(sys.argv)
window = SpritRechner()
window.show()
app.exec()










