class NestedIterator:
    def __init__(self, list_):
        self._stopped = False
        self._list = list_
        self._i = 0
        self._j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self._i < len(self._list):
                if self._j < len(self._list[self._i]):
                    v = self._list[self._i][self._j]
                    self._j += 1
                    return v

                self._i += 1
                self._j = 0
            self._stopped = True
        raise StopIteration


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'g', 'h'],
        [],
        [],
        ['i', 'j', 'k'],
        []
    ]

    print(next(NestedIterator(nested_list)))
    flat_list = list(NestedIterator(nested_list))
    print(*flat_list)


main()

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for i in nested_list[:]:
    for x in i: nested_list.append(x)
    nested_list.remove(i)
print(nested_list)


