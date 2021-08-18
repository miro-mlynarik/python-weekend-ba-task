class Splitter:
    def __init__(self):
        self.result = set()

    def split(self, text):
        self._try_level(text, [])

        return sorted(list(self.result))

    def _try_level(self, text, path):
        if len(text) == 0:
            self.result.update(path)
            return

        self._try_level_with_length(text, path, 2)
        self._try_level_with_length(text, path, 3)

    def _try_level_with_length(self, text, path, length):
        if len(text) < length:
            return

        new = text[0:length]
        previous = path[-1] if len(path) > 0 else ""
        if new != previous:
            path.append(new)
            self._try_level(text[length:], path)
            path.pop()


if __name__ == '__main__':
    # print(Splitter().split("abcdef"))
    print(Splitter().split("abcdefg"))
    # print(Splitter().split("ababcabc"))
    # print(Splitter().split("ababcabc"))
    # print(Splitter().split("ccccacccc"))
