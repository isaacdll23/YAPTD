from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()

        #title
        self.setWindowTitle('PDF Text Dumper')

        # fixed size
        self.setFixedHeight(100)
        self.setFixedWidth(500)

        # select source file - label
        self.label_srcfile = QLabel('Select Source File:', self)
        self.label_srcfile.move(5, 5)

        # select outfile location - label
        self.label_outfile = QLabel('Select Output Directory:', self)
        self.label_outfile.move(5, 35)

        # show all widgets
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())