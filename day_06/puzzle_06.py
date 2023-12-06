
def find_winning_strategies(race):
    total_time = race[0]
    dist_to_beat = race[1]
    win_strategies = []
    for hold_time in range(total_time):
        dist = hold_time * (total_time - hold_time)
        if dist > dist_to_beat:
            win_strategies.append((hold_time, dist))

    return win_strategies


def count_win_strategies(race):
    total_time = race[0]
    dist_to_beat = race[1]
    wins_count = 0
    for hold_time in range(total_time):
        dist = hold_time * (total_time - hold_time)
        if dist > dist_to_beat:
            wins_count = 2 * (int(total_time / 2) - hold_time + 1)
            wins_count -= 1 if total_time % 2 == 0 else 0
            break

    return wins_count


def part_1():
    res = 1
    with open('inputs/my_input_06.txt', 'r') as file:
        times = [int(x) for x in list(file.readline().split(':')[1].strip().split())]
        distances = [int(x) for x in list(file.readline().split(':')[1].strip().split())]
        races = list(zip(times, distances))

    for race in races:
        win_strategies = find_winning_strategies(race)
        # print(win_strategies)
        res *= len(win_strategies)

    return res


def part_2():

    with open('inputs/my_input_06.txt', 'r') as file:
        time = int(''.join(file.readline().split(':')[1].split()))
        distance = int(''.join(file.readline().split(':')[1].split()))
        race = (time, distance)

    res = count_win_strategies(race)
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
