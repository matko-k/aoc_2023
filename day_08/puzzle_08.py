
def get_loops(network, instructions, start):
    loop_steps = 0
    curr = start
    while True:
        if curr[-1] == 'Z':
            return loop_steps
        dir = 0 if instructions[loop_steps % len(instructions)] == 'L' else 1
        loop_steps += 1
        curr = network[curr][dir]


def greatest_common_div(a, b):
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return a * b // greatest_common_div(a, b)


def parse_input(filename):
    network = {}
    with open(filename, 'r') as file:
        instructions = file.readline().strip()
        file.readline()
        for line in file:
            node = line.split(' = ')[0]
            left = line.split(' = ')[1].split(', ')[0].strip()[1:]
            right = line.split(' = ')[1].split(', ')[1].strip()[:-1]
            network[node] = (left, right)

    return instructions, network


def part_1():

    instructions, network = parse_input('inputs/my_input_08.txt')

    steps = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        dir = 0 if instructions[steps % len(instructions)] == 'L' else 1
        steps += 1
        curr = network[curr][dir]

    return steps


def part_2():
    instructions, network = parse_input('inputs/my_input_08.txt')

    starts = [node for node in network.keys() if node[-1] == 'A']
    loops = []
    for node in starts:
        loops.append(get_loops(network, instructions, node))

    res = 1
    for ll in loops:
        res = least_common_multiple(res, ll)

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
