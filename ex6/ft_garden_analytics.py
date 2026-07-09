#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0, age_x: int = 0) -> None:
        self.name = name
        self._height = height
        self._age_x = age_x
        if self._height < 0:
            print("Height cannot be negative. Height automatically set to 0")
            self.set_height(0)
        elif self._age_x < 0:
            print("Age cannot be negative. Age automatically set to 0")
            self.set_age(0)
        self.Stats = self.StatisticHolder(name)

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name.capitalize()}:Error! Height cannot be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age_x = new_age
        else:
            print(f"{self.name.capitalize()}: Error! age cannot be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._age_x

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
            )
        self.Stats.number_of_show = self.Stats.number_of_show + 1

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
        self.Stats.number_of_age = self.Stats.number_of_age + 1

    def grow(self) -> None:
        self.set_height(self.get_height() + 1)
        self.Stats.number_of_grow = self.Stats.number_of_grow + 1

    def week_growth(self) -> None:
        initial_height = self.get_height()
        for days in range(1, 8):
            self.grow()
            print(f"=== Day {days} ===")
            self.show()
        print(f"Growth this week: "
              f"{(self.get_height() - initial_height):.1f}cm")

    @staticmethod
    def year_old_checker(age_x: int) -> None:
        print(f"Is {age_x} more than a year? -> ", end="")
        if age_x > 365:
            print(f"{True}")
        else:
            print("False")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant")

    class StatisticHolder:
        def __init__(self, name: str) -> None:
            self.name = name
            self.number_of_grow = 0
            self.number_of_age = 0
            self.number_of_show = 0
            self.number_of_shade = -1

        def display(self) -> None:
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.number_of_grow} grow, "
                  f"{self.number_of_age} age, "
                  f"{self.number_of_show} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_x: int, color: str,
                 bloomed: bool = False) -> None:
        super().__init__(name, height, age_x)
        self.color = color
        self.bloomed = bloomed

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed is True:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_x: int, diameter: int):
        super().__init__(name, height, age_x)
        self.diameter = diameter
        self.Stats.number_of_shade = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.diameter:.1f}cm wide.")
        self.Stats.number_of_shade = self.Stats.number_of_shade + 1

    def display(self) -> None:
        self.Stats.display()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_x: int,
                 haverst_season: str, nutritional_value: int = 0):
        super().__init__(name, height, age_x)
        self.harvest_season = haverst_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season : {self.harvest_season.capitalize()}")
        print(f"Nutrition value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value = self.nutritional_value + 1

    def long_grow(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        for i in range(1, days + 1):
            self.grow()


class Seed(Flower):
    def __init__(self, name: str, height: float, age_x: int, color: str,
                 bloomed: bool, number_of_seeds: int) -> None:
        super().__init__(name, height, age_x, color, bloomed)
        self.number_of_seeds = number_of_seeds

    def bloom(self) -> None:
        super().bloom()
        self.number_of_seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds : {self.number_of_seeds}")


def show_statistic(PlantInstance: Plant) -> None:
    PlantInstance.Stats.display()
    if PlantInstance.Stats.number_of_shade != -1:
        print(f"{PlantInstance.Stats.number_of_shade} shade")


if __name__ == "__main__":
    print("== Checking year-old")
    Plant.year_old_checker(30)
    Plant.year_old_checker(400)
    print()

    print("=== Flower")
    Flower1 = Flower("Rose", 15, 10, "red")
    Flower1.show()
    show_statistic(Flower1)
    print(f"[asking the {Flower1.name} to grow and bloom]")
    Flower1.grow()
    Flower1.bloom()
    Flower1.show()
    show_statistic(Flower1)
    print()

    print("===Tree")
    Tree1 = Tree("Oak", 200, 365, 5)
    Tree1.show()
    show_statistic(Tree1)
    Tree1.produce_shade()
    show_statistic(Tree1)
    print()

    print("=== Seed")
    Seed1 = Seed("sunflower", 80, 45, "yellow", False, 0)
    Seed1.show()
    print(f"[make the {Seed1.name} to grow, age and bloom]")
    Seed1.grow()
    Seed1.set_height(110)
    Seed1.age()
    Seed1.bloom()
    Seed1.show()
    show_statistic(Seed1)
    print()

    print("=== Anonymous")
    Anon = Plant.create_anonymous()
    Anon.show()
    show_statistic(Anon)
