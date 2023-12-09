
def process_report(report):
    processed = []
    curr = report
    while True:
        processed.append(curr)
        diff = [curr[i+1] - curr[i] for i in range(len(curr) - 1)]
        if all(x == 0 for x in diff):
            break
        curr = diff
    return processed


def parse_input(filename):
    reports = []
    with open(filename, 'r') as file:
        for line in file:
           reports.append([int(x) for x in line.strip().split()])

    return reports


def part_1():

    reports = parse_input('inputs/my_input_09.txt')
    processed = []
    for rep in reports:
        processed.append(process_report(rep))

    res = 0
    for prep in processed:
        x = 0
        for line in reversed(prep):
            x += line[-1]
        res += x

    return res


def part_2():

    reports = parse_input('inputs/my_input_09.txt')
    processed = []
    for rep in reports:
        processed.append(process_report(rep))

    res = 0
    for prep in processed:
        x = 0
        for line in reversed(prep):
            x = line[0] - x
        res += x

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
