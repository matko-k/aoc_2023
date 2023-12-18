
def get_real_vertices(commands):
    p = (0, 0)
    points = [p]

    for c in commands:
        hex = c[2]
        dist = int(hex[:-1], 16)
        dir = int(hex[-1])
        if dir == 0:
            p = (p[0] + dist, p[1])
        elif dir == 2:
            p = (p[0] - dist, p[1])
        elif dir == 3:
            p = (p[0], p[1] + dist)
        elif dir == 1:
            p = (p[0], p[1] - dist)
        points.append(p)

    return points[:-1]


def get_outline_vertices(commands):
    p = (0, 0)
    points = [p]

    for c in commands:
        if c[0] == 'R':
            p = (p[0] + int(c[1]), p[1])
        elif c[0] == 'L':
            p = (p[0] - int(c[1]), p[1])
        elif c[0] == 'U':
            p = (p[0], p[1] + int(c[1]))
        elif c[0] == 'D':
            p = (p[0], p[1] - int(c[1]))
        points.append(p)

    return points[:-1]


def get_area(v):
    area = 0
    for i in range(len(v) - 1):
        area += v[i][0] * v[i+1][1] - v[i+1][0] * v[i][1]
    area += v[-1][0] * v[0][1] - v[0][0] * v[-1][1]
    return abs(area) // 2


def get_outline_len(v):
    l = 0
    p = v[0]
    for i in range(1, len(v)):
        l += abs(v[i][0] - p[0]) + abs(v[i][1] - p[1])
        p = v[i]
    l += abs(v[-1][0] - v[0][0]) + abs(v[-1][1] - v[0][1])
    return l


def parse_input(filename):

    commands = []
    with open(filename, 'r') as file:
        for line in file:
            dir, dist, color = line.strip().split()
            color = ''.join(filter(lambda c: c not in '#()', color))
            commands.append((dir, dist, color))

    return commands


def part_1():

    commands = parse_input('inputs/my_input_18.txt')
    vertices = get_outline_vertices(commands)

    return get_area(vertices) + get_outline_len(vertices) // 2 + 1


def part_2():

    commands = parse_input('inputs/my_input_18.txt')
    vertices = get_real_vertices(commands)

    return get_area(vertices) + get_outline_len(vertices) // 2 + 1


if __name__ == "__main__":
    import time

    start = time.time()
    print(part_1())
    end = time.time()
    print(f"part1: {1000*(end-start)} ms")

    start = time.time()
    print(part_2())
    end = time.time()
    print(f"part2: {1000*(end-start)} ms")
