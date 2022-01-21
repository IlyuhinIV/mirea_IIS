from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self,mes:str) -> None:
        pass

class Observable(ABC):
    def __init__(self) -> None:
        self.observers = []
        self.prod = []

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify(self) -> None:
        for observer in self.observers:
            for prod in self.prod:
                observer.update(prod)

class Prod(Observable):
    def add(self, prod: Observer) -> None:
        self.prod.append(prod)

class Peop(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self,mes:str) -> None:
        print(f'{self.name} получил: {mes}')

class Builder(ABC):
    @abstractmethod
    def product(self) -> None: pass

    @abstractmethod
    def product_cake(self) -> None: pass

    @abstractmethod
    def product_saled(self) -> None: pass

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
    new = Prod()
    new.register(Peop('Ivan'))
    new.add('Торт')
    print_status(Creation_Cake())
    new.notify()
    print('---------------------------------------------')
    new = Prod()
    new.register(Peop('Vika'))
    new.add('Салат')
    print_status(Creation_Salad())
    new.notify()


