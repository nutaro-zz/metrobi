class Achilles:
    def __init__(self) -> None:
        self._position = 1

    @property
    def position(self) -> float:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        self._position += 1 / value


class Tortoise:
    def __init__(self) -> None:
        self._position = 1.4

    @property
    def position(self) -> float:
        return self._position

    @position.setter
    def position(self, value: float) -> None:
        self._position += 1 / value


def run() -> None:
    achilles = Achilles()
    tortoise = Tortoise()
    for x in range(1, 100):
        achilles.position = x
        tortoise.position = x
        print(f"Achilles {achilles.position}")
        print(f"Tortoise {tortoise.position}")


if __name__ == "__main__":
    run()
