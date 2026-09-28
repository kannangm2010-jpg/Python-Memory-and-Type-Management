# ==========================================
# PRIMITIVE DATA TYPES DEMO
# ==========================================

import sys

print("===== PYTHON PRIMITIVE DATA TYPES =====\n")

# -----------------------------------
# 1. INTEGER
# -----------------------------------
num = 10

print("INTEGER")
print("Value:", num)
print("Type:", type(num))
print("Memory Address:", id(num))
print("Size:", sys.getsizeof(num), "bytes")
print()

# -----------------------------------
# 2. FLOAT
# -----------------------------------
decimal_num = 10.5

print("FLOAT")
print("Value:", decimal_num)
print("Type:", type(decimal_num))
print("Memory Address:", id(decimal_num))
print("Size:", sys.getsizeof(decimal_num), "bytes")
print()

# -----------------------------------
# 3. COMPLEX
# -----------------------------------
complex_num = 2 + 3j

print("COMPLEX")
print("Value:", complex_num)
print("Type:", type(complex_num))
print("Memory Address:", id(complex_num))
print("Size:", sys.getsizeof(complex_num), "bytes")
print()

# -----------------------------------
# 4. BOOLEAN
# -----------------------------------
flag = True

print("BOOLEAN")
print("Value:", flag)
print("Type:", type(flag))
print("Memory Address:", id(flag))
print("Size:", sys.getsizeof(flag), "bytes")
print()

# -----------------------------------
# 5. STRING
# -----------------------------------
text = "Python"

print("STRING")
print("Value:", text)
print("Type:", type(text))
print("Memory Address:", id(text))
print("Size:", sys.getsizeof(text), "bytes")
print()

# -----------------------------------
# STRING SIZE CHANGE
# -----------------------------------
small = "Hi"
large = "Hello Python Programming"

print("STRING SIZE COMPARISON")
print("Small String Size:", sys.getsizeof(small), "bytes")
print("Large String Size:", sys.getsizeof(large), "bytes")
print()

print("===== END =====")





# SHOW INTEGER AS 1 BYTE

num = 10

binary = format(num, '08b')

print("Decimal:", num)
print("1 Byte Binary:", binary)


# NEGATIVE NUMBER IN 1 BYTE

num = -10

binary = format(num & 0xff, '08b')

print("Decimal:", num)
print("1 Byte Binary:", binary)