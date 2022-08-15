class Empty(Exception):
    pass


# 공백 줄: 클래스 정의 앞뒤로 두 개의 공백 줄
class ArrayQueue:

    def __init__(self):
        self._data = []

    # 공백 줄: 클래스 내의 메소드 정의 앞뒤로는 한 개의 공백 줄
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data):
            return False
        else:
            return True

    # 공백 줄: 클래스 내의 메소드 정의 앞뒤로는 한 개의 공백 줄
    def first(self):  # 들여쓰기: 각 들여쓰기 레벨마다 4칸 공백
        # False에 대한 비교는 'if cond is False:' 또는 'if not cond:'
        if len(self._data) is False:
            raise Empty("error")
        else:
            return self._data[0]

    def dequeue(self):
        # False에 대한 비교는 'if cond is False:' 또는 'if not cond:'
        if len(self._data) is False:
            raise Empty("error")

        val = self._data[0]
        del self._data[0]
        return val

    # 공백 줄: 클래스 내의 메소드 정의 앞뒤로는 한 개의 공백 줄
    def enqueue(self, e):
        self._data.append(e)


Q = ArrayQueue()

Q.enqueue(5)        # Q._data 리스트에 5 추가(append), Q._data = [5]
Q.enqueue(3)        # Q._data 리스트에 3 추가(append), Q._data = [5, 3]
print(len(Q))       # Q._data 리스트의 길이인 2 출력

print(Q.dequeue())  # Q._data 리스트에서 인덱스가 0인 값 5를 삭제하고 출력, Q._data = [3]
print(len(Q))       # Q._data 리스트의 길이인 1 출력

print(Q.first())    # Q._data 리스트에서 인덱스가 0인 값 3을 출력
# 파일 끝의 빈 줄
