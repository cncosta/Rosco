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
        self.estado = "blue"
        self.resize(40, 40)
        self.change_color()


    def mousePressEvent(self, QMouseEvent):
        if self.estado == "blue":
            self.estado = "green"

        elif self.estado == "green":
            self.estado = "red"


        elif self.estado == "red":
            self.estado = "yellow"


        elif self.estado == "yellow":
            self.estado = "blue"

        self.change_color()


    def change_color(self):
        self.setStyleSheet(f"background-color: qradialgradient(cx:0, cy:0, radius: 1 ,"
                           f"fx:0.5, fy:0.5,stop:0 white, stop:1 {self.estado});"
                           f"border-radius: 20px;")



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
            angle = theta * i
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
