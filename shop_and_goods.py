class SuperShop:

    goods = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)

    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def check_value(self, value):
        return type(value) == str and self.min_length <= len(value) <= self.max_length


class PriceValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_value(value):
            setattr(instance, self.name, value)

    def __init__(self, max_value=10_000):
        self.max_value = max_value

    def check_value(self, value):
        return type(value) in (int, float) and 0 <= value <= self.max_value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
