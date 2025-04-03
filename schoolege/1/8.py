from itertools import *
graph = [["К", "Р"], ["Р", "М"], ["Р", "С"], ["Р", "П"], ["П", "Т"], ["П", "Л"], ["П", "С"],
        ["Т", "С"], ["Л", "С"], ["К", "С"]]
table = [[1, 3], [1, 5], [2, 3], [2, 4], [2, 5], [2, 7], [3, 5], [3, 6], [5, 7]]
for i in permutations("КМРПСЛТ"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
        print(i.index("П") + 1, i.index("Л") + 1)
        # print(i.index("П") + 1, i.index("Т") + 1)