def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile:  # Проверяем, не пуст ли pile
        box = pile.grab_a_box()  # Получаем коробку из pile
        for item in box:  # Предполагаем, что box - это итерируемый объект
            if item.is_a_box():
                pile.append(item)  # Добавляем коробку обратно в pile
            elif item.is_a_key():
                print("found the key")

def look_for_key1(box):
    for item in box:
        if item.is_a_box():
            look_for_key1(item)  # Рекурсивный вызов для вложенной коробки
        elif item.is_a_key():
            print("found the key")

def countdown(i):  # Обратный отсчет
    print(i)
    if i <= 1:  # Базовый случай
        return
    else:   # Рекурсивный случай
        countdown(i-1)
countdown(5)

def greet():
    print("Hello, " + name + "!")
def question():
    print("how are you " + name + "?")
def bye():
    print("ok bye " + name)

name = "Alex"
greet()
question()
bye()

# Факториал
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
x = 4
print(fact(x))
print(fact(5))

