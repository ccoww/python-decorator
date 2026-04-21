"""
装饰器模式（Decorator）- Python 最小可运行示例。
场景：饮料基类 + 调料装饰（摩卡、奶泡），运行时按需叠加功能与价格。
运行: python3 beverage_decorator.py
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class Espresso(Beverage):
    def get_description(self) -> str:
        return "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def get_description(self) -> str:
        return "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage


class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20


class Whip(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


def main() -> None:
    beverage1: Beverage = Espresso()
    print(f"{beverage1.get_description()} ${beverage1.cost():.2f}")

    beverage2: Beverage = HouseBlend()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost():.2f}")


if __name__ == "__main__":
    main()
