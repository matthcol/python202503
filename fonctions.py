def code_city(city: str, department: int, counter: int) -> str:
    a = city[:3].upper()
    return f"{a:_<3}{counter:05d}D{department:03d}"

def decode(code_city: str) -> tuple[str, int, int]: # 3.10
# def decode(code_city: str) -> Tuple[str, int, int]:  # 3.8/3.9
    """decode a city code in 3 parts: short name, counter, department

    The city_code must have 12 characters:
    - city short name on the first 3 characters
    - counter on characters 3 to 7
    - department on last 3 characters (after letter D)
    
    Example: code_city = 'MON00123D034' => 'MON', 123, 34 
    """
    city_part = code_city[:3]
    counter_part = code_city[3:8]
    department_part = code_city[-3:]
    return city_part.replace('_', ''), int(counter_part), int(department_part)

code1 = code_city('Pau', 64, 1)
print(code1)

# appel erroné en terme de type
# code2 = code_city('Pau', 64.5, 1) 
# print(code2)

city, counter, dept = decode(code1)
print(city, counter, dept)