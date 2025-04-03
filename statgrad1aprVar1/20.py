def moves(p):
    a, b = p
    return (a - 2, b), (a, b - 2), (a // 3, b), (a, b // 3)

def gameover(pos):
    return sum(pos) <= 150

def win1(pos):
    return not gameover(pos) and any(gameover(m) for m in moves(pos))

def lose1(pos):
    return all(win1(m) for m in moves(pos))
def lose1_bad(pos):
    return any(win1(m) for m in moves(pos))

def win2(pos):
    return not win1(pos) and any(lose1(m) for m in moves(pos))

def lose2(pos):
    return all(win1(m) or win2(m) for m in moves(pos)) and any(win2(m) for m in moves(pos))

z19 = [s for s in range(135, 10000) if lose1_bad([17, s])]
z20 = [s for s in range(135, 10000) if win2([17, s])]
z21 = [s for s in range(135, 10000) if lose2([17, s])]
print(max(z19))
print(z20[0], z20[1])
print(min(z21))