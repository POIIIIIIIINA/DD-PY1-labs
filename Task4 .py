class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)   # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        """Инициализация даты"""
        self._day = day
        self._month = month
        self._year = year
        self.is_valid_date(self._day, self._month, self._year)

    def is_leap_year(self, year: int) -> bool:
        """Проверяет, является ли год високосным"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        max_day = self.get_max_day(month, year)
        if day < 1 or day > max_day:
            raise ValueError(f"Day must be between 1 and {max_day} for month {month}.")

    @property
    def day(self) -> int:
        """Геттер для дня"""
        return self._day

    @day.setter
    def day(self, value: int) -> None:
        """Сеттер для дня"""
        self.is_valid_date(value, self._month, self._year)
        self._day = value

    @property
    def month(self) -> int:
        """Геттер для месяца"""
        return self._month

    @month.setter
    def month(self, value: int) -> None:
        """Сеттер для месяца"""
        self.is_valid_date(self._day, value, self._year)
        self._month = value

    @property
    def year(self) -> int:
        """Геттер для года"""
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        """Сеттер для года"""
        self.is_valid_date(self._day, self._month, value)
        self._year = value

    def __str__(self) -> str:
        """Возвращает строковое представление даты"""
        return f"{self._day:02d}-{self._month:02d}-{self._year}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление даты"""
        return f"Date(day={self._day}, month={self._month}, year={self._year})"


# Примеры использования класса Date
if __name__ == "__main__":
    try:
        date = Date(29, 2, 2020)  # Високосный год
        print(date)  # Вывод: 29-02-2020
        date.day = 28  # Изменение дня
        print(date)  # Вывод: 28-02-2020
        date.month = 3  # Изменение месяца
        print(date)  # Вывод: 28-03-2020
        date.year = 2021  # Изменение года
        print(date)  # Вывод: 28-03-2021
    except ValueError as e:
        print(e)

