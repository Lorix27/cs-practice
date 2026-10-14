def parse_record(line): # Единственное место, где решается, что строка негодная.
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Нужно ровно 3 поля")

    city = parts[0]
    temp_text = parts[1]
    date = parts[2]

    if city == "" or date == "":
        raise ValueError("Пустой город или дата")

    try:
        temperature = float(temp_text)
    except ValueError:
        raise ValueError("Температура не число")

    result = {}
    result["city"] = city
    result["temp"] = temperature
    result["date"] = date
    return result


def read_valid(lines): # Ловит ValueError из parse_record и пропускает плохие строки.
    records = []

    for line in lines:
        if line.strip() == "":
            continue

        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue

    return records


def average_by_city(records):
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temp"]

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

    for city in sorted(averages):
        if best is None:
            best = city
        elif averages[city] > averages[best]:
            best = city

    return best