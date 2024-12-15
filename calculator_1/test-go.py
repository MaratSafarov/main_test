import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLCDNumber, QGridLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса QMainWindow
        self.setWindowTitle("Калькулятор LCD") # Устанавливаем заголовок окна
        self.setGeometry(100, 100, 390, 585) # Устанавливаем размер и положение окна: (x, y, ширина, высота)
        self.central_widget = QWidget() # Создаем центральный виджет, который будет содержать другие элементы интерфейса
        self.setCentralWidget(self.central_widget) # Устанавливаем центральный виджет для основного окна
        self.setStyleSheet(
            "background-color: rgb(38, 38, 38);")  # Задаем стиль для главного окна (цвет фона: темно-серый)

        self.lcd = QLCDNumber() # Создаем LCD экран
        self.lcd.setStyleSheet("background-color: rgb(0, 208, 100);")


        self.layout = QVBoxLayout() # Создаем вертикальный макет
        self.layout.addWidget(self.lcd) # Добавляем LCD экран в вертикальный макет


        self.create_buttons() # Создаем клавиши (метод, который добавляет кнопки в интерфейс)
        self.central_widget.setLayout(self.layout) # Устанавливаем созданный вертикальный макет как основной для центрального виджета


        self.current_input = "" # Переменная для хранения текущего ввода

    def create_buttons(self):
        grid = QGridLayout() # Создаем объект QGridLayout для организации кнопок в виде сетки
        buttons = [
            (self)
        ]

        self.button_sub = QPushButton(self.window)  # Создаем кнопку для вычитания и помещаем ее в основное окно (self.window)
        self.button_sub.setGeometry(QtCore.QRect(280, 300, 71,
                                                 71))  # Устанавливаем геометрию кнопки: позиция (x=280, y=300) и размер (ширина=71, высота=71)
        font = QtGui.QFont()  # Создаем объект шрифта для кнопки
        font.setPointSize(30)  # Устанавливаем размер шрифта на 30 пунктов
        self.button_sub.setFont(font)  # Применяем шрифт к кнопке
        self.button_sub.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")  # Задаем стиль для кнопки: цвет фона (RGB 0, 208, 100) и цвет текста (белый)
        self.button_sub.setObjectName(
            "button_sub")  # Устанавливаем уникальное имя для кнопки, которое можно использовать для идентификации

        for text, x, y in buttons: # Предполагается, что buttons - это список кортежей, где каждый кортеж содержит текст кнопки и её координаты (x, y)
            button = QPushButton(text) # Создаем кнопку с текстом, указанным в переменной text
            button.clicked.connect(lambda checked, t=text: self.on_button_clicked(t)) # Подключаем сигнал clicked кнопки к функции on_button_clicked
                    # Используем лямбда-функцию, чтобы передать текст кнопки в функцию
            grid.addWidget(button, x, y) # Добавляем кнопку в сетку (grid) в позиции (x, y)

        self.layout.addLayout(grid) # Добавляем сетку (grid) в основной layout (раскладку) интерфейса

    def on_button_clicked(self, button_text):
        if button_text == 'C': # Если нажата кнопка "C" (очистить)
            self.current_input = ""  # Сбрасываем текущий ввод
            self.lcd.display(0)  # Отображаем 0 на LCD экране
        elif button_text == '=': # Если нажата кнопка "=" (вычислить)
            try:
                result = eval(self.current_input) # Пытаемся вычислить выражение, хранящееся в current_input
                self.lcd.display(result)  # Отображаем результат на LCD экране
                self.current_input = str(result)  # Обновляем текущее значение на результат
            except Exception:
                self.lcd.display("Ошибка") # Если произошла ошибка (например, синтаксическая ошибка), отображаем "Ошибка"
                self.current_input = ""  # Сбрасываем текущий ввод
        else: # Для всех остальных кнопок (цифры и операции)
            self.current_input += button_text  # Добавляем текст кнопки к текущему вводу
            self.lcd.display(self.current_input)  # Обновляем LCD экран, показывая текущий ввод


if __name__ == '__main__':  # Проверяем, выполняется ли этот файл как основная программа
    app = QApplication(sys.argv)  # Создаем экземпляр QApplication, который управляет основным потоком событий приложения
    calculator = Calculator()  # Создаем экземпляр класса Calculator, представляющий интерфейс калькулятора
    calculator.show()  # Отображаем окно калькулятора на экране
    sys.exit(app.exec_())  # Запускаем главный цикл обработки событий приложения и завершаем программу при выходе
