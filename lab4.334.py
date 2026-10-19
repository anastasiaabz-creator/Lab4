n = int(input("Введіть число:"))

# Формуємо 5 рядків малюнка для кожної частини пінгвінів
line1 = "   ~     " * n
line2 = "  (o o)  " * n
line3 = " /  V  \\ " * n

# 4-й рядок підставляє номер пінгвіна i від 1 до n
line4 = "".join([f"/(  {i}  )\\" for i in range(1, n + 1)])

line5 = "  ^^ ^^  " * n

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)

