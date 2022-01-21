from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import List

class Server(ABC):
    @abstractmethod
    def sub(self, observer:Observer) -> None:
        pass

    @abstractmethod
    def unsub(self, observer:Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteServer(Server):
    state: int = None
    observers: List[Observer] = []

    def sub(self, observer:Observer) -> None:
        self.observers.append(observer)

    def unsub(self, observer:Observer) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        print('Уведомление')
        for o in self.observers:
            o.update(self)

    def logic(self) -> None:
        self.state = random.randrange(0,10)
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, s: Server) -> None:
        pass

class OneObserver(Observer):
    def update(self, s: Server) -> None:
        if s.state < 3:
            print('A')
class TwoObserver(Observer):
    def update(self, s: Server) -> None:
        if s.state >= 3:
            print('B')
if __name__ == "__main__":
    server = ConcreteServer()
    one = OneObserver()
    server.sub(one)
    two = TwoObserver()
    server.sub(two)

    server.logic()
    server.logic()