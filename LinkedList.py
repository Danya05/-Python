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
            self.last = obj
        else:
            curr_obj = self.top
            while curr_obj.next is not None:
                curr_obj = curr_obj.next
            self.last = curr_obj
            self.last.next = obj
            self.last = obj

    def pop(self):
        obj = self.top
        if obj is None:
            self.last = None
            return None
        if obj == self.last:
            self.top = None
            self.last = None
            return obj
        while obj.next != self.last:
            obj = obj.next
        res = obj.next
        obj.next = None
        self.last = obj
        return res

    def get_data(self):
        obj = self.top
        array = []
        while obj is not None:
            array.append(obj.data)
            obj = obj.next
        return array


st = Stack()
for i in range(20):
    st.push(StackObj(f'Первые данные {i}'))
for i in range(10):
    st.pop()
for i in range(10):
    st.push(StackObj(f'Вторые данные {i}'))

for i in range(20):
    st.pop()
    print(st.get_data())
for i in range(10):
    st.pop()

print(st.get_data(), end='\n\n')
for i in range(10):
    st.push(StackObj(f'Третьи данные {i}'))

print(st.get_data(), end='\n\n')
for i in range(5):
    st.pop()

print(st.get_data(), end='\n\n')
