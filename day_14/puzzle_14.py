

def tilt_up(array):
    tilted = array

    in_movement = True

    while in_movement:
        in_movement = False
        for i in range(1, len(array)):
            for j in range(len(array[0])):
                if tilted[i][j] == 'O':
                    if tilted[i-1][j] in '.':
                        tilted[i-1][j], tilted[i][j] = 'O', '.'
                        in_movement = True

    return tilted


def tilt_down(array):
    tilted = array

    in_movement = True

    while in_movement:
        in_movement = False
        for i in range(len(array) - 1):
            for j in range(len(array[0])):
                if tilted[i][j] == 'O':
                    if tilted[i+1][j] in '.':
                        tilted[i+1][j], tilted[i][j] = 'O', '.'
                        in_movement = True

    return tilted


def tilt_left(array):
    tilted = array

    in_movement = True

    while in_movement:
        in_movement = False
        for i in range(len(array)):
            for j in range(1, len(array[0])):
                if tilted[i][j] == 'O':
                    if tilted[i][j-1] in '.':
                        tilted[i][j-1], tilted[i][j] = 'O', '.'
                        in_movement = True

    return tilted


def tilt_right(array):
    tilted = array

    in_movement = True

    while in_movement:
        in_movement = False
        for i in range(len(array)):
            for j in range(len(array[0]) - 1):
                if tilted[i][j] == 'O':
                    if tilted[i][j+1] in '.':
                        tilted[i][j+1], tilted[i][j] = 'O', '.'
                        in_movement = True

    return tilted


def get_load_up(array):

    load = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 'O':
                load += len(array) - i

    return load


def parse_input(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append([*line.strip()])

    return array


def find_result(results):
    seen = {}

    for i, val in enumerate(results):
        if val in seen:
            start = seen[val]
            end = i
            return results[start + (1000000000 - start) % (end-start) - 1]
        else:
            seen[val] = i

    return -1


def part_1():
    array = parse_input('inputs/my_input_14.txt')

    array = tilt_up(array)
    res = get_load_up(array)

    return res


def part_2():
    array = parse_input('inputs/my_input_14.txt')

    results = []

    for i in range(200):
        array = tilt_up(array)
        array = tilt_left(array)
        array = tilt_down(array)
        array = tilt_right(array)
        results.append(get_load_up(array))

    res = find_result(results)
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
