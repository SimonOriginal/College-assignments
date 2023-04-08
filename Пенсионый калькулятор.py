"""
    Эта программа вычисляет примерный размер годовой пенсии, который
    Вы можете ожидать на основе текущего возраста, зарплаты и накоплений,
    с учетом процентной ставки депозита на заданный срок и автоматическим пополнением депозита на 20% годовых.
    Программа также выводит общую сумму накоплений, включая сумму, которую вы заработали на своих депозитах.
"""

def calculate_pension(deposit, monthly_addition, duration, interest_rate, inflation_rate, pension_years):
    total_duration = duration + pension_years * 12    # общий срок в месяцах
    for i in range(total_duration):
        deposit += monthly_addition    # добавляем ежемесячное пополнение
        monthly_interest = deposit * (interest_rate / 12)    # считаем проценты за месяц
        deposit += monthly_interest - (deposit + monthly_interest) * inflation_rate / 12    # вычитаем ожидаемую инфляцию
    monthly_pension = deposit / (pension_years * 12)    # считаем сумму ежемесячной пенсии
    return monthly_pension

deposit = 360000
monthly_addition = 6000
duration = 12
interest_rate = 0.146
years = 30
inflation_rate = 0.12
pension_years = 20

total_duration = years * 12
total_interest = 0

for i in range(years):
    for j in range(12):
        deposit += monthly_addition
        monthly_interest = deposit * (interest_rate / 12)
        deposit += monthly_interest - (deposit + monthly_interest) * inflation_rate / 12
        total_interest += monthly_interest
    print(f"Сумма вклада на конец {i+1}-го года: {deposit:.2f} ₴.")

total_deposit = deposit + total_interest
print(f"Сумма вклада через {years} лет с учетом инфляции: {total_deposit:.2f} ₴.")

monthly_pension = calculate_pension(deposit, monthly_addition, duration, interest_rate, inflation_rate, pension_years)
print(f"Ежемесячная пенсия на {pension_years} лет: {monthly_pension:.2f} ₴.")

input()
