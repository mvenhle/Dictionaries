# A python program to combine two dictionary adding values for common keys
from collections import Counter
d1 = {'a': 100, 'b': 250, 'c': 300, 'd': 700}
d2 = {'a': 300, 'b': 200, 'd': 400, 'c': 200}
d = Counter(d1) + Counter(d2)
print(d)