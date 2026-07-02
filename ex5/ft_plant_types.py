#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0, age_x: int = 0) -> None:
        self.name = name
        self.height = height
        self.age_x = age_x

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self.height = new_height
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.name.capitalize()}:Error! Height cannot be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self.height

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self.age_x = new_age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.name.capitalize()}: Error! age cannot be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self.age_x

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
            )

    def age(self) -> None:
        self.age_x = self.age_x + 1

    def grow(self) -> None:
        self.height += 0.8
        self.age()

    def week_growth(self) -> None:
        initial_height = self.height
        for days in range(1, 8):
            self.grow()
            print(f"=== Day {days} ===")
            self.show()
        print(f"Growth this week: {(self.height - initial_height):.1f}cm")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_x: int, color: str) -> None:
        super().__init__(name, height, age_x)
        self.color = color

    def bloom(self):
        