import json


def _cast(s: str):
    s = s.strip()
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        return s

def csv_to_records(text: str) -> list[dict]:
    lines = text.splitlines()
    if not lines:
        return []
    head = [h.strip() for h in lines[0].split(",")]
    return [
        dict(zip(head, (v.strip() for v in line.split(","))))
        for line in lines[1:]
        if line.strip()
    ]

def parse_settings(lines: list[str]) -> dict:
    res, cur = {}, None
    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- "):
            if cur is not None:
                res[cur].append(_cast(line.lstrip()[2:].strip()))
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            res[k], cur = [], k
        else:
            res[k], cur = _cast(v), None
    return res


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    return [{**extra.get(r.get(key), {}), **r} for r in rows]


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)