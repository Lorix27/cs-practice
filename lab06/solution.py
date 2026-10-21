def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        if name.startswith(".") and name.count(".") == 1:
            ext = ""
        elif "." in name:
            ext = name.rsplit(".", 1)[-1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    if index == 0:
        return f"{int(size)} {units[0]}"
    return f"{size:.1f} {units[index]}"
# lab06 finalized
