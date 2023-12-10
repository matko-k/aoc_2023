
def get_next(curr, dir, pipeline):
    return curr[0] + dir[0], curr[1] + dir[1], pipeline[curr[1] + dir[1]][curr[0] + dir[0]]


def find_connecting(curr, dir, pipeline):
    if curr[2] == '-':
        if dir[0] > 0:
            return get_next(curr, dir, pipeline), dir
        return get_next(curr, dir, pipeline), dir

    if curr[2] == '|':
        if dir[1] > 0:
            return get_next(curr, dir, pipeline), dir
        return get_next(curr, dir, pipeline), dir

    if curr[2] == 'L':
        if dir[0] != 0:
            dir = (0, -1)
            return get_next(curr, dir, pipeline), dir
        dir = (1, 0)
        return get_next(curr, dir, pipeline), dir

    if curr[2] == 'J':
        if dir[0] != 0:
            dir = (0, -1)
            return get_next(curr, dir, pipeline), dir
        dir = (-1, 0)
        return get_next(curr, dir, pipeline), dir

    if curr[2] == '7':
        if dir[0] != 0:
            dir = (0, 1)
            return get_next(curr, dir, pipeline), dir
        dir = (-1, 0)
        return get_next(curr, dir, pipeline), dir

    if curr[2] == 'F':
        if dir[0] != 0:
            dir = (0, 1)
            return get_next(curr, dir, pipeline), dir
        dir = (1, 0)
        return get_next(curr, dir, pipeline), dir


def find_loop(start, dir, pipeline):
    curr = get_next(start, dir, pipeline)
    next_dir = dir
    loop = [curr]
    while True:
        if curr == start:
            return loop
        curr, next_dir = find_connecting(curr, next_dir, pipeline)
        loop.append(curr)


def parse_input(filename):
    pipeline = []
    start_x = 0
    start_y = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if 'S' in line:
                start_x = line.rfind('S')
                start_y = count
            count += 1
            pipeline.append([*line.strip()])

    return start_x, start_y, pipeline


def check_crosses_to_the_right(loop_points, start, row):
    crosses = {'|': 0, 'L': 0, 'J': 0, '7': 0, 'F': 0}
    for i in range(start[0] + 1, len(row)):
        if (i, start[1]) in loop_points:
            if row[i] in crosses.keys():
                crosses[row[i]] += 1

    full_crosses = crosses['|'] + min(crosses['L'], crosses['7']) + min(crosses['F'], crosses['J'])

    return full_crosses


def find_enclosed_tiles(loop_points, pipeline):
    tiles = 0
    for i in range(len(pipeline)):
        for j in range(len(pipeline[i])):
            if (j, i) in loop_points:
                continue
            crosses = check_crosses_to_the_right(loop_points, (j, i), pipeline[i])
            tiles += crosses % 2

    return tiles


def part_1():

    start_x, start_y, pipeline = parse_input('inputs/my_input_10.txt')

    # init_dir = (1, 0) # example
    init_dir = (-1, 0)
    loop = find_loop((start_x, start_y, 'S'), init_dir, pipeline)

    return len(loop) // 2


def part_2():
    start_x, start_y, pipeline = parse_input('inputs/my_input_10.txt')

    # init_dir = (-1, 0) # example
    init_dir = (-1, 0)
    loop = find_loop((start_x, start_y, 'S'), init_dir, pipeline)
    loop_points = [(x[0], x[1]) for x in loop]

    # pipeline[start_y][start_x] = '7' # example
    pipeline[start_y][start_x] = '7'

    enclosed_tiles = find_enclosed_tiles(loop_points, pipeline)
    return enclosed_tiles


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
