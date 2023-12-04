import math


def count_cards(cards, index, ):
    if cards[index] == 0:
        return 0

    sum = cards[index]
    for i in range(1, cards[index] + 1):
        sum += count_cards(cards, index + i)

    return sum

def part_1():
    sum = 0

    with open('inputs/my_input_04.txt', 'r') as file:
        for line in file:
            win_nums = [int(x) for x in list(line.split(':')[1].split('|')[0].split())]
            my_nums = [int(x) for x in list(line.split(':')[1].split('|')[1].split())]
            count = 0
            for my_num in my_nums:
                if my_num in win_nums:
                    count += 1
            sum += math.pow(2, count-1) if count > 0 else 0

    return sum


def part_2():
    sum = 0
    cards = []

    with open('inputs/my_input_04.txt', 'r') as file:
        for line in file:
            win_nums = [int(x) for x in list(line.split(':')[1].split('|')[0].split())]
            my_nums = [int(x) for x in list(line.split(':')[1].split('|')[1].split())]
            count = 0
            for my_num in my_nums:
                if my_num in win_nums:
                    count += 1
            cards.append(count)

    for i in range(len(cards)):
        sum += 1 + count_cards(cards, i)
    return sum


if __name__ == "__main__":
    print(part_1())
    print(part_2())
