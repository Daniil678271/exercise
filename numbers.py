letters = ['A', 'B', 'C', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lucky_digit = input("Счастливая цифра:")

if lucky_digit not in digits:
    print("Ошибка! Введите цифру от 0 до 9.")
    exit()

plates = []
for l1 in letters:
    for l2 in letters:
        for d1 in digits:
            for d2 in digits:
                for l3 in letters:
                    for l4 in letters:
                        if d1 == lucky_digit or d2 == lucky_digit:
                            plate = f"{l1}{l2}{d1}{d2}{l3}{l4}"
                            plates.append(plate)
print(f"Всего номеров: {len(plates)}")
print("Примеры:",",".join(plates[:5]) if plates else "Нет номеров")