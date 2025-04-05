from math import dist, atan

def phi(point, center):
    x, y = point
    xc, yc = center
    return atan((y - yc)/(x - xc))

base = ''
files = ['25_А.txt', '25_Б.txt']
centers = [(5, -9), (-10, -7)]
eps = [0.1, 0.1]
tasks = [0, 1]

for t in tasks:
    data = [tuple(map(float, line.replace(',', '.').split())) for line in open(base + files[t])]
    clusters = []
    while data:
        clusters.append([data.pop(0)])
        for p in clusters[-1]:
            neigb = [pt for pt in data if abs(phi(pt, centers[t]) - phi(p, centers[t])) < eps[t]]
            clusters[-1] += neigb
            for pt in neigb:
                data.remove(pt)
    #print(len(clusters), [len(c) for c in clusters])

    clust_centers = []
    for cl in clusters:
        dmin = 10**100
        c = None
        for p in cl:
            d = sum(dist(p, pt) for pt in cl)
            if d < dmin:
                dmin = d
                c = p
        clust_centers.append(c)

    px = sum(p[0] for p in clust_centers) / len(clust_centers)
    py = sum(p[1] for p in clust_centers) / len(clust_centers)
    print(int(abs(px) * 10_000), int(abs(py) * 10_000))