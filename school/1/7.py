from itertools import *
graph = [["A", "B"], ["B", "C"], ["B", "E"], ["B", "F"], ["F", "E"], ["E", "D"], ["D", "C"]]
table = [[1, 3], [1, 6], [2, 6], [3, 4], [3, 6], [4, 5], [5, 6]]
for i in permutations("ABCDEF"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("D") + 1)