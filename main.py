import random

points = {
    "comp": 0,
    "player": 0
}

words = ["дом", "кошка", "собака", "машина", "игра"]

def is_odd(number: int):
    if number % 2 == 0:
        return False
    else:
        return True

while True:
    a = random.randint(10, 120)
    if is_odd(a):
        continue
    b = random.randint(10, 120)
    if is_odd(b):
        continue
    op = random.choice(("+", "-"))
    if op == "+":
        ans = a+b
        user = input(f"{a} + {b} = ")
    else:
        ans = a - b
        user = input(f"{a} - {b} = ")
    if user == str(ans):
        print("Верно!")
        points["player"] += 1
    else:
        print("Ты ошибся! Попробуй еще раз!")
        points["comp"] += 1
    print(f'Счет: {points["player"]}:{points["comp"]}')
