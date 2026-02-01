# module_random.py
import random

# Angka integer random
print("Angka integer random:", random.randint(1, 10)) # 1-10
print("Angka integer random:", random.randint(1, 10)) # 1-10
print("Angka integer random:", random.randint(1, 10)) # 1-10

# Angka float random
print("Random 0.0-1.0:", random.random()) # 0.0-1.0
print("Angka float random:", random.uniform(1, 10)) # 1-10
print("Angka float random:", random.uniform(1, 10)) # 1-10
print("Angka float random:", random.uniform(1, 10)) # 1-10

# Pilihan acak dari list
print("Pilihan acak dari list:", random.choice([1, 2, 3, 4, 5])) # 1-5
print("Pilihan acak dari list:", random.choice([1, 2, 3, 4, 5])) # 1-5
print("Pilihan acak dari list:", random.choice([1, 2, 3, 4, 5])) # 1-5

# Pilihan acak dari string
print("Pilihan acak dari string:", random.choice("hello")) # h, e, l, o
print("Pilihan acak dari string:", random.choice("hello")) # h, e, l, o
print("Pilihan acak dari string:", random.choice("hello")) # h, e, l, o

# Pilihan acak dari tuple
print("Pilihan acak dari tuple:", random.choice((1, 2, 3, 4, 5))) # 1-5
print("Pilihan acak dari tuple:", random.choice((1, 2, 3, 4, 5))) # 1-5
print("Pilihan acak dari tuple:", random.choice((1, 2, 3, 4, 5))) # 1-5

# Pilihan acak dari set (harus dikonversi ke list dulu)
print("Pilihan acak dari set:", random.choice(list({1, 2, 3, 4, 5}))) # 1-5
print("Pilihan acak dari set:", random.choice(list({1, 2, 3, 4, 5}))) # 1-5
print("Pilihan acak dari set:", random.choice(list({1, 2, 3, 4, 5}))) # 1-5

# Pilihan acak dari dictionary keys (harus dikonversi ke list dulu)
print("Pilihan acak dari dictionary:", random.choice(list({1: "a", 2: "b", 3: "c"}.keys()))) # 1-3
print("Pilihan acak dari dictionary:", random.choice(list({1: "a", 2: "b", 3: "c"}.keys()))) # 1-3
print("Pilihan acak dari dictionary:", random.choice(list({1: "a", 2: "b", 3: "c"}.keys()))) # 1-3

# Pilihan acak dari list of strings
print("Pilihan acak dari list of strings:", random.choice(["a", "b", "c", "d", "e"])) # a-e
print("Pilihan acak dari list of strings:", random.choice(["a", "b", "c", "d", "e"])) # a-e
print("Pilihan acak dari list of strings:", random.choice(["a", "b", "c", "d", "e"])) # a-e

# Pilihan acak dari list of tuples
print("Pilihan acak dari list of tuples:", random.choice([(1, 2), (3, 4), (5, 6)])) # (1,2), (3,4), (5,6)
print("Pilihan acak dari list of tuples:", random.choice([(1, 2), (3, 4), (5, 6)])) # (1,2), (3,4), (5,6)
print("Pilihan acak dari list of tuples:", random.choice([(1, 2), (3, 4), (5, 6)])) # (1,2), (3,4), (5,6)

# Pilihan acak dari list of dictionaries
print("Pilihan acak dari list of dictionaries:", random.choice([{"a": 1}, {"b": 2}, {"c": 3}])) # {"a": 1}, {"b": 2}, {"c": 3}
print("Pilihan acak dari list of dictionaries:", random.choice([{"a": 1}, {"b": 2}, {"c": 3}])) # {"a": 1}, {"b": 2}, {"c": 3}
print("Pilihan acak dari list of dictionaries:", random.choice([{"a": 1}, {"b": 2}, {"c": 3}])) # {"a": 1}, {"b": 2}, {"c": 3}

# Pilihan acak dari list of lists
print("Pilihan acak dari list of lists:", random.choice([[1, 2], [3, 4], [5, 6]])) # [1,2], [3,4], [5,6]
print("Pilihan acak dari list of lists:", random.choice([[1, 2], [3, 4], [5, 6]])) # [1,2], [3,4], [5,6]
print("Pilihan acak dari list of lists:", random.choice([[1, 2], [3, 4], [5, 6]])) # [1,2], [3,4], [5,6]

# Pilihan acak dari list of tuples of strings
print("Pilihan acak dari list of tuples of strings:", random.choice([("a", "b"), ("c", "d"), ("e", "f")])) # ("a","b"), ("c","d"), ("e","f")
print("Pilihan acak dari list of tuples of strings:", random.choice([("a", "b"), ("c", "d"), ("e", "f")])) # ("a","b"), ("c","d"), ("e","f")
print("Pilihan acak dari list of tuples of strings:", random.choice([("a", "b"), ("c", "d"), ("e", "f")])) # ("a","b"), ("c","d"), ("e","f")

# Pilihan acak dari list of tuples of dictionaries
print("Pilihan acak dari list of tuples of dictionaries:", random.choice([({"a": 1}, {"b": 2}), ({"c": 3}, {"d": 4}), ({"e": 5}, {"f": 6})])) # ({"a":1},{"b":2}), ({"c":3},{"d":4}), ({"e":5},{"f":6})
print("Pilihan acak dari list of tuples of dictionaries:", random.choice([({"a": 1}, {"b": 2}), ({"c": 3}, {"d": 4}), ({"e": 5}, {"f": 6})])) # ({"a":1},{"b":2}), ({"c":3},{"d":4}), ({"e":5},{"f":6})
print("Pilihan acak dari list of tuples of dictionaries:", random.choice([({"a": 1}, {"b": 2}), ({"c": 3}, {"d": 4}), ({"e": 5}, {"f": 6})])) # ({"a":1},{"b":2}), ({"c":3},{"d":4}), ({"e":5},{"f":6})

# Pilihan acak dari list of tuples of lists
print("Pilihan acak dari list of tuples of lists:", random.choice([([1, 2], [3, 4]), ([5, 6], [7, 8]), ([9, 10], [11, 12])])) # ([1,2],[3,4]), ([5,6],[7,8]), ([9,10],[11,12])
print("Pilihan acak dari list of tuples of lists:", random.choice([([1, 2], [3, 4]), ([5, 6], [7, 8]), ([9, 10], [11, 12])])) # ([1,2],[3,4]), ([5,6],[7,8]), ([9,10],[11,12])
print("Pilihan acak dari list of tuples of lists:", random.choice([([1, 2], [3, 4]), ([5, 6], [7, 8]), ([9, 10], [11, 12])])) # ([1,2],[3,4]), ([5,6],[7,8]), ([9,10],[11,12])

buah = ["mangga", "pisang", "jeruk", "anggur", "semangka"]
print("Pilihan acak dari list of strings:", random.choice(buah)) # mangga, pisang, jeruk, anggur, semangka
print("Pilihan acak dari list of strings:", random.choice(buah)) # mangga, pisang, jeruk, anggur, semangka
print("Pilihan acak dari list of strings:", random.choice(buah)) # mangga, pisang, jeruk, anggur, semangka