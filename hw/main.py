from wine import Wine
from beer import Beer
from market import Market

# Создаем список вин и пива
wine_list = [
    Wine("Merlot", "2023-01-01"),
    Wine("Chardonnay", "2023-02-01"),
    Wine("Cabernet Sauvignon", "2023-03-01"),
    Wine("Pinot Noir", "2023-04-01"),
    Wine("Riesling", "2023-05-01"),
    Wine("Syrah", "2023-06-01"),
    Wine("Zinfandel", "2023-07-01"),
    Wine("Malbec", "2023-08-01"),
    Wine("Sauvignon Blanc", "2023-09-01"),
    Wine("Tempranillo", "2023-10-01")
]

beer_list = [
    Beer("IPA", "2023-01-01"),
    Beer("Stout", "2023-02-01"),
    Beer("Pale Ale", "2023-03-01"),
    Beer("Pilsner", "2023-04-01"),
    Beer("Porter", "2023-05-01"),
    Beer("Saison", "2023-06-01"),
    Beer("Wheat Beer", "2023-07-01"),
    Beer("Sour Beer", "2023-08-01"),
    Beer("Brown Ale", "2023-09-01"),
    Beer("Amber Ale", "2023-10-01")
]

market = Market(wine_list, beer_list)
print("Начало проверок")
print("Задача 1: Получаем отсортированный список всех напитков по наименованию")
drinks_sorted_by_title = market.get_drinks_sorted_by_title()
print([i.title for i in drinks_sorted_by_title])

print("Задача 2: Проверить наличие напитка в магазине")
drink_exists = market.has_drink_with_title("Wheat Beer")
print(drink_exists)
drink_exists = market.has_drink_with_title("Porter")
print(drink_exists)

print("Задача 3: Получаем список напитков (вина и пива) в указанном диапазоне даты производства")

drinks_in_date_range = market.get_drinks_by_production_date("2023-08-01", "2023-10-01")
print([i.title for i in drinks_in_date_range])
