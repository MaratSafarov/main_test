def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18
gcd = euclidean_algorithm(num1, num2)
print(f"НОД({num1}, {num2}) = {gcd}")

# Рекурсия
def euclidean_algorithm_recursive(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algorithm_recursive(b, a % b)

num1 = 48
num2 = 18
gcd = euclidean_algorithm_recursive(num1, num2)
print(f"НОД({num1}, {num2}) = {gcd}")

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
print(sum([1, 2, 3, 4]))


# Сумма чисел списка
def sum_2(arr_2):
    if arr_2 == []:
        return 0
    return arr_2[0] + sum_2(arr_2[1:])  # return 1 + sum_2(arr_2[1:])
print(sum_2([1, 2, 3, 4]))
