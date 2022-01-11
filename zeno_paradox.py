class Runner:
    def __init__(self, position: int) -> None:
        self._position = position

    @property
    def position(self) -> float:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        self._position = 1 / value


def run() -> None:
    achilles = Runner(1)
    tortoise = Runner(1)
    for x in range(1, 50):
        achilles.position = x
        tortoise.position = x
        print(f"Achilles {achilles.position}")
        print(f"Tortoise {tortoise.position}")


if __name__ == "__main__":
    run()
