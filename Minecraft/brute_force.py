import math

min = math.inf


def build_wall(n, c, d, m, wall):
    global min
    min = math.inf
    build_wall_bt(n, c, d, m, wall, 0, -1)
    return min


def build_wall_bt(n, c, d, m, wall, cost, last_action):
    global min
    if len(set(wall)) == 1 and wall[0] == n:
        if cost < min:
            min = cost
        return
    if cost >= min:
        return
    for i in range(len(wall)):
        if wall[i] < n:
            if last_action != 1:
                wall[i] += 1
                build_wall_bt(n, c, d, m, wall, cost + c, 0)
                wall[i] -= 1
        if wall[i] > n:
            if last_action != 0:
                wall[i] -= 1
                build_wall_bt(n, c, d, m, wall, cost + d, 1)
                wall[i] += 1
        if wall[i] > 1:
            for j in range(len(wall)):
                if i != j and wall[j] < n:
                    if last_action != 2:
                        wall[i] -= 1
                        wall[j] += 1
                        build_wall_bt(n, c, d, m, wall, cost + m, 2)
                        wall[i] += 1
                        wall[j] -= 1
    

def main():
    # n, c, d, m = map(int, input().split())
    n, c, d, m = [5, 3, 4, 1]
    # wall = list(map(int, input().split()))
    wall = [6, 6, 4, 4, 4, 4, 6]
    print(build_wall(n, c, d, m, wall))


if __name__ == "__main__":
    main()
