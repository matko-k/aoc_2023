

def bounce_beams(array, beams, energized, beam_states):
    while len(beams) > 0:

        curr_x, curr_y, dir_x, dir_y = beams.pop()
        
        beams_state = ''
        beams_state += str(curr_x)+'|'+str(curr_y)+'|'+str(dir_x)+'|'+str(dir_y)
        if beams_state in beam_states:
            continue
        beam_states.append(beams_state)

        next_x, next_y = curr_x + dir_x, curr_y + dir_y
        
        if next_x < 0 or next_y < 0 or next_x >= len(array[0]) or next_y >= len(array):
            continue

        energized.add((next_x, next_y))
        next_char = array[next_y][next_x]

        if next_char == '.':
            next_beam = (next_x, next_y, dir_x, dir_y)
            beams.extend([next_beam])

        elif next_char == '|':
            if dir_x == 0:
                next_beam = (next_x, next_y, dir_x, dir_y)
                beams.extend([next_beam])
            else:
                next_beam_up = (next_x, next_y, 0, 1)
                next_beam_down = (next_x, next_y, 0, -1)
                beams.extend([next_beam_up, next_beam_down])

        elif next_char == '-':
            if dir_x == 0:
                next_beam_left = (next_x, next_y, -1, 0)
                next_beam_right = (next_x, next_y, 1, 0)
                beams.extend([next_beam_left, next_beam_right])
            else:
                next_beam = (next_x, next_y, dir_x, dir_y)
                beams.extend([next_beam])

        elif next_char == '/':
            if dir_x == 0:
                next_beam = (next_x, next_y, -dir_y, 0)
                beams.extend([next_beam])
            else:
                next_beam = (next_x, next_y, 0, -dir_x)
                beams.extend([next_beam])

        elif next_char == '\\':
            if dir_x == 0:
                next_beam = (next_x, next_y, dir_y, 0)
                beams.extend([next_beam])
            else:
                next_beam = (next_x, next_y, 0, dir_x)
                beams.extend([next_beam])


def parse_input(filename):

    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append([*line.strip()])

    return array


def part_1():

    array = parse_input('inputs/my_input_16.txt')
    start_beam = (-1, 0, 1, 0)
    beams = [start_beam]
    beam_states = []
    energized = set()

    bounce_beams(array, beams, energized, beam_states)

    return len(energized)


def part_2():

    array = parse_input('inputs/my_input_16.txt')
    res = 0
    for i in range(len(array)):
        start_beam = (-1, i, 1, 0)
        beams = [start_beam]
        beam_states = []
        energized = set()

        bounce_beams(array, beams, energized, beam_states)
        res = max(res, len(energized))


        start_beam = (len(array[0]), i, -1, 0)
        beams = [start_beam]
        beam_states = []
        energized = set()

        bounce_beams(array, beams, energized, beam_states)
        res = max(res, len(energized))

    for i in range(len(array[0])):
        start_beam = (i, -1, 0, 1)
        beams = [start_beam]
        beam_states = []
        energized = set()

        bounce_beams(array, beams, energized, beam_states)
        res = max(res, len(energized))

        start_beam = (i, len(array), 0, -1)
        beams = [start_beam]
        beam_states = []
        energized = set()

        bounce_beams(array, beams, energized, beam_states)
        res = max(res, len(energized))

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
