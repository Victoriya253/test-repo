import doctest


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

    def grow(self, growth: float) -> None:
        """
        Увеличение высоты дерева.

        :param growth: Увеличение высоты

        :raise ValueError: Если увеличение высоты отрицательное

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.grow(2.5)
        >>> tree.height
        13.0
        >>> tree.grow(-1)
        Traceback (most recent call last):
            ...
        ValueError: Увеличение высоты должно быть положительным
        """
        if not isinstance(growth, (int, float)):
            raise TypeError("Увеличение высоты должно быть типа int или float")
        if growth < 0:
            raise ValueError("Увеличение высоты должно быть положительным")
        self.height += growth

    def age_tree(self) -> None:
        """
        Увеличивает возраст дерева на 1 год.

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.age_tree()
        >>> tree.age
        6
        """
        self.age += 1

    def display_info(self) -> str:
        """
        Отображает информацию о дереве.

        :return: Строка с информацией о дереве

        Примеры:
        >>> tree = Tree("Сосна", 10.5, 5)
        >>> tree.display_info()
        'Вид: Сосна, Высота: 10.5, Возраст: 5'
        """
        return f"Вид: {self.species}, Высота: {self.height}, Возраст: {self.age}"


if __name__ == "__main__":
    doctest.testmod()


class Love:
    def __init__(self, partner: str, duration: int, intensity: float):
        """
        Создание и подготовка к работе объекта "Любовь"

        :param partner: Имя партнёра
        :param duration: Длительность отношений в месяцах
        :param intensity: Интенсивность любви от 0.0 до 10.0

        Примеры:
        >>> love = Love("Никита", 12, 8.5)  # инициализация экземпляра класса
        """
        if not isinstance(partner, str):
            raise TypeError("Имя партнёра должно быть строкой")
        if not partner:
            raise ValueError("Имя партнёра не может быть пустым")
        self.partner = partner

        if not isinstance(duration, int):
            raise TypeError("Длительность отношений должна быть целым числом")
        if duration < 0:
            raise ValueError("Длительность отношений не может быть отрицательной")
        self.duration = duration

        if not isinstance(intensity, (int, float)):
            raise TypeError("Интенсивность любви должна быть типа int или float")
        if intensity < 0.0 or intensity > 10.0:
            raise ValueError("Интенсивность любви должна быть в диапазоне от 0.0 до 10.0")
        self.intensity = intensity

    def deepen_relationship(self, months: int) -> None:
        """
        Увеличивает длительность отношений.

        :param months: Количество месяцев, на которое увеличивается длительность

        :raise ValueError: Если количество месяцев отрицательное

        Примеры:
        >>> love = Love("Никита", 12, 8.5)
        >>> love.deepen_relationship(6)
        >>> love.duration
        18
        >>> love.deepen_relationship(-1)
        Traceback (most recent call last):
            ...
        ValueError: Количество месяцев должно быть положительным
        """
        if not isinstance(months, int):
            raise TypeError("Количество месяцев должно быть целым числом")
        if months < 0:
            raise ValueError("Количество месяцев должно быть положительным")
        self.duration += months

    def increase_intensity(self, amount: float) -> None:
        """
        Увеличивает интенсивность любви.

        :param amount: Значение, на которое увеличивается интенсивность

        :raise ValueError: Если увеличение превышает 10.0

        Примеры:
        >>> love = Love("Никита", 12, 8.5)
        >>> love.increase_intensity(1.0)
        >>> love.intensity
        9.5
        >>> love.increase_intensity(2.0)
        Traceback (most recent call last):
            ...
        ValueError: Интенсивность любви не может превышать 10.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Увеличение интенсивности должно быть типа int или float")
        if self.intensity + amount > 10.0:
            raise ValueError("Интенсивность любви не может превышать 10.0")
        self.intensity += amount

    def display_info(self) -> str:
        """
        Отображает информацию о любви.

        :return: Строка с информацией о любви

        Примеры:
        >>> love = Love("Никита", 12, 8.5)
        >>> love.display_info()
        'Партнёр: Никита, Длительность: 12, Интенсивность: 8.5'
        """
        return f"Партнёр: {self.partner}, Длительность: {self.duration}, Интенсивность: {self.intensity}"


class Mammals:
    def __init__(self, species: str, habitat: str):
        """
        Создание объекта "Млекопитающие"

        :param species: Вид млекопитающего
        :param habitat: Среда обитания

        Примеры:
        >>> mammal = Mammals("Лев", "Савана")  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид должен быть строкой (str)")
        self.species = species

        if not isinstance(habitat, str):
            raise TypeError("Среда обитания должна быть строкой (str)")
        self.habitat = habitat

    def change_species(self, new_species: str) -> None:
        """
        Устанавливает новый вид.

        :param new_species: Новый вид

        Примеры:
        >>> mammal = Mammals("Лев", "Савана")
        >>> mammal.change_species("Тигр")
        >>> mammal.species
        'Тигр'
        """
        if not isinstance(new_species, str):
            raise TypeError("Новый вид должен быть строкой (str)")
        self.species = new_species

    def change_habitat(self, new_habitat: str) -> None:
        """
        Устанавливает новую среду обитания.

        :param new_habitat: Новая среда обитания

        Примеры:
        >>> mammal = Mammals("Лев", "Савана")
        >>> mammal.change_habitat("Лес")
        >>> mammal.habitat
        'Лес'
        """
        if not isinstance(new_habitat, str):
            raise TypeError("Новая среда обитания должна быть строкой (str)")
        self.habitat = new_habitat

    def description(self) -> str:
        """
        Возвращает описание млекопитающего.

        :return: Строка с описанием

        Примеры:
        >>> mammal = Mammals("Лев", "Савана")
        >>> mammal.description()
        'Млекопитающее: Лев, обитает в Саване.'
        """
        return f"Млекопитающее: {self.species}, обитает в {self.habitat}."
