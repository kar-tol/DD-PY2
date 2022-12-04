import doctest
from typing import Union


class NuclearReactor:
    def __init__(self, power: int, pressure: Union[int, float], flow_rate: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ядерный реактор"

        :param power: Тепловая мощность реактора (задается в МВт)
        :param pressure: Давление в реакторе (задается в МПа)
        :param flow_rate: Расход теплоносителя в реакторе (задается в кг/с)

        Пример:
        >>> nuclear_reactor = NuclearReactor(3200, 16.14, 17544)
        """
        if not isinstance(power, int):
            raise TypeError("Тепловая энергия должна быть типа int")
        if power < 0:
            raise ValueError("Тепловая энергия не может быть отрицательным числом")
        self.power = power

        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление должно быть типа int или float")
        if pressure < 0:
            raise ValueError("Давление не может быть отрицательным числом")
        self.pressure = pressure

        if not isinstance(flow_rate, (int, float)):
            raise TypeError("Расход теплоносителя должен быть типа int или float")
        if flow_rate < 0:
            raise ValueError("Температура не может быть отрицательным числом")
        self.flow_rate = flow_rate

    def change_power(self, new_power: int) -> None:
        """
        Функция, которая меняет тепловую мощность реактора
        :param new_power: Новая тепловая мощность реактора (задается в МВт)

        Пример:
        >>> nuclear_reactor = NuclearReactor(3200, 16.14, 17544)
        >>> nuclear_reactor.change_power(3000)
        """
        if not isinstance(new_power, int):
            raise TypeError("Тепловая энергия должна быть типа int")
        if new_power < 0:
            raise ValueError("Тепловая энергия не может быть отрицательным числом")
        ...

    def change_pressure(self, new_pressure: Union[int, float]) -> None:
        """
        Функция, которая меняет давление в реакторе
        :param new_pressure: Новое давление в реакторе (задается в МПа)

        Пример:
        >>> nuclear_reactor = NuclearReactor(3200, 16.14, 17544)
        >>> nuclear_reactor.change_pressure(17)
        """
        if not isinstance(new_pressure, (int, float)):
            raise TypeError("Давление должно быть типа int или float")
        if new_pressure < 0:
            raise ValueError("Давление не может быть отрицательным числом")
        ...


class GameConsole:
    def __init__(self, name: str, price: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Игровая приставка"

        :param name: Название приставки
        :param price: Цена приставки в рублях

        Пример:
        >>> game_console = GameConsole("Xbox One", 40000)
        """
        if not isinstance(name, str):
            raise TypeError("Название игровой прситавки должно быть типа str")
        self.name = name

        if not isinstance(price, (int, float)):
            raise TypeError("Цена игровой приставки должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена игровой приставки должна быть положительным числом")
        self.price = price

    def is_turned_on_game_console(self) -> bool:
        """
        Функция, которая проверяет, включена ли игровая приставка

        :return: Включена ли приставка

        Пример:
        >>> game_console = GameConsole("Xbox One", 40000)
        >>> game_console.is_turned_on_game_console()
        """
        ...

    def fix_game_console(self, damage: str) -> None:
        """
        Функция, которая чинит игровую приставку

        :param damage: Что повреждено

        Пример:
        >>> game_console = GameConsole("Xbox One", 40000)
        >>> game_console.fix_game_console("Дисковод")
        """
        if not isinstance(damage, str):
            raise TypeError("Название поврежденного элемента должно быть типа str")
        ...


class Manuscript:
    def __init__(self, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Рукопись"

        :param name: Название рукописи
        :param pages: Количество страниц

        Пример:
        >>> manuscript = Manuscript("Мертвые души. 2 том", 475)
        """
        if not isinstance(name, str):
            raise TypeError("Название рукописи должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.pages = pages

    def opportunity_to_burn_the_manuscript(self) -> bool:
        """
        Функция, которая проверяет возможность сжечь рукопись

        :return: Можно ли сжечь рукопись

        Пример:
        >>> manuscript = Manuscript("Мертвые души. 2 том", 475)
        >>> manuscript.opportunity_to_burn_the_manuscript()
        """

    def sell_the_manuscript(self, fee: Union[int, float]) -> None:
        """
        Функция, которая продает рукопись

        :param fee: Гонорар автора (задается в рублях)

        Пример:
        >>> manuscript = Manuscript("Мертвые души. 2 том", 475)
        >>> manuscript.sell_the_manuscript(1000000)
        """
        if not isinstance(fee, (int, float)):
            raise TypeError("Гонорар должен быть типа int или float")
        if fee <= 0:
            raise ValueError("Гонорар должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
