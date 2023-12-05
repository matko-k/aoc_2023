
def do_conversions(source, conversions):
    for i in range(len(source)):
        for c in conversions:
            if c[1] <= source[i] < c[1] + c[2]:
                source[i] = c[0] + source[i]-c[1]
                break


def do_conversion_on_range(source, conversions):
    result_ranges = []
    to_be_converted = [source]
    while len(to_be_converted) > 0:
        current_source = to_be_converted.pop()
        for c in sorted(conversions):
            s_start = current_source[0]
            s_range = current_source[1]
            s_end = s_start + s_range - 1
            c_start = c[1]
            c_range = c[2]
            c_end = c_start + c_range - 1
            c_dest = c[0]
            if c_start <= s_start <= c_end:
                new_start = c_dest + s_start - c_start

                if c_end >= s_end:
                    result_ranges.append((new_start, s_range))
                else:
                    result_ranges.append((new_start, s_range - (s_end - c_end)))
                    to_be_converted.append((c_end + 1, s_end - c_end))

    if len(result_ranges) == 0:
        result_ranges.append(source)
    return result_ranges


def part_1():

    with open('inputs/my_input_05.txt', 'r') as file:
        current = [int(x) for x in list(file.readline().split(':')[1].split())]
        conversions = []
        conversion_name = ''
        for line in file:
            if len(line.strip()) == 0:
                do_conversions(current, conversions)
                conversions = []
                conversion_name = file.readline().strip()
                continue
            conversions.append([int(x) for x in list(line.split())])
        do_conversions(current, conversions)
    return min(current)


def part_2():

    with open('inputs/my_input_05.txt', 'r') as file:
        initial = [int(x) for x in list(file.readline().split(':')[1].split())]
        start_seeds = initial[0::2]
        seed_ranges = initial[1::2]

        all_conversions = []
        conversions = []
        for line in file:
            if len(line.strip()) == 0:
                all_conversions.append(conversions)
                conversions = []
                conversion_name = file.readline().strip()
                continue
            conversions.append([int(x) for x in list(line.split())])
        all_conversions.append(conversions)

    min_seed_locations = []
    for i in range(len(start_seeds)):
        all_seed_ranges = [(start_seeds[i], seed_ranges[i])]
        for conversion_step in all_conversions:
            new_seed_ranges = []
            for seed_range in all_seed_ranges:
                split_seed_ranges = do_conversion_on_range(seed_range, conversion_step)
                for ssr in split_seed_ranges:
                    new_seed_ranges.append(ssr)
            all_seed_ranges = new_seed_ranges

        min_seed_locations.append(min(list(x[0] for x in all_seed_ranges)))

    return min(min_seed_locations)


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
