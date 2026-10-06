"""측정값 저장소."""


class Store:
    def __init__(self):
        self._items = []

    def add(self, name, value):
        self._items.append((name, value))

    def count(self):
        return len(self._items)

    def elapsed_seconds(self, start, end):
        return end - start

    def average(self):
        if not self._items:
            return 0
        return sum(v for _, v in self._items) / len(self._items)
