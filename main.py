# b8ac8dfb8f1f39b63c68656215fd5833a3ec0940
import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)

        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        r = random.randint(5, 200)
        qp.setBrush(QColor(255, 255, 0))
        self.x0, self.y0 = random.randint(100, 400), random.randint(100, 400)
        qp.drawEllipse(self.x0 - r // 2, self.y0 - r // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
