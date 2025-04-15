from itertools import *
graph = [["A", "B"], ["A", "E"], ["A", "F"], ["A", "G"], ["B", "F"], ["B", "E"], ["B", "C"],
         ["C", "D"], ["C", "H"], ["D", "H"], ["H", "G"]]
table = [[1, 3], [1, 8], [2, 4], [2, 7], [3, 8], [3, 5], [3, 8], [4, 6], [4, 7], [4, 8], [5, 7], [6, 7]]
for i in permutations("ABCDEFGH"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("B") + 1, i.index("F") + 1)
        print(i.index("B") + 1, i.index("E") + 1)