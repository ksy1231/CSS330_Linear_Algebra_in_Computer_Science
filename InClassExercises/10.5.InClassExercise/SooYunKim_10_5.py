# Problem 1:
def bin_list(n):
      if n == 0:
            return ['']
      else:
            return ['0'+i for i in bin_list(n-1)] + ['1'+i for i in bin_list(n-1)]
a = bin_list(3)
	
# Problem 2:
b = []
for i in range(ord('a'), ord('h')):
    b += chr(i)
	
# Problem 3:
d = {x:y for x, y in zip(b, a)}

# Problem 4:
def inv_dict(dict):
    return { dict[k]: k for k in dict.keys() }
def id(dict):
    v = list(dict.values())
    k = list(dict.keys())
    nd = {}
    for n in range(len(v)):
        nd[v[n]] = k[n]
        return nd
D = {'a': '000', 'b': '001', 'c': '010', 'd': '011', 'e': '100', 'f': '101', 'g': '110'}
i = inv_dict(D)

print("Problem 1 Answer:", a)
print("Problem 2 Answer:", b)
print("Problem 3 Answer:", d)
print("Problem 4 Answer:", i)
