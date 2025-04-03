from itertools import *
graph = [["A", "C"], ["C", "B"], ["C", "D"], ["B", "D"], ["B", "E"], ["B", "F"], ["E", "F"]]
table = [[1, 2], [1, 4], [2, 4], [3, 4], [3, 6], [4, 6], [5, 6]]
for i in permutations("ABCDEF"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("E") + 1, i.index("F") + 1)