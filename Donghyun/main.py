import sys
from GANgineer_ui import Ui_GANgineer  # 수정부분
from PyQt5.QtWidgets import *


class GANgineer(QMainWindow, Ui_GANgineer):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()


app = QApplication([])
sn = GANgineer()
QApplication.processEvents()
sys.exit(app.exec_())