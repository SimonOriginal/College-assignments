"""
https://github.com/SimonOriginal

Описати клас, що реалізовує вказаний нижче тип даних. Клас повинен містити конструктор та 
подані нижче операції над об‘єктами (обов‘язково операції порівняння та привласнення) з 
використанням перевантаження операцій. 
Написати програму, яка демонструє роботу з об‘єктами цього класу. 
Програма повинна містити меню для перевірки усіх методів цього класу і операцій.
"""


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    while True:
        print("Виберіть операцію:")
        print("1. Додавання векторів")
        print("2. Векторний добуток двох векторів")
        print("3. Порівняйте два вектори")
        print("4. Додавання векторів на місці")
        print("5. Вийти")

        choice = int(input("> "))

        if choice == 1:
            result = v1 + v2
            print(f"{v1} + {v2} = {result}")
        elif choice == 2:
            result = v1 * v2
            print(f"{v1} x {v2} = {result}")
        elif choice == 3:
            if v1 == v2:
                print(f"{v1} дорівнює {v2}")
            elif v1 < v2:
                print(f"{v1} коротше ніж {v2}")
            elif v1 > v2:
                print(f"{v1} довше ніж {v2}")
        elif choice == 4:
            v1 += v2
            print(f"{v1} += {v2} => {v1}")
        elif choice == 5:
            break
        else:
            print("Невірний вибір. Спробуйте знову.")


# основная часть программы
while main():
    pass  # повторять цикл пока пользователь не выберет выход из программы
