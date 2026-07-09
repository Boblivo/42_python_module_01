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

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def grow(self) -> None:
        self.set_height(self.get_height() + 1)
        self.age()

    def week_growth(self) -> None:
        initial_height = self.get_height()
        for days in range(1, 8):
            self.grow()
            print(f"=== Day {days} ===")
            self.show()
        print(f"Growth this week: "
              f"{(self.get_height() - initial_height):.1f}cm")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_x: int, color: str,
                 bloomed: bool = False) -> None:
        super().__init__(name, height, age_x)
        self.color = color
        self.bloomed = bloomed

    def bloom(self) -> None:
        self.bloomed = True
        print(f"[asking the {self.name} to bloom]")

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

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.diameter:.1f}cm wide.")


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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Flower1 = Flower("Rose", 15, 10, "red")
    Flower1.show()
    Flower1.bloom()
    Flower1.show()
    print("\n")
    print("=== Tree")
    Tree1 = Tree("oak", 200, 365, 5)
    Tree1.show()
    Tree1.produce_shade()
    print("\n")
    print("=== Vegetable")
    Vegetable1 = Vegetable("Tomato", 5, 10, "April")
    Vegetable1.show()
    Vegetable1.long_grow(20)
    Vegetable1.show()
