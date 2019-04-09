# Problem 1:
a = [chr(d) for d in range(ord('a'), ord('h'))]

# Problem 2:
b = [str(d0) + str(d1) + str(d2) for d0 in range(2) for d1 in range(2) for d2 in range(2)]

# Problem 3:
d = {k:v for (k, v) in zip(a, b)}

# Problem 4:
i = {d[key]: key for key in d.keys()}

print("Problem 1 Answer:", a)
print("Problem 2 Answer:", b)
print("Problem 3 Answer:", d)
print("Problem 4 Answer:", i)
