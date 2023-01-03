class StackObj:
    __data = None
    __next = None

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nextt):
        if nextt is None or type(nextt) == StackObj:
            self.__next = nextt


class Stack:
    top = None
    last = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            next = self.top
            self.top = obj
            self.top.next = next

    def pop(self):
        try:
            self.top = self.top.next
        except:
            self.top = None

    def get_data(self):
        obj = self.top
        array = []
        while obj is not None:
            array.append(obj.data)
            obj = obj.next
        return array[::-1]


st = Stack()
for i in range(20):
    st.push(StackObj(f'Первые данные {i}'))

for i in range(10):
    st.pop()

