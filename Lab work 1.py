# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
from abc import ABC, abstractmethod


class Furniture(ABC):
    def __init__(self, material: str, height: float, width: float, depth: float):
        """
        Инициализация класса Furniture.

        :param material: Материал, из которого изготовлена мебель (например, "дерево", "металл").
        :param height: Высота мебели в сантиметрах (должна быть положительной).
        :param width: Ширина мебели в сантиметрах (должна быть положительной).
        :param depth: Глубина мебели в сантиметрах (должна быть положительной).

        :raises ValueError: Если height, width или depth не положительные.

        >>> table = Furniture("дерево", 75, 120, 60)
        """
        if height <= 0 or width <= 0 or depth <= 0:
            raise ValueError("Высота, ширина и глубина должны быть положительными числами.")

        self.material = material
        self.height = height
        self.width = width
        self.depth = depth

    @abstractmethod
    def describe(self) -> str:
        """Возвращает описание мебели."""
        ...

    @abstractmethod
    def get_area(self) -> float:
        """Возвращает площадь поверхности мебели."""
        ...


class Tree(ABC):
    def __init__(self, species: str, age: int, height: float):
        """
        Инициализация класса Tree.

        :param species: Вид дерева (например, "дуб", "ель").
        :param age: Возраст дерева в годах (должен быть неотрицательным).
        :param height: Высота дерева в метрах (должна быть положительной).

        :raises ValueError: Если age отрицательный или height не положительная.

        >>> oak = Tree("дуб", 50, 20)
        """
        if age < 0 or height <= 0:
            raise ValueError("Возраст дерева не может быть отрицательным, а высота должна быть положительной.")

        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """Увеличивает возраст дерева на заданное количество лет."""
        ...

    @abstractmethod
    def shed_leaves(self) -> str:
        """Возвращает информацию о сбрасывании листьев."""
        ...


class SocialNetwork(ABC):
    def __init__(self, name: str, users_count: int):
        """
        Инициализация класса SocialNetwork.

        :param name: Название социальной сети (например, "Facebook").
        :param users_count: Количество пользователей в социальной сети (должно быть неотрицательным).

        :raises ValueError: Если users_count отрицательный.

        >>> facebook = SocialNetwork("Facebook", 2500000000)
        """
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.users_count = users_count

    @abstractmethod
    def add_user(self) -> None:
        """Добавляет нового пользователя в социальную сеть."""
        ...

    @abstractmethod
    def remove_user(self) -> None:
        """Удаляет пользователя из социальной сети."""
        ...
