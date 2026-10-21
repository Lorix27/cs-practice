from logstats import count_levels, top_errors, format_report


def main():
    path = input().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))


if __name__ == "__main__":
    main()