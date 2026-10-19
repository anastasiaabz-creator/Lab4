def check_brackets_balance(expr: str):
    balance = 0

    for char in expr:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

text = input("Введіть вираз: ")
print(check_brackets_balance(text))

