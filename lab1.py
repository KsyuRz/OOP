import doctest


class Human:
    def __init__(self, name: str, age: int):
        """
        Класс описывающий человека
        :param name: Имя человека
        :param age: Возраст человека

        Примеры:
        >>> human = Human("Иван", 30)  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возаст человека должен быть положительным числом")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа string")
        if not name:
            raise ValueError("Имя обязательно должно быть заполнено.")
        self.name = name

    def is_adult_human(self) -> bool:
        """
        Функция которая проверяет является ли человек совершеннолетним
        :return: Является ли человек совершеннолетним

        Примеры:
        >>> human = Human("Иван", 30)
        >>> human.is_adult_human()  # результат True
        """
        if self.age >= 18:
            return True
        else:
            return False

    def add_age(self, years: int) -> None:
        """
        Добавление возраста.
        :param years: Количество лет, которые прибавляются объекту
        :raise ValueError: Если количество добавляемых лет в сумме с исходным возрастом превышает 100 - вызываем ошибку

        Примеры:
        >>> human = Human("Иван",30)
        >>> human.add_age(20)
        """
        if not isinstance(years, int):
            raise TypeError("Добавляемое количество лет должно быть типа int")
        if years < 0:
            raise ValueError("Добавляемое количество лет должно быть положительным числом ")


class Car:
    def __init__(self, model: str, speed: int, max_speed: int):
        """
        Класс описывающий автомобиль
        :param model: Модель автомобиля
        :param speed:  Скорость
        :param max_speed:  Максимальная скорость

        Примеры:
        >>> car = Car("Audi RS4", 80, 280)  # инициализация экземпляра класса
        """
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть типа int")
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.speed = speed

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость  должна быть положительным числом")
        self.max_speed = max_speed

        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа string")
        if not model:
            raise ValueError("Название модели обязательно должно быть заполнено.")
        self.model = model

    def accelerate(self, increment) -> None:
        """
        Функция которая увеличивает скорость автомобиля в зависимости от increment с проверкой первоначальной скорости
        :param increment:  на сколько увеличиваем скорость
        :raise ValueError: Если после выполнения сложения speed > max_speed, то выводим ошибку

        Примеры:
        >>>car = Car("Audi RS4", 80, 280)
        >>>car.accelerate(15)
        """
        if self.speed < self.max_speed:
            self.speed += increment
        else:
            raise ValueError("скорость не может превышать максимальную")

    def decelerat(self, decrement) -> None:
        """
        Функция которая уменьшает скорость автомобиля в зависимости от decrement с проверкой первоначальной скорости
        :param decrement:  на сколько уменьшаем скорость
        :raise ValueError: Если после выполнения вычитания speed < 0, то выводим ошибку

        Примеры:
        >>>car = Car("Audi RS4", 80, 280)
        >>>car.decelerat(80)
        """
        if self.speed != 0:
            self.speed -= decrement
        else:
            raise ValueError("Автомобиль стоит на месте")


class Product:
    def __init__(self, product_name: str, price: float, quantity: int):
        """
        Класс описывающий продукт
        :param product_name: Название товара
        :param price:  Цена
        :param quantity:  Количество

        Примеры:
        >>> product = Product("Клавиатура", 25.6, 5)  # инициализация экземпляра класса
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество должно быть положительным числом")
        self.quantity = quantity

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной или равной нулю")
        self.price = price

        if not isinstance(product_name, str):
            raise TypeError("Название товара должно быть типа string")
        if not product_name:
            raise ValueError("Название товара обязательно должно быть заполнено.")
        self.product_name = product_name

    def total_cost(self) -> float:
        """
        Функция которая рассчитывает общую стоимость
        :raise ValueError: Если после выполнения сложения speed > max_speed, то выводим ошибку

        Примеры:
         >>> product = Product("Клавиатура", 25.6, 5)
        >>>product.total_cost()
        """
        return self.price * self.quantity

    def update_quantity(self, new_quantity) -> None:
        """
        Функция которая обновляет количество товаров
        :param new_quantity:  новое количество

        Примеры:
        >>>product = Product("Клавиатура", 25.6, 5)
        >>>product.update_quantity(15)
        """
        if not isinstance(new_quantity, int):
            raise TypeError("Количество должно быть типа int")
        if new_quantity < 0:
            raise ValueError("Количество должно быть положительным числом")
        self.quantity = new_quantity


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
