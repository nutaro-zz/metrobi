import math


class DropEgg:

    def __init__(self):
        self.eggs = 2
        self.floor = 100
        self.steps = int(math.sqrt(self.floor * self.eggs))
        self.egg_break = 15

    def run(self):
        print(f"Egg broke at {self.drop(self.steps)} floor")
        print(f"In the worst case scenario it would be necessary {self.steps}")

    def drop(self, top_floor):
        broken = False
        if self.egg_break <= top_floor:
            broken = True
        if not broken:
            return self.drop(top_floor+self.steps)
        for x in range((top_floor - self.steps) + 1, top_floor):
            if x == self.egg_break:
                return self.egg_break


if __name__ == "__main__":
    egg = DropEgg()
    egg.run()
