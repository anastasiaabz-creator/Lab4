def format_text(max_len: int, text: str):
    words = text.split()
    current_line = []
    current_length = 0

    for word in words:
        added_len = len(word) if not current_line else len(word) + 1

        if current_length + added_len <= max_len:
            current_line.append(word)
            current_length += added_len
        else:
            print(" ".join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        print(" ".join(current_line))

while True:
    limit_input = input("Введіть m: ")

    if not limit_input:
        break

    max_len = int(limit_input)
    text = input("Введіть текст: ")

    format_text(max_len, text)
    print()



