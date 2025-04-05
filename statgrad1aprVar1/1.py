from itertools import *
graph = [["A", "B"], ["A", "C"], ["A", "F"], ["B", "C"], ["C", "E"], ["E", "G"], ["E", "D"], ["G", "D"], ["D", "F"]]
table = [[1, 3], [1, 4], [1, 6], [2, 4], [2, 5], [3, 6], [4, 5], [5, 7], [6, 7]]
for i in permutations("ABCDEFG"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("B") + 1, i.index("G") + 1)