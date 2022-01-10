class Lexical:

    def __init__(self, value: str):
        self.values = value
        self.open_close = {"{": "}", "[": "]", "(": ")"}
        self.open_buffer = []
        self.close_buffer = []

    def _analyze(self):
        for x in self.values:
            if x in self.open_close.keys():
                self.open_buffer.append(x)
                continue
            if x in self.open_close.values():
                self.close_buffer.append(x)

    def validate(self) -> bool:
        self._analyze()
        if len(self.open_buffer) != len(self.close_buffer):
            return False
        for x in range(0, len(self.open_buffer)):
            _open = self.open_buffer.pop()
            _close = self.close_buffer.pop(0)
            if _close == self.open_close[_open]:
                continue
            return False
        return True


if __name__ == "__main__":
    lexical = Lexical("{([)]}")
    print(lexical.validate())
