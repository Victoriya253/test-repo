class Flower:
    """Базовый класс для цветов"""

    def __init__(self, name: str, color: str, scent: str) -> None:
        """Инициализация атрибутов цветка"""
        self.name = name
        self.color = color
        self.scent = scent

    def __str__(self) -> str:
        """Возвращает строковое представление цветка"""
        return f"{self.name} цвет {self.color} с ароматом {self.scent}"

    def __repr__(self) -> str:
        """Возвращает подробное представление цветка"""
        return f"Flower(name='{self.name}', color='{self.color}', scent='{self.scent}')"


class Rose(Flower):
    """Класс розы, наследуется от Flower"""

    def __init__(self, color: str, scent: str, thorn_length: float) -> None:
        """Инициализация атрибутов розы"""
        super().__init__("Роза", color, scent)
        self.__thorn_length = thorn_length  # Инкапсуляция, чтобы длина шипов не менялась вне класса

    def __str__(self) -> str:
        """Возвращает строковое представление розы с длиной шипов"""
        return f"{super().__str__()} с длиной шипов {self.__thorn_length} см"

    def __repr__(self) -> str:
        """Возвращает подробное представление розы"""
        return f"Rose(color='{self.color}', scent='{self.scent}', thorn_length={self.__thorn_length})"

    def info(self) -> str:
        """Возвращает информацию о розе"""
        return f"{self.name} цвет {self.color}, запах: {self.scent}, длина шипов: {self.__thorn_length} см"


class Tulip(Flower):
    """Класс тюльпана, наследуется от Flower"""

    def __init__(self, color: str, scent: str, bloom_time: str) -> None:
        """Инициализация атрибутов тюльпана"""
        super().__init__("Тюльпан", color, scent)
        self.bloom_time = bloom_time  # Доступен для изменения, так как его изменение может быть полезным

    def __str__(self) -> str:
        """Возвращает строковое представление тюльпана с временем цветения"""
        return f"{super().__str__()} время цветения: {self.bloom_time}"

    def __repr__(self) -> str:
        """Возвращает подробное представление тюльпана"""
        return f"Tulip(color='{self.color}', scent='{self.scent}', bloom_time='{self.bloom_time}')"

    def info(self) -> str:
        """Возвращает информацию о тюльпане"""
        return f"{self.name} цвет {self.color}, запах: {self.scent}, время цветения: {self.bloom_time}"


if __name__ == "__main__":
    rose = Rose("красный", "сладкий", 3.5)
    tulip = Tulip("желтый", "нежный", "весна")

    print(rose)
    print(repr(rose))
    print(rose.info())

    print(tulip)
    print(repr(tulip))
    print(tulip.info())
