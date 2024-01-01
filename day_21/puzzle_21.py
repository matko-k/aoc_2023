
def find_destinations(array, start, steps, is_limited):
    odd_count = 0
    even_count = 0

    width = len(array[0])
    height = len(array)

    explorers = [start]

    explored = set()

    while steps >= 0:
        new_explorers = []
        for pos in explorers:

            if is_limited and (pos[0] < 0 or pos[0] > len(array[0])-1 or pos[1] < 0 or pos[1] > len(array)-1):
                continue

            if array[pos[1] % height][pos[0] % width] == '#':
                continue
            if pos in explored:
                continue
            explored.add(pos)

            if steps % 2 > 0:
                odd_count += 1
            else:
                even_count += 1

            next_dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for next_dir in next_dirs:
                new_explorers.append((pos[0] + next_dir[0], pos[1] + next_dir[1]))

        explorers = new_explorers
        steps -= 1

    return odd_count, even_count


def parse_input(filename):
    array = []
    with open(filename, 'r') as file:
        for lc, line in enumerate(file):
            array.append([*line.strip()])
            if 'S' in line:
                start = (line.find('S'), lc)

    return array, start


def part_1():
    array, start = parse_input('inputs/my_input_21.txt')
    steps = 64

    odd_count, even_count = find_destinations(array, start, steps, True)
    res = odd_count if steps % 2 > 0 else even_count

    return res


def part_2():
    array, start = parse_input('inputs/my_input_21.txt')
    steps = 26501365

    assert len(array) == len(array[0])
    side = len(array)
    full = steps // side
    rest = steps % side

    full_odd, full_even = find_destinations(array, start, 130, True)
    count = [full_odd, full_even] if rest % 2 > 0 else [full_even, full_odd]

    res = count[0]
    for i in range(1, full + 1):
        res += 4 * i * count[i % 2]
    res -= full

    corner_starts = [(0, 0), (0, side-1), (side-1, 0), (side-1, side-1)]

    corners_in = 1
    for cs in corner_starts:
        corners_in += find_destinations(array, cs, rest - 1, True)[1]

    corners_out = 1
    for cs in corner_starts:
        corners_out += find_destinations(array, cs, rest - 1, True)[0] + 1

    res += full * corners_in
    res -= (full + 1) * corners_out

    return res


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
