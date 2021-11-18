# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq  # алгоритм очереди кучи
from collections import Counter, namedtuple


# класс ветвей дерева
class Node(namedtuple('Node', ['left', 'right'])):
    def go(self, c, pr):
        self.left.go(c, pr + '0')
        self.right.go(c, pr + '1')


# класс потомков
class Child(namedtuple('Child', ['ch'])):
    def go(self, c, pr):
        c[self.ch] = pr or '0'


# код Хаффмана
def huffman(s):
    # переменная под очередь с приоритетами
    h = []

    # очередь по частоте символа
    for ch, fr in Counter(s).items():
        h.append((fr, len(h), Child(ch)))

    # очередь с приоритетами
    heapq.heapify(h)
    n = len(h)

    # набор элементов по частоте
    while len(h) > 1:
        fr1, n1, left = heapq.heappop(h)
        fr2, n2, right = heapq.heappop(h)
        heapq.heappush(h, (fr1 + fr2, n, Node(left, right)))
        n += 1

    # словарь кодов символов
    c = {}

    # заполнение словаря
    if h:
        [(fr3, n3, kor)] = h
        kor.go(c, '')
    return c


s = 'hello world python'
h = huffman(s)
print(''.join(h[i] for i in s))
