from day_08.puzzle_08 import least_common_multiple as lcm


def push_button(modules, cycles=None, button_press_count=0):
    pulses = [('button', 'broadcaster', -1)]

    low_count = 0
    high_count = 0

    while len(pulses) > 0:
        source, target, signal = pulses.pop(0)
        # print(source, signal, target)

        if signal > 0:
            high_count += 1
        else:
            low_count += 1

        if not (target in modules.keys()):
            continue

        if modules[target][0] == 'B':
            for t in modules[target][1]:
                pulses.append((target, t, signal))
            continue

        if modules[target][0] == '%':
            if signal > 0:
                continue

            new_signal = -1 * modules[target][2]
            for t in modules[target][1]:
                pulses.append((target, t, new_signal))
            modules[target] = ('%', modules[target][1], new_signal, {})
            continue

        if modules[target][0] == '&':
            modules[target][3][source] = signal

            new_signal = 1 if -1 in modules[target][3].values() else -1

            if cycles and target in cycles.keys() and new_signal > 0:
                if cycles[target] < 0:
                    cycles[target] = button_press_count

            for t in modules[target][1]:
                pulses.append((target, t, new_signal))

    return low_count, high_count


def parse_input(filename):
    modules = {}
    with open(filename, 'r') as file:
        for line in file:
            module, destination = line.strip().split(' -> ')
            if module == 'broadcaster':
                type = 'B'
                id = module
            else:
                type = module[0]
                id = module[1:]

            state = -1
            input_states = {}
            modules[id] = (type, destination.split(', '), state, input_states)

    for mod in modules:
        for target in modules[mod][1]:
            if target in modules.keys():
                modules[target][3][mod] = -1

    return modules


def part_1():
    modules = parse_input('inputs/my_input_20.txt')

    button_count = 1000
    low_count = 0
    high_count = 0

    while button_count > 0:
        button_count += -1
        lc, hc = push_button(modules)
        low_count += lc
        high_count += hc

    return low_count * high_count


def part_2():
    modules = parse_input('inputs/my_input_20.txt')

    button_count = 0

    cycles = {}

    for mod in modules.values():
        if 'rx' in mod[1]:
            for src in mod[3].keys():
                cycles[src] = -1
            break

    while -1 in cycles.values():
        button_count += 1
        push_button(modules, cycles, button_count)

    res = 1
    for cycle in cycles.values():
        res = lcm(res, cycle)

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
