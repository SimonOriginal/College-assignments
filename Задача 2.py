#   Simon Bezruhenko
#   https://github.com/SimonOriginal

import math

# визначаємо імовірності виходу при відомому вході
p_y_given_x = [
    [0.360, 0.016, 0.012],
    [0.024, 0.360, 0.008],
    [0.016, 0.024, 0.180]
]
# обчислюємо суму імовірностей кожного входу
p_x = [sum([p_y_given_x[i][j] for j in range(len(p_y_given_x[i]))]) for i in range(len(p_y_given_x))]

# виводимо таблицю імовірностей входу та перевіряємо, чи дорівнює її сума 1
for i in range(len(p_x)):
    print(f"p(x{i}) = {p_x[i]:.2f}")
print(f"Сума імовірностей входу: {sum(p_x):.2f}")

# обчислюємо ентропію входу
H_x = -sum([p*math.log2(p) for p in p_x if p > 0])

# обчислюємо умовну ентропію виходу при відомому вході
H_y_given_x = 0
for i in range(len(p_x)):
    for j in range(len(p_y_given_x[i])):
        if p_y_given_x[i][j] > 0:
            H_y_given_x -= p_x[i] * p_y_given_x[i][j] * math.log2(p_y_given_x[i][j])

# обчислюємо середню кількість інформації, що переноситься одним символом
I_y_x = H_x - H_y_given_x

# обчислюємо швидкість передачі інформації (в Бодах)
v0 = 75  # припустимо, що швидкість передачі символів дорівнює 1 Бод
I_transmission = I_y_x * v0

# обчислюємо пропускну здатність каналу
I_max = math.log2(len(p_y_given_x[0]))
C = I_max * v0

# виводимо результати
print(f"Ентропія входу: {H_x:.4f} біт")
print(f"Умовна ентропія виходу при відомому вході: {H_y_given_x:.4f} біт")
print(f"Середня кількість інформації, що переноситься одним символом: {I_y_x:.4f} біт")
print(f"Швидкість передачі інформації: {I_transmission:.4f} Бод")
print(f"Пропускна здатність каналу: {C:.4f} Бод")

input("Натисніть Enter, щоб вийти...")
