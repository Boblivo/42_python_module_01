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
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.name.capitalize()}:Error! Height cannot be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age_x = new_age
            print(f"Age updated: {self.get_age()} days")
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


if __name__ == "__main__":
    print("=== Garden Security System")
    Plant1 = Plant("rose", 15, 10)
    print("Plant created : ", end="")
    Plant1.show()
    print()
    Plant1.set_height(25)
    Plant1.set_age(30)
    print()
    Plant1.set_height(-1)
    Plant1.set_age(-1)
    print()
    print("Current state: ", end="")
    Plant1.show()
