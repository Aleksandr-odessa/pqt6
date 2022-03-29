from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget
from gen_pasw import gen
import sys


# Создаем подкласс QMainWindow что бы настраивать окно, с помощью __init__.
class MainWindow(QMainWindow):

    def button_clicked(self):

        try:
            n = self.input.text()
            generator = gen(int(n))
        except ValueError:
            self.label.setText('')
            self.labelEror.setText('Error. Please enter number')
        else:
            self.labelEror.setText('')
            # setText выводит текст f в метку
            self.label.setText(generator)
            # self.label.move(100,50)
            self.label.adjustSize()

    def __init__(self):
        # чтобы разрешить Qt настраивать объект,
        # нужно вызывать super __init__.

        super().__init__()

        # меняем заголовок главного окна
        self.setWindowTitle("Генератор паролей")
        self.label = QLineEdit(self)
        self.labelEror = QLabel()
        self.input = QLineEdit()
        self.button = QPushButton("Сгенерировать пароль")

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.labelEror)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)

        # запуск функции button_clicked при нажатии на кнопку

        self.button.clicked.connect(self.button_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

# создаём экземпляр QApplication и передаём sys.arg
# (список Python с аргументами командной строки, передаваемыми приложению):


app = QApplication(sys.argv)

# создаём экземпляр MainWindow, используя имя переменной window
window = MainWindow()
window.show()

app.exec()
