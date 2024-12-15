import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLCDNumber, QGridLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__() # Вызываем конструктор родительского класса QMainWindow
        self.setWindowTitle("Калькулятор с LCD экраном") # Устанавливаем заголовок окна
        self.setGeometry(100, 100, 300, 400) # Устанавливаем размер и положение окна: (x, y, ширина, высота)
        self.central_widget = QWidget() # Создаем центральный виджет, который будет содержать другие элементы интерфейса
        self.setCentralWidget(self.central_widget) # Устанавливаем центральный виджет для основного окна

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
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

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
