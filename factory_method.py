from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

class Product(ABC):
    @abstractmethod
    def status(self) -> str:
        pass

class Creation_Salad(Creator):
    def create(self) -> Product:
        return Salad()

class Salad(Product):
    def status(self) -> str:
        return "Салат приготовлен"

class Creation_Cake(Creator):
    def create(self) -> Product:
        return Cake()

class Cake(Product):
    def status(self) -> str:
        return "Торт приготовлен"

def print_status(create: Creator) -> None:
    s = create.create()
    print(s.status())

if __name__ == "__main__":
    print_status(Creation_Salad())
    print_status(Creation_Cake())
