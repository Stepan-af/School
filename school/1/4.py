from itertools import *
graph = [["A", "B"], ["A", "C"], ["B", "E"], ["B", "D"], ["E", "D"], ["E", "F"], ["D", "F"], ["C", "B"]]
table = [[1, 2], [1, 3], [1, 5], [1, 6], [2, 4], [2, 6], [3, 5], [4, 6]]
for i in permutations("ABCDEF"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("F") + 1)