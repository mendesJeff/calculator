import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget

from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Definiindo padrões da Janela
        self.setWindowTitle("Luli's calculator")
        self.setFixedSize(350, 400)

        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)
        self.display = QLineEdit()

        # Criando o Display
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px}')

        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Chamando os botões
        self.create_button(QPushButton('DEL'), 2, 4, 1, 1,
                           lambda: self.display.setText(''), 'red')
        self.create_button(QPushButton('<-'), 3, 4, 1, 1,
                           lambda: self.display.setText(self.display.text()[:-1]))
        self.create_button(QPushButton('/'), 4, 4, 1, 1)
        self.create_button(QPushButton('7'), 2, 0, 1, 1, None, 'number')
        self.create_button(QPushButton('8'), 2, 1, 1, 1, None, 'number')
        self.create_button(QPushButton('9'), 2, 2, 1, 1, None, 'number')
        self.create_button(QPushButton('*'), 2, 3, 1, 1)
        self.create_button(QPushButton('4'), 3, 0, 1, 1, None, 'number')
        self.create_button(QPushButton('5'), 3, 1, 1, 1, None, 'number')
        self.create_button(QPushButton('6'), 3, 2, 1, 1, None, 'number')
        self.create_button(QPushButton('-'), 3, 3, 1, 1)
        self.create_button(QPushButton('3'), 4, 0, 1, 1, None, 'number')
        self.create_button(QPushButton('2'), 4, 1, 1, 1, None, 'number')
        self.create_button(QPushButton('1'), 4, 2, 1, 1, None, 'number')
        self.create_button(QPushButton('+'), 4, 3, 1, 1)
        self.create_button(QPushButton('+/-'), 5, 0, 1, 1)
        self.create_button(QPushButton('0'), 5, 1, 1, 1,  None, 'number')
        self.create_button(QPushButton('.'), 5, 2, 1, 1)
        self.create_button(QPushButton('='), 5, 3, 1, 2,
                           self.result, 'equal')

    def create_button(self, button, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(button, row, col, rowspan, colspan)

        if style == 'red':
            button.setStyleSheet(
                '* {background: rgba(255, 10, 10, 0.8); color: white; font-size: 20px; font-weight: bold}')

        elif style == 'number':
            button.setStyleSheet(
                '*{background: rgba(100, 100, 100, 0.8); color: white; font-size: 30px}')

        elif style == 'equal':
            button.setStyleSheet(
                '*{background: rgba(10, 10, 255, 0.8); color: white; font-size: 40px}')

        if not function:
            button.clicked.connect(lambda: self.display.setText(
                self.display.text() + button.text()))
        else:
            button.clicked.connect(function)

        button.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

    def result(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )

        except Exception as error:
            print(f'Error: {error}')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
