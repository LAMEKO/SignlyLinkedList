class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value=None):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, pos, value):
        if pos == 0:
            node_ = Node(value)
            node_.next = self.head
            self.head = node_
        elif 0 < pos < len(self):
            node_ = Node(value)
            count = 0
            cur = self.head
            while cur:
                if pos == count + 1:
                    node_.next = cur.next  # следующий элемент узла - следующий элемент текущего элемента
                    cur.next = node_  # следующий элемент текущего элемента - вставляемый элемент
                    break  # выходим из цикла
                cur = cur.next  # переходим к следующему элементу
                count += 1  # увеличиваем счётчик
        else:
            raise IndexError("out of range")  # если индекс выходит за границы списка

    def remove(self, pos):  # удаление по индексу
        if pos == 0:  # если удаляем голову
            self.head = self.head.next  # голова - следующий элемент
        elif 0 < pos < len(self):  # если удаляем не голову
            count = 0  # счётчик
            cur = self.head  # текущий элемент - голова
            cur_previous = None  # предыдущий элемент - пусто
            while cur:  # пока есть элементы
                if pos == count:  # если счётчик равен позиции
                    cur_previous.next = cur.next  # следующий элемент предыдущего элемента - следующий элемент текущего элемента
                    break  # выходим из цикла
                cur_previous = cur  # предыдущий элемент - текущий элемент
                cur = cur.next  # переходим к следующему элементу
                count += 1  # увеличиваем счётчик
        else:
            raise IndexError("out of range")  # если индекс выходит за границы списка

    def append(self, value):  # добавление в конец
        node_ = Node(value)  # создаём узел
        if self.is_empty():  # если список пуст
            self.head = node_  # голова - вставляемый элемент
        else:  # если список не пуст
            cur = self.head  # текущий элемент - голова
            while cur.next:  # пока есть следующий элемент
                cur = cur.next  # переходим к следующему элементу
            cur.next = node_  # следующий элемент текущего элемента - вставляемый элемент

    def __len__(self):  # длина списка
        count = 0  # счётчик
        cur = self.head  # текущий элемент - голова
        while cur:  # пока есть элементы
            count += 1  # увеличиваем счётчик
            cur = cur.next  # переходим к следующему элементу
        return count  # возвращаем длину списка

    def __repr__(self):  # вывод списка
        result = '['  # начало списка
        cur = self.head  # текущий элемент - голова
        count = 0  # счётчик
        while cur:  # пока есть элементы
            if count == 0:  # если счётчик равен 0
                result += str(cur.value)  # добавляем значение текущего элемента в строку
                count += 1  # увеличиваем счётчик
            else:  # если счётчик не равен 0
                result += ', ' + str(cur.value)  # добавляем запятую и значение текущего элемента в строку
            cur = cur.next  # переходим к следующему элементу
        result += ']'
        return result

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __getitem__(self, index):
        if 0 < index < len(self):
            count = 0
            cur = self.head
            while cur:
                if index == count:
                    return cur.value
                cur = cur.next
                count += 1
        else:
            raise IndexError("out of range")

    def __setitem__(self, index, value):
        if 0 <= index < len(self):
            count = 0
            cur = self.head
            while cur:
                if index == count:
                    cur.value = value
                    break
                cur = cur.next
                count += 1
        else:
            raise IndexError("out of range")
