import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QComboBox, QSlider, \
    QPushButton
from PyQt5.QtCore import Qt


class Radiodemo(QWidget):

    def __init__(self, parent=None):
        super(Radiodemo, self).__init__(parent)

        self.funkcje = ["3x^2 + 5x -8", "-2x^3 + 7x - 2"]

        self.cb = QComboBox()
        self.cb.addItems(self.funkcje)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(-100, 100)
        self.sliderValue = QLabel('0')
        self.slider.valueChanged.connect(self.updateLabel)
        self.sliderValue.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.etap = 0
        self.metoda = "brak"
        self.stop = "brak"
        self.funkcja = "brak"
        self.poczatek = 0
        self.koniec = 0
        self.wybor = "Metoda bisekcji"
        self.iteracje = 0
        self.dokladnosc =0.0

        self.layout = QVBoxLayout()

        self.label = QLabel("Wybierz metodę")
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.label)

        self.b1 = QRadioButton("Metoda bisekcji")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        self.layout.addWidget(self.b1)

        self.b2 = QRadioButton("Metoda złotego podziału")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        self.layout.addWidget(self.b2)
        self.setLayout(self.layout)
        self.setWindowTitle("Wybór metody")

        self.next = QPushButton('OK')
        self.next.clicked.connect(self.myfunc)
        self.layout.addWidget(self.next)

    def btnstate(self, b):

        if (b.isChecked()):
            self.wybor = b.text()

    def myfunc(self):

        if self.etap == 0:
            self.etap += 1
            self.metoda = self.wybor
            self.label.setText("Wybierz warunek stopu")
            self.b1.setText("Ilość iteracji")
            self.b1.setChecked(True)
            self.b2.setText("Dokładność")
            self.wybor = "Ilość iteracji"

        elif self.etap == 1:
            self.etap += 1
            self.stop = self.wybor
            self.label.setText("Wybierz funkcję testową")
            self.layout.removeWidget(self.b1)
            self.layout.removeWidget(self.b2)
            self.layout.removeWidget(self.next)
            self.b1.deleteLater()
            self.b2.deleteLater()
            self.layout.addWidget(self.cb)
            self.layout.addWidget(self.next)

        elif self.etap == 2:
            self.etap += 1
            self.funkcja = self.cb.currentText()
            self.label.setText("Wybierz początek przedziału")
            self.layout.removeWidget(self.cb)
            self.layout.removeWidget(self.next)
            self.cb.deleteLater()
            self.layout.addWidget(self.slider)
            self.layout.addWidget(self.sliderValue)
            self.layout.addWidget(self.next)
        elif self.etap == 3:
            self.etap += 1
            self.poczatek = self.slider.value()
            self.label.setText("Wybierz koniec przedziału")
            self.slider.setRange(self.poczatek + 1, self.poczatek + 100)

        elif self.etap == 4:
            self.etap += 1
            self.koniec = self.slider.value()
            if self.stop == "Ilość iteracji":
                self.slider.setRange(1, 50)
                self.label.setText("Wybierz ilość iteracji")
            else:
                self.label.setText("Wybierz dokładność")
                self.slider.setRange(0, 100)
                self.slider.setValue(50)
                self.sliderValue.setText('0.5')
                self.slider.valueChanged.connect(self.updateLabelFloat)


        elif self.etap == 5:
            if self.stop == "Ilość iteracji":
                self.iteracje = self.slider.value()
            else:
                self.dokladnosc = self.slider.value() / 100.0

            if self.metoda == "Metoda bisekcji":
                self.bisekcja()
            else:
                self.zlotyPodzial()

    def updateLabel(self, value):
        self.sliderValue.setText(str(value))

    def updateLabelFloat(self, value):
        self.sliderValue.setText(str(value/100.0))

    def bisekcja(self):
        print("bi")

    def zlotyPodzial(self):
        print("gold")


def main():
    app = QApplication(sys.argv)
    ex = Radiodemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
