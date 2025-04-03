from itertools import *
graph = [["A", "B"], ["A", "C"], ["C", "B"], ["B", "F"], ["B", "E"], ["F", "E"], ["C", "D"], ["D", "E"]]
table = [[1, 3], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 6], [4, 6]]
for i in permutations("ABCDEF"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("A") + 1, i.index("F") + 1)