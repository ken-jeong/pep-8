class Empty(Exception):
    pass


class ArrayQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data):
            return False
        else:
            return True

    def first(self):
        if len(self._data) is False:
            raise Empty("error")
        else:
            return self._data[0]

    def dequeue(self):
        if len(self._data) is False:
            raise Empty("error")

        val = self._data[0]
        del self._data[0]
        return val

    def enqueue(self, e):
        self._data.append(e)


Q = ArrayQueue()

Q.enqueue(5)        # Q._data 리스트에 5 추가(append), Q._data = [5]
Q.enqueue(3)        # Q._data 리스트에 3 추가(append), Q._data = [5, 3]
print(len(Q))       # Q._data 리스트의 길이인 2 출력

print(Q.dequeue())  # Q._data 리스트에서 인덱스가 0인 값 5를 삭제하고 출력, Q._data = [3]
print(len(Q))       # Q._data 리스트의 길이인 1 출력

print(Q.first())    # Q._data 리스트에서 인덱스가 0인 값 3을 출력
