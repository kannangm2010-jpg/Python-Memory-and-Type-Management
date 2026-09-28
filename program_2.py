 #INTEGER DEMO

print("===== INTEGER DEMO =====\n")

a = 10
b = 10

print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))

print("Same memory?", a is b)

# Change value
b = b + 5

print("\nAfter change:")
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))

print("Same memory?", a is b)




















