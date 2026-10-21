import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    text = sys.stdin.read()
    lines = text.splitlines()

    non_empty = []
    for line in lines:
        if line.strip() != "":
            non_empty.append(line)

    records = read_valid(lines)

    skipped = len(non_empty) - len(records)

    averages = average_by_city(records)
    best = warmest_city(records)

    print(len(records))
    print(skipped)

    if best == "":
        print("0.0")
    else:
        value = averages[best]
        print(f"{value:.1f}")


if __name__ == "__main__":
    main()