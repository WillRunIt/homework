import string


_ASCII_MAPPING = {}
_INDEX = 0
for letter in string.ascii_letters + "0123456789 ,.!?()[]":
    _ASCII_MAPPING[letter] = _INDEX
    _INDEX += 1


def _hash_function(key: str, size=100):
    """Take a key as an input and calculate an integer output
    Output should be between 0 and size
    """
    key = str(key)
    hash_value = 0
    for letter in key:
        hash_value += _ASCII_MAPPING[letter]
    hash_value = hash_value % size
    return hash_value


class Dictionary():
    def __init__(self):
        self.capacity = 10
        self._size = 0
        self.storage = []
        self._resize_and_rehash()

    def _resize_and_rehash(self):
        old_storage = self.storage.copy()
        self.capacity *= 2
        self.storage = []
        for _ in range(self.capacity):
            self.storage.append([])

        for cell in old_storage:
            for key, value in cell:
                self.put(key, value)

    def get(self, search_key):
        index = _hash_function(search_key, size=self.capacity)
        for key, value in self.storage[index]:
            if search_key == key:
                return value
        raise KeyError(search_key)

    def put(self, key, value):
        self._size =+ 1
        if self._size == self.capacity:
            self._resize_and_rehash()
        index = _hash_function(key, size=self.capacity)
        self.storage[index].append((key, value))

    def pop(self, search_key):
        self._size -= 1
        index = _hash_function(search_key, size=self.capacity)
        for key, value in self.storage[index]:
            if search_key == key:
                self.storage[index].pop()

    def items(self):
        items = []
        for item in self.storage:
            items.append(item)
        return items

    def keys(self):
        keys = []
        for key in self.storage:
            keys.append(key)
        return keys

    def __str__(self):
        return f"Capacity: {self.capacity}, Dictionary: {self.storage}"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


demo_dict = Dictionary()
demo_dict["1"] = 1
print(demo_dict["1"])
demo_dict["2"] = 2
demo_dict[(1, 2, 3)] = (1, 2, 3)
print(demo_dict.storage)