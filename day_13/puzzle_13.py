
def find_mirror_line(field, skip=-1):
    base = [field[0]]

    for i in range(1, len(field)):
        max_size = min(len(base), len(field) - len(base))
        mirror = True
        for j in range(max_size):
            row_1 = base[-1-j]
            row_2 = field[i+j]
            if row_1 != row_2:
                mirror = False
                break
        if mirror and i != skip:
            return i
        base.append(field[i])

    return -1


def parse_input(filename):

    with open(filename, 'r') as file:
        fields = []
        field = []
        for line in file:
            if len(line.strip()) == 0:
                fields.append(field)
                field = []
                continue
            field.append([*line.strip()])
        fields.append(field)

    return fields


def part_1():
    fields = parse_input('inputs/my_input_13.txt')

    sum = 0
    for field in fields:
        res = find_mirror_line(field)
        if res >= 0:
            sum += 100*res
            continue
        field = list(map(list, zip(*field)))
        res = find_mirror_line(field)
        sum += res

    return sum


def part_2():
    fields = parse_input('inputs/my_input_13.txt')
    scores = []

    for field in fields:
        res = find_mirror_line(field)
        if res >= 0:
            scores.append(100*res)
            continue
        field = list(map(list, zip(*field)))
        res = find_mirror_line(field)
        scores.append(res)

    index = 0
    sum = 0
    for field in fields:
        i = 0
        found = False
        while i < len(field) and not found:
            j = 0
            while j < len(field[0]) and not found:
                test_field = [row[:] for row in field]
                test_field[i][j] = '#' if test_field[i][j] == '.' else '.'
                res = find_mirror_line(test_field, scores[index] // 100)
                if res >= 0:
                    sum += res*100
                    found = True
                    continue
                test_field = list(map(list, zip(*test_field)))
                res = find_mirror_line(test_field, scores[index])
                if res >= 0:
                    sum += res
                    found = True
                    continue
                j += 1
            i += 1
        index += 1
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
