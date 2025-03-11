class Valuable:
    def get_price(self) -> int: ...


class Product(Valuable):
    def __init__(self, price):
        self.price = price

    def get_price(self) -> int:
        return self.price


class Box(Valuable):
    def __init__(self) -> None:
        self.valuables: list[Valuable] = []

    def add_valuable(self, valuable: Valuable):
        self.valuables.append(valuable)

    def remove_valuable(self, valuable: Valuable):
        self.valuables.remove(valuable)

    def get_price(self) -> int:
        return sum(v.get_price() for v in self.valuables)


if __name__ == "__main__":
    box = Box()
    mug = Product(10)
    t_shirt = Product(30)
    meals = Box()
    milk = Product(5)
    bread = Product(2)
    meals.add_valuable(milk)
    meals.add_valuable(bread)
    box.add_valuable(meals)
    box.add_valuable(mug)
    box.add_valuable(t_shirt)
    print(f"Price for the box: {box.get_price()}")
