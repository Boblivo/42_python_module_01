#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_x: int) -> None:
        self.name = name
        self.height = height
        self.age_x = age_x

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, "
            f"{self.age_x} days old"
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


if __name__ == "__main__":
    Plant1 = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    Plant1.show()
    Plant1.week_growth()
