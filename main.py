# Завдання "Історія відвідувань": Створіть програму, що відтворює
# історію відвідувань веб-сторінок. Кожна нова відвідана сторінка
# додається до стеку. Можна реалізувати можливість "повернутися" до
# попередньої сторінки за допомогою видалення з вершини стеку.

class WebHistory:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def visit_page(stack, page):
    stack.push(page)
    print(f'Відвідано сторінку: {page}')
    print(f'Історія відвідувань:\n{stack.items}\n')


def back_page(stack):
    if not stack.is_empty():
        prev_page = stack.pop()
        print(f'Повернення до попередньої сторінки: {prev_page}')
        print(f'Історія відвідувань:\n{stack.items}\n')
    else:
        print('Немає попередніх сторінок для повернення.\n')


def main():
    history = WebHistory()

    visit_page(history, 'google.com')
    visit_page(history, 'github.com')
    back_page(history)
    visit_page(history, 'uakino.com')
    back_page(history)
    back_page(history)


if __name__ == '__main__':
    main()


# калькулятор
class Calculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise ValueError("Порожній стек")
        return self.stack.pop()

    def evaluate_postfix(self, postfix):
        for token in postfix.split():
            if token.isdigit():
                self.push(int(token))
            elif token == '+':
                operand2 = self.pop()
                operand1 = self.pop()
                result = operand1 + operand2
                self.push(result)
            elif token == '-':
                operand2 = self.pop()
                operand1 = self.pop()
                result = operand1 - operand2
                self.push(result)
            elif token == '*':
                operand2 = self.pop()
                operand1 = self.pop()
                result = operand1 * operand2
                self.push(result)
            elif token == '/':
                operand2 = self.pop()
                operand1 = self.pop()
                result = operand1 / operand2
                self.push(result)
            else:
                raise ValueError("Неприпустимий маркер: {}".format(token))

        if len(self.stack) != 1:
            raise ValueError("Недійсний вираз")

        return self.pop()


calculator = Calculator()
postfix_expression = '3 4 2 1 - * +'
result = calculator.evaluate_postfix(postfix_expression)
print("Результат:", result)
