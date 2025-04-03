from itertools import *
graph = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "D"], ["D", "E"],
        ["E", "F"]]
table = [[1, 3], [1, 5], [1, 6], [2, 6], [3, 4], [4, 6]]
for i in permutations("ABCDEF"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("C") + 1, i.index("D") + 1)