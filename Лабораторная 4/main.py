if __name__ == "__main__":
    class PowerReactor:
        def __init__(self, power: int, coolant: str, operation_organization: str):
            """
            Создание и подготовка к работе объекта "PowerReactor" (базовый класс)

            :param power: Мощность (МВт)
            :param coolant: Теплоноситель
            :param operation_organization: Эксплуатирующая организация (ЭО)
            """
            self.power = power
            self.coolant = coolant
            self._operation_organization = operation_organization

        @property  # Атрибут operation_organization пользователь изменять не может, т.к. в РФ одна ЭО
        def operation_organization(self) -> str:
            """
            Метод возвращает название ЭО

            :return: Название_ЭО
            """
            return self._operation_organization

        def shut_down(self, time_of_shutdown: int) -> None:
            """
            Метод для останова реактора

            :param time_of_shutdown: Время останова (с)
            :return: Метод ничего не возвращает
            """
            ...

        def design_reactor(self, design_requirements: str) -> str:
            """
            Метод для проектирования реактора

            :param design_requirements: Требования к проекту
            :return: Метод возвращает название проектирующей организации
            """
            ...

        def __str__(self) -> str:
            """
            Метод __str__ должен возвращать строку формата, где "мощность" берется с помощью атрибута power,
            "теплоноситель" берется с помощью атрибута coolant, "эксплуатирующая организация" берется с помощью
            атрибута operation_organization

            :return: Реактор. Мощность: мощность. Теплоноситель: теплоноситель. ЭО: эксплуатирующая организация
            """
            return f"Реактор. Мощность: {self.power} МВт. Теплоноситель: {self.coolant}. ЭО: {self.operation_organization}"

        def __repr__(self) -> str:
            """
            Метод __repr__ должен возвращать валидную python строку,
            по которой можно инициализировать точно такой же экземпляр

            :return: Reactor(power=_, coolant='_', operation_organization='_')
            """
            return f"{self.__class__.__name__}(power={self.power}, coolant={self.coolant!r}, " \
                   f"operation_organization={self.operation_organization!r})"


    class ThermalReactor(PowerReactor):
        def __init__(self, power: int, coolant: str, operation_organization: str, moderator: str):
            """
            Создание и подготовка к работе объекта "ThermalReactor" (дочерний класс)

            :param power: Мощность
            :param coolant: Теплоноситель
            :param operation_organization: Эксплуатирующая организация (ЭО)
            :param moderator: Замедлитель
            """
            super().__init__(power, coolant, operation_organization)
            # Атрибуты power, coolant, operation_organization наследуются из базового класса
            self.moderator = moderator

        def shut_down(self, time_of_shutdown: int) -> bool:
            """
            Метод для останова реактора (так как тепловой реактор может потерять устойчивость, при останове это нужно
            проверить, поэтому метод необходимо перегрузить)

            :param time_of_shutdown: Время останова (с)
            :return: Делает вывод, остался ли реактор устойчивым или нет
            """
            ...

        def __str__(self) -> str:
            """
            Метод __str__ должен возвращать строку формата, где "мощность" берется с помощью атрибута power,
            "теплоноситель" берется с помощью атрибута coolant, "эксплуатирующая организация" берется с помощью
            атрибута operation_organization, замедлитель берется с помощью атрибута moderator

            :return: Тепловой реактор. Мощность: мощность. Теплоноситель: теплоноситель. ЭО: эксплуатирующая организация.
                     Замедлитель: замедлитель
            """
            return f"Тепловой реактор. Мощность: {self.power} МВт. Теплоноситель: {self.coolant}. " \
                   f"ЭО: {self.operation_organization}. Замедлитель: {self.moderator}"

        def __repr__(self) -> str:
            """
            Метод __repr__ должен возвращать валидную python строку,
            по которой можно инициализировать точно такой же экземпляр

            :return: ThermalReactor(power=_, coolant='_', operation_organization='_', moderator='_')
            """
            return f"{self.__class__.__name__}(power={self.power}, coolant={self.coolant!r}, " \
                   f"operation_organization={self.operation_organization!r}), moderator={self.moderator!r}"
    pass
