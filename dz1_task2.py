# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

bit_or = int(bin(5), 2) | int(bin(6), 2)
bit_and = int(bin(5), 2) & int(bin(6), 2)
bit_xor = int(bin(5), 2) ^ int(bin(6), 2)

print("OR: %s" % bin(bit_or))
print("AND: %s" % bin(bit_and))
print("XOR: %s" % bin(bit_xor))

right_5 = bin(5 >> 2)
print(right_5)

left_5 = bin(5 << 2)
print(left_5)
