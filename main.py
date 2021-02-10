import json
import sys
from PIL import Image
import io
import requests
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from yandexAPI import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('template.ui', self)
        self.setWindowTitle("Проект крутышек")

        self.yandex_api = YandexAPI()
        self.show_image()

    def show_image(self):
        bits = self.yandex_api.get_map_image()
        image = Image.open(io.BytesIO(bits))
        pixmap = image.toqpixmap()
        self.pixmap_lb.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())