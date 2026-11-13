import numpy as np

# ===== Задание 1. Создание векторов и матриц =====
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("line:", line)
print("zeros:", zeros)
print("unknown_table:")
print(unknown_table)
print("identity:")
print(identity)

# ===== Задание 2. Индексы и срезы в векторе =====
print("третий элемент:", hours[2])
print("последний элемент:", hours[-1])
print("индексы 2–5:", hours[2:6])
print("каждый второй:", hours[::2])
print("в обратном порядке:", hours[::-1])

# ===== Задание 3. Строки и столбцы таблицы =====
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("центральный фрагмент 2×2:")
print(temperatures[0:2, 1:3])

# ===== Задание 4. Прямоугольные срезы =====
matrix = np.arange(1, 26).reshape(5, 5)

print("первые три строки:")
print(matrix[:3])
print("shape:", matrix[:3].shape)

print("последние две строки:")
print(matrix[-2:])
print("shape:", matrix[-2:].shape)

print("первые два столбца:")
print(matrix[:, :2])
print("shape:", matrix[:, :2].shape)

print("строки 1–3, столбцы 2–4:")
print(matrix[1:4, 2:5])
print("shape:", matrix[1:4, 2:5].shape)

print("правый нижний блок 2×2:")
print(matrix[-2:, -2:])
print("shape:", matrix[-2:, -2:].shape)

# ===== Задание 5. Изменение массива с помощью срезов =====
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:")
print(changed_matrix)
print("matrix:")
print(matrix)

# ===== Задание 6. Изменение формы =====
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)
