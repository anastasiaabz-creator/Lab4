while True:
    text = input("Введіть текст: ")

    # Якщо ввели порожній рядок (просто натиснули Enter), виходимо з циклу
    if not text:
        break

    result = []
    seen = set()

    for char in text:
        if char == " ":
            continue
        # Додаємо символ, якщо він ще не зустрічався
        if char not in seen:
            seen.add(char)
            result.append(char)

    print("".join(result))
