import sys

print("===== PYTHON PRIMITIVE DATA TYPES =====\n")




# SHOW INTEGER AS 1 BYTE

num = 5

binary = format(num, '08b')

print("Decimal:", num)
print("1 Byte Binary:", binary)





# NEGATIVE NUMBER IN 1 BYTE

num = -5

binary = format(num & 0xff, '08b')

print("Decimal:", num)
print("1 Byte Binary:", binary)