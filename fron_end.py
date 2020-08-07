from PyQt5.QtWidgets import QLabel, QWidget, QApplication
from PyQt5.QtCore import Qt
import numpy as np
import sys
import parametros as pm

class PaintLabel(QLabel):

    def __init__(self,letra,*args):
        super().__init__('round label', *args)
        self.setText(letra)
        self.setAlignment(Qt.AlignCenter)
        self.estado = "white"

    def mousePressEvent(self, QMouseEvent):
        if self.estado == "white":
            self.setStyleSheet('background-color: green; border-radius: 20px;')
            self.estado = "green"

        elif self.estado == "green":
            self.setStyleSheet('background-color: red; border-radius: 20px;')
            self.estado = "red"
        elif self.estado == "red":
            self.estado = "yellow"
            self.setStyleSheet('background-color: #f5dd29; border-radius: 20px;')

        elif self.estado == "yellow":
            self.estado = "white"
            self.setStyleSheet('background-color: rgb 0 0 0 0; '
                               'border-radius: 20px;'
                               'border: 2px solid blue')


class MainWindow(QWidget):
    def __init__(self,*args):
        super().__init__(*args)
        self.letras = {}
        self.author = QLabel(self)
        self.author.setText('Author cncosta')
        self.author.move(0,0)
        self.setWindowTitle('Pasapalabra')
        self.setFixedSize(430,430)


        for i in pm.letras:
            self.letras.update({i: PaintLabel(i,self)})
        self.set_up()

    def set_up(self):
        i = 0
        theta = 2 * np.pi / len(self.letras)
        for label in self.letras.values():
            label.resize(40, 40)
            label.setStyleSheet("border: 2px solid blue; "
                                "border-radius: 20px;")
            angle = theta * (i)
            dx = int(round(200 + 165 * np.cos(angle - np.pi/2)))
            dy = int(round(200 + 165 * np.sin(angle - np.pi/2)))
            label.move(dx,dy)
            i += 1



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    a = QApplication(sys.argv)
    ventana_inicial = MainWindow()
    ventana_inicial.show()
    sys.exit(a.exec())
