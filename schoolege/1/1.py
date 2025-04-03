from itertools import *
graph = [["a", "c"], ["a", "b"], ["c", "b"], ["b", "e"], ["b", "d"], ["d", "e"], ["e", "f"], ["d", "f"]]
table = [[1, 2], [1, 3], [1, 5], [1, 6], [2, 4], [2, 6], [3, 5], [4, 6]]
for i in permutations("abcdef"):
    if all([i[x - 1], i[y - 1]] in graph or [i[y - 1], i[x - 1]] in graph for x, y in table):
    # for x, y in i:
    #     if [i[x - 1], i[y - 1]] in graph:
        print(i.index("f") + 1)