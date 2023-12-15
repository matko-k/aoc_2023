
def do_HASH(string):
    res = 0
    for ch in string:
        res += ord(ch)
        res *= 17
        res %= 256

    return res


def do_HASHMAP(step, boxes):

    if '-' in step:
        lbl = step.strip('-')
        box = boxes[do_HASH(lbl)]
        for lens in reversed(box):
            if lens[0] == lbl:
                box.remove(lens)
                return

    if '=' in step:
        lbl = step.split('=')[0]
        foc = step.split('=')[1]
        box = boxes[do_HASH(lbl)]
        for i in range(len(box)):
            if box[i][0] == lbl:
                box[i] = (lbl, foc)
                return
        box.append((lbl, foc))


def parse_input(filename):

    with open(filename, 'r') as file:
        steps = list(file.readline().strip().split(','))

    return steps


def part_1():

    steps = parse_input('inputs/my_input_15.txt')
    results = [do_HASH(x) for x in steps]

    return sum(results)


def part_2():
    steps = parse_input('inputs/my_input_15.txt')

    boxes = {}
    for x in range(256):
        boxes.setdefault(x, [])
    for step in steps:
        do_HASHMAP(step, boxes)

    res = 0
    for x in range(256):
        for i in range(len(boxes[x])):
            res += (1 + x) * (1 + i) * int(boxes[x][i][1])

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
