# # Калькулятор
# # Создайте класс, где реализованы функции (методы)
# # математических операций. А также функции, для ввода данных.

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return a + b

    def minus(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


while True:

    sign = input('Введите Знак(+, -, *, /, 0 -exit ): ')
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/'):
        a = (int(input('Введите первое число: ')))
        b = (int(input('Введите второе число: ')))

        calculator_obj = Calculator(a, b)
    if sign == '+':
        calculator_obj.sum()
        print(calculator_obj.sum())
    elif sign == '-':
        calculator_obj.minus()
        print(calculator_obj.minus())
    elif sign == '*':
        calculator_obj.multiplication()
        print(calculator_obj.multiplication())
    elif sign == '/':
        try:
            print(calculator_obj.division())
        except ZeroDivisionError:
            print('На 0 делить нельзя!')
