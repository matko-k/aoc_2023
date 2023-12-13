
def is_spring_valid(spring, groups):
    s = ''

    for c in spring:
        if c != '.' or not s or c != s[-1]:
            s += c

    sections = s.strip('.').split('.')
    if len(sections) != len(groups):
        return False

    for i in range(len(sections)):
        if len(sections[i]) != groups[i]:
            return False

    return True


def find_combinations(spring, groups):
    if '?' not in spring:
        return 1 if is_spring_valid(spring, groups) else 0

    i = spring.find('?')
    return (find_combinations(spring[:i] + '.' + spring[i+1:], groups)
            + find_combinations(spring[:i] + '#' + spring[i+1:], groups))


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
            springs.append(spring)
            groups.append(nums)

    return springs, groups


def part_1():
    springs, groups = parse_input('inputs/example_12.txt')
    sum = 0

    for i in range(len(springs)):
        sum += find_combinations(springs[i], groups[i])

    return sum


def part_2():
    springs, groups = parse_input('inputs/example_12.txt', True)
    sum = 0

    # for i in range(len(springs)):
    #     sum += find_combinations(springs[i], groups[i])
    #
    # return sum


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
