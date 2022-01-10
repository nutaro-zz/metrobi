class Runner:
    def __init__(self, position: int) -> None:
        self.position = position


def run() -> None:
    achilles = Runner(0)
    tortoise = Runner(1)
    while achilles.position <= tortoise.position:
        achilles.position = tortoise.position
        tortoise.position += 0.5
        print(f"Achilhes {achilles.position}")
        print(f"Tortoise {tortoise.position}")


if __name__ == "__main__":
    run()
