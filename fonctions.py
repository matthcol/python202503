def code_city(city: str, department: int, counter: int) -> str:
    a = city[:3].upper()
    # return f"{a}{counter}D{department}"
    return f"{a:_<3}{counter:05d}D{department:03d}"