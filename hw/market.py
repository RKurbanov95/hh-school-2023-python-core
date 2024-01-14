from logger import Logger

@Logger
class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.drinks = {i.title: i for i in wines + beers}

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        if title in self.drinks.keys():
            return True
        return False

    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        sorted_titles = sorted(self.drinks.keys())
        return [self.drinks[i] for i in sorted_titles]

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        result = []
        for drink in self.drinks.values():
            if from_date <= drink.production_date <= to_date:
                result.append(drink)
        return result
