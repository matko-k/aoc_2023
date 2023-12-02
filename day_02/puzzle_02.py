
def is_within_limits(color, amount):
    limit_red = 12
    limit_green = 13
    limit_blue = 14

    if color == 'red':
        return amount <= limit_red
    if color == 'green':
        return amount <= limit_green
    if color == 'blue':
        return amount <= limit_blue

def part_1():
    sum = 0

    with open('inputs/my_input_02.txt', 'r') as file:
        for line in file:
            line_split = line.split(':')
            game_id = int(line_split[0].split()[-1])
            rounds = line_split[1].split(';')
            possible = True
            for round in rounds:
                cubes = round.split(',')
                for cube in cubes:
                    color = cube.split()[1]
                    amount = int(cube.split()[0])
                    if not is_within_limits(color, amount):
                        possible = False
                        break
            if possible:
                sum += game_id

    return sum
def part_2():
    sum = 0

    with open('inputs/my_input_02.txt', 'r') as file:
        for line in file:
            line_split = line.split(':')
            game_id = int(line_split[0].split()[-1])
            rounds = line_split[1].split(';')
            game_max = {'red': 0, 'green': 0, 'blue': 0}
            for round in rounds:
                cubes = round.split(',')
                for cube in cubes:
                    color = cube.split()[1]
                    amount = int(cube.split()[0])
                    game_max[color] = max(game_max[color], amount)
            game_power = game_max['red'] * game_max['green'] * game_max['blue']
            sum += game_power

    return sum

if __name__ == "__main__":
    print(part_1())
    print(part_2())
