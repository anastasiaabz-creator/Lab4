while True:
    text = input("Введіть рядок: ")

    if not text:
        break

    char = input("Введіть символ: ")

    # Шукаємо перше та останнє входження символу
    first_index = text.find(char)
    last_index = text.rfind(char)

    # Якщо символ відсутній (find повертає -1)
    if first_index == -1:
        print("missing\n")
    # Якщо символ зустрічається лише один раз
    elif first_index == last_index:
        print(f"{first_index}\n")
    # Якщо символ зустрічається декілька разів
    else:
        print(f"{first_index} {last_index}\n")

