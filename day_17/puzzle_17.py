import queue


def parse_input(filename):

    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append([int(x) for x in line.strip()])

    return array


def find_heat_loss(array, start, end, min_steps, max_steps):

    closed = set()
    open = queue.PriorityQueue()
    open.put((0, (start, (1, 0), 1)))
    open.put((0, (start, (0, 1), 1)))

    while open:
        cost, current = open.get()

        if current in closed:
            continue
        closed.add(current)

        pos, direction, dir_count = current

        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if next_pos[0] > len(array[0]) - 1 or next_pos[0] < 0 or next_pos[1] > len(array) - 1 or next_pos[1] < 0:
            continue

        next_cost = cost + array[next_pos[1]][next_pos[0]]

        if next_pos == end:
            return next_cost

        possible_dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        possible_dirs.remove((-direction[0], -direction[1]))

        for next_dir in possible_dirs:
            next_dir_count = dir_count + 1
            if next_dir != direction:
                if dir_count < min_steps:
                    continue
                next_dir_count = 1

            if next_dir_count > max_steps:
                continue
            open.put((next_cost, (next_pos, next_dir, next_dir_count)))

    return -1


def part_1():

    array = parse_input('inputs/my_input_17.txt')
    start = (0, 0)
    end = (len(array[0]) - 1, len(array) - 1)

    heat_loss = find_heat_loss(array, start, end, 1,3)

    return heat_loss


def part_2():
    array = parse_input('inputs/my_input_17.txt')
    start = (0, 0)
    end = (len(array[0]) - 1, len(array) - 1)

    heat_loss = find_heat_loss(array, start, end, 4, 10)

    return heat_loss


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
