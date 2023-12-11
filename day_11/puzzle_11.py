
def expand_universe(universe):
    expanded_rows = []
    for row in universe:
        expanded_rows.append(row)
        if all(x == '.' for x in row):
            expanded_rows.append(row)

    expanded_rows = list(map(list, zip(*expanded_rows)))

    expanded_columns = []
    for row in expanded_rows:
        expanded_columns.append(row)
        if all(x == '.' for x in row):
            expanded_columns.append(row)

    expanded = list(map(list, zip(*expanded_columns)))

    return expanded


def expand_universe_2(universe):
    expanded_rows = []
    for row in universe:
        if all(x == '.' for x in row):
            expanded_rows.append(list('o' * len(row)))
            continue
        expanded_rows.append(row)

    expanded_rows = list(map(list, zip(*expanded_rows)))

    expanded_columns = []
    for row in expanded_rows:
        if all(x in '.o' for x in row):
            expanded_columns.append(list('o' * len(row)))
            continue
        expanded_columns.append(row)

    expanded = list(map(list, zip(*expanded_columns)))

    return expanded


def parse_input(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append([*line.strip()])

    return array


def part_1():

    expanded_universe = expand_universe(parse_input('inputs/my_input_11.txt'))
    galaxies = []
    for i in range(len(expanded_universe)):
        for j in range(len(expanded_universe[0])):
            if expanded_universe[i][j] == '#':
                galaxies.append((j, i))

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

    return sum


def part_2():
    expanded_universe = expand_universe_2(parse_input('inputs/my_input_11.txt'))
    galaxies = []
    exp = 1000000
    for i in range(len(expanded_universe)):
        for j in range(len(expanded_universe[0])):
            if expanded_universe[i][j] == '#':
                galaxies.append((j, i))

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            x1 = min(galaxies[i][0], galaxies[j][0])
            x2 = max(galaxies[i][0], galaxies[j][0])
            y1 = min(galaxies[i][1], galaxies[j][1])
            y2 = max(galaxies[i][1], galaxies[j][1])
            path = 0
            for k in range(x1 + 1, x2 + 1):
                path += exp if expanded_universe[y1][k] == 'o' else 1
            for l in range(y1 + 1, y2 + 1):
                path += exp if expanded_universe[l][x1] == 'o' else 1
            sum += path

    return sum


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
