from dataclasses import dataclass

@dataclass
class City:
    name: str
    department: str
    population: int


city_list: list[City] = [
    City('Montpellier', '34', 307_101),
    City('Pau', '64', 77_000),
    City(name='Mittelbergheim', department='67', population=640),
]

# city_list.append('test') # erreur de type

for city in city_list:
    print(city.name)