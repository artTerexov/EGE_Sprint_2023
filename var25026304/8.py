from itertools import product

s = list(product("АВОРТ", repeat=6))


print(s.index(('В', 'О', 'Р', 'О', 'Т', 'А')))
