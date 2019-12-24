from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from app.CompetitorColorEnum import CompetitorColorEnum


class CompetitorLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, label_color, font):
        QLabel.__init__(self)
        self.setStyleSheet("border: 2px solid " + label_color + " outset;"
                                                                "background-color: white;")
        self.setFont(font)
        self.setMaximumSize(QtCore.QSize(564, 16777215))
        self.setObjectName("competitor_aka_label") \
            if label_color == CompetitorColorEnum.aka.value \
            else self.competitor_shiro_label.setObjectName("competitor_shiro_label")
        self.__init_default_values()

    def __init_default_values(self):
        self.setMaximumSize(QtCore.QSize(564, 16777215))
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setIndent(15)

    def mousePressEvent(self, q_mouse_event):
        self.clicked.emit()
