from functions import *

def part_1():
    sum = 0

    array = []
    # with open('inputs/example_03.txt', 'r') as file:
    with open('inputs/my_input_03.txt', 'r') as file:
        for line in file:
            array.append(list(line.strip()))

    for i in range(len(array)):
        numbers = []
        positions = []
        current = ''
        for j in range(len(array[i])):
            if not array[i][j].isdigit():
                if len(current) > 0:
                    numbers.append(int(current))
                    positions[-1] = (positions[-1][0], j - 1)
                    current = ''
                    continue
            else:
                if len(current) == 0:
                    positions.append((j, -1))
                current += array[i][j]
        if len(current) > 0:
            numbers.append(int(current))
            positions[-1] = (positions[-1][0], len(array[i]) - 1)
        # print(numbers)
        # print(positions)
        for k in range(len(numbers)):
            for j in range(positions[k][0], positions[k][1] + 1):
                if is_symbol_adjacent(array, i, j):
                    sum += numbers[k]
                    break

    return sum


def part_2():
    sum = 0

    array = []
    # with open('inputs/example_03.txt', 'r') as file:
    with open('inputs/my_input_03.txt', 'r') as file:
        for line in file:
            array.append(list(line.strip()))

    all_numbers = []
    for i in range(len(array)):
        numbers = []
        positions = []
        current = ''
        for j in range(len(array[i])):
            if not array[i][j].isdigit():
                if len(current) > 0:
                    numbers.append(int(current))
                    positions[-1] = positions[-1][:2] + (j - 1,)
                    current = ''
                    continue
            else:
                if len(current) == 0:
                    positions.append((i, j, -1))
                current += array[i][j]
        if len(current) > 0:
            numbers.append(int(current))
            positions[-1] = positions[-1][:2] + (len(array[i]) - 1,)
        # print(numbers)
        # print(positions)

        for k in range(len(numbers)):
            all_numbers.append((numbers[k],) + positions[k])

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '*':
                surrounding_numbers = find_surrounding_numbers(all_numbers, i, j)
                if len(surrounding_numbers) == 2:
                    sum += surrounding_numbers[0] * surrounding_numbers[1]

    return sum


if __name__ == "__main__":
    print(part_1())
    print(part_2())
