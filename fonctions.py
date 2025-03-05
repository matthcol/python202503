def code_city(city: str, department: int, counter: int) -> str:
    a = city[:3].upper()
    return f"{a:_<3}{counter:05d}D{department:03d}"

code1 = code_city('Pau', 64, 1)
print(code1)

# appel erroné en terme de type
code2 = code_city('Pau', 64.5, 1) 
# print(code2)