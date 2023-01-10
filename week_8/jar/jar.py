class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

cookie_jar = Jar(10)
cookie_jar.deposit(8)
cookie_jar.withdraw(6)
print(cookie_jar.capacity)
print(cookie_jar.size)