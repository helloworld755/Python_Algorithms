# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

s = 'abcd'
subs = set()

for i in range(len(s)):
    for j in range(len(s), i, -1):
        subs.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(len(subs)-1)
