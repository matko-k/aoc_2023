
def state_to_str(springs, groups):
    res = ''
    for s in springs:
        res += s + '|'
    for num in groups:
        res += str(num) + '|'

    return res


def find_combinations(springs, groups, state_map):

    state_id = state_to_str(springs, groups)
    if state_id in state_map.keys():
        return state_map[state_id]

    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        return 0

    if len(groups) == 0:
        for sp in springs:
            if '#' in sp:
                return 0
        return 1

    next_springs = springs[0]
    next_group = groups[0]

    if len(next_springs) == next_group:
        if '#' in next_springs:
            return find_combinations(springs[1:], groups[1:], state_map)

    if len(next_springs) < next_group:
        if '#' in next_springs:
            return 0
        return find_combinations(springs[1:], groups, state_map)

    res = 0
    i = next_springs.find('?')
    if i >= 0:
        next_1 = next_springs[:i]
        next_2 = next_springs[i+1:]
        if len(next_1) > 0 and len(next_2) > 0:
            res += find_combinations([next_1] + [next_2] + springs[1:], groups, state_map)
        elif len(next_2) == 0 and len(next_1) > 0:
            res += find_combinations([next_1] + springs[1:], groups, state_map)
        elif len(next_1) == 0 and len(next_2) > 0:
            res += find_combinations([next_2] + springs[1:], groups, state_map)
        else:
            res += find_combinations(springs[1:], groups, state_map)

        next = next_1 + '#' + next_2
        res += find_combinations([next] + springs[1:], groups, state_map)

    state_map[state_id] = res
    return res


def parse_input(filename, part2=False):
    springs = []
    groups = []
    with open(filename, 'r') as file:
        for line in file:
            spring = line.split(' ')[0]
            nums = [int(x) for x in line.split(' ')[1].strip().split(',')]
            if part2:
                total_spring = spring
                total_nums = nums.copy()
                for i in range(4):
                    total_spring += '?' + spring
                    total_nums.extend(nums)
                spring = total_spring
                nums = total_nums
            springs.append([x for x in spring.strip('.').split('.') if x])
            groups.append(nums)

    return springs, groups


def part_1():
    springs, groups = parse_input('inputs/my_input_12.txt')
    sum = 0
    for i in range(len(springs)):
        state_map = {}
        sum += find_combinations(springs[i], groups[i], state_map)

    return sum


def part_2():
    springs, groups = parse_input('inputs/my_input_12.txt', True)
    sum = 0
    for i in range(len(springs)):
        state_map = {}
        sum += find_combinations(springs[i], groups[i], state_map)

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
