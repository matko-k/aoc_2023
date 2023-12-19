
def get_accepted_ranges(wf_id, workflows, ranges):
    if wf_id == 'A':
        res = 1
        for _, r in ranges.items():
            res *= r[1] - r[0] + 1
        return res

    if wf_id == 'R':
        return 0

    wf = workflows[wf_id]
    remaining_ranges = {**ranges}

    res = 0

    for check in wf[:-1]:
        dest = check[3]
        range_id = check[0]
        val = check[2]
        next_ranges = {**remaining_ranges}
        low, high = next_ranges[range_id]
        if check[1] < 0:
            next_ranges[range_id] = (low, val - 1)
            remaining_ranges[range_id] = (val, high)
        else:
            next_ranges[range_id] = (val + 1, high)
            remaining_ranges[range_id] = (low, val)

        res += get_accepted_ranges(dest, workflows, next_ranges)

    res += get_accepted_ranges(wf[-1], workflows, remaining_ranges)

    return res


def do_workflow(wf, part):
    for check in wf[:-1]:
        ls = part[check[0]]
        rs = check[2]
        res = ls < rs if check[1] < 0 else ls > rs
        if res:
            return check[3]

    return wf[-1]


def parse_input(filename):
    workflows = {}
    parts = []
    with open(filename, 'r') as file:
        switch = True
        for line in file:
            if len(line.strip()) == 0:
                switch = False
                continue

            if switch:
                id = line.strip().split('{')[0]
                flows = line.strip().split('{')[1].strip('}').split(',')
                wf = []
                for flow in flows[:-1]:
                    dest = flow.split(':')[1]
                    expr = flow.split(':')[0]
                    operation = -1 if '<' in expr else 1
                    operands = expr.split('<') if operation < 0 else expr.split('>')
                    wf.append((operands[0], operation, int(operands[1]), dest))
                wf.append(flows[-1])
                workflows[id] = wf
                continue

            pts = line.strip('{}\n').split(',')
            part = {}
            for p in pts:
                id = p.split('=')[0]
                val = int(p.split('=')[1])
                part[id] = val
            parts.append(part)

    return workflows, parts


def part_1():
    workflows, parts = parse_input('inputs/my_input_19.txt')

    result = 0

    for part in parts:
        res = 'in'
        while res not in ['A', 'R']:
            res = do_workflow(workflows[res], part)
        if res == 'A':
            result += part['x'] + part['m'] + part['a'] + part['s']

    return result


def part_2():
    workflows, parts = parse_input('inputs/my_input_19.txt')

    ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

    result = get_accepted_ranges('in', workflows, ranges)

    return result


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
