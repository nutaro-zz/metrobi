class Achilles:

    def __init__(self) -> None:
        self.position = 0


class Tortoise:

    def __init__(self) -> None:
        self.position = 1


def run() -> None:
    achilles = Achilles()
    tortoise = Tortoise()
    while achilles.position <= tortoise.position:
        achilles.position = tortoise.position
        tortoise.position += 0.5
        print(f"Achilhes {achilles.position}")
        print(f"Tortoise {tortoise.position}")


if __name__ == "__main__":
    run()
