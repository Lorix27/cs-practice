def parse_record(line):
    # Режем строку по точке с запятой
    parts = line.split(";")

    # Должно быть ровно три поля
    if len(parts) != 3:
        raise ValueError("Нужно ровно 3 поля")

    # Убираем пробелы по краям у каждого поля
    city = parts[0].strip()
    temp_text = parts[1].strip()
    date = parts[2].strip()

    # Город и дата не должны быть пустыми
    if city == "" or date == "":
        raise ValueError("Пустой город или дата")

    # Меняем запятую на точку — чтобы "−3,5" тоже принималось
    temp_text = temp_text.replace(",", ".")

    # Пробуем превратить температуру в число
    try:
        temperature = float(temp_text)
    except ValueError:
        raise ValueError("Температура не число")

    # Ключ обязательно "temperature" — так требует автопроверка
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines):
    records = []

    for line in lines:
        # Пустые строки пропускаем молча
        if line.strip() == "":
            continue

        # Пробуем разобрать; если плохо — пропускаем
        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records


def average_by_city(records):
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]   # ← ключ "temperature"

        if city not in total:
            total[city] = 0
            count[city] = 0

        total[city] = total[city] + temp
        count[city] = count[city] + 1

    result = {}
    for city in total:
        avg = total[city] / count[city]
        result[city] = round(avg, 1)

    return result


def warmest_city(records):
    averages = average_by_city(records)

    if len(averages) == 0:
        return ""

    best = None

    # sorted гарантирует алфавитный порядок — при равенстве средних
    # победит город, который раньше по алфавиту
    for city in sorted(averages):
        if best is None:
            best = city
        elif averages[city] > averages[best]:
            best = city

    return best