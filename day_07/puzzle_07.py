from functools import cmp_to_key


def get_card_power(card, use_jokers=False):
    if card.isdigit():
        return int(card)
    if card == 'T':
        return 10
    if card == 'J':
        return 1 if use_jokers else 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14


def get_hand_type(hand, use_jokers=False):
    hand_map = {}
    for card in hand[0]:
        if card in hand_map:
            hand_map[card] += 1
        else:
            hand_map[card] = 1

    jokers = 0
    if use_jokers:
        jokers = hand_map.pop('J', 0)
        if jokers == 5:
            return 7

    card_counts = []
    for _, card_count in hand_map.items():
        card_counts.append(card_count)
    card_counts = sorted(card_counts, reverse=True)
    card_counts[0] = card_counts[0] + jokers

    if len(card_counts) == 1:
        return 7 # 5 of a kind

    if len(card_counts) == 2:
        if card_counts[0] == 4:
            return 6 # 4 of a kind
        return 5 # full house

    if len(card_counts) == 3:
        if card_counts[0] == 3:
            return 4 # 3 of a kind
        return 3 # 2 pairs

    if len(card_counts) == 4:
        return 2 # 1 pair

    return 1 # high card


def hand_sort(hand1, hand2, use_jokers=False):
    hand_type_1 = get_hand_type(hand1, use_jokers)
    hand_type_2 = get_hand_type(hand2, use_jokers)

    type_diff = hand_type_1 - hand_type_2
    if type_diff != 0:
        return type_diff

    for i in range(5):
        if get_card_power(hand1[0][i], use_jokers) != get_card_power(hand2[0][i], use_jokers):
            return get_card_power(hand1[0][i], use_jokers) - get_card_power(hand2[0][i], use_jokers)

    return 0 # hands are equal


def hand_sort2(hand1, hand2):
    return hand_sort(hand1, hand2, True)


def part_1():

    hands = []
    with open('inputs/my_input_07.txt', 'r') as file:
        for line in file:
            cards, bid = line.split()
            hands.append((cards, bid))

    res = 0
    i = 1
    sorted_hands = sorted(hands, key=cmp_to_key(hand_sort))
    for hand in sorted_hands:
        res += int(hand[1]) * i
        i += 1

    return res


def part_2():

    hands = []
    with open('inputs/my_input_07.txt', 'r') as file:
        for line in file:
            cards, bid = line.split()
            hands.append((cards, bid))

    res = 0
    i = 1
    sorted_hands = sorted(hands, key=cmp_to_key(hand_sort2))
    for hand in sorted_hands:
        res += int(hand[1]) * i
        i += 1

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
