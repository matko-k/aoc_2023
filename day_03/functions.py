def is_symbol(c):
    return not (c.isdigit() or c == '.')


def is_symbol_adjacent(array, i, j):
    i_limit = len(array)
    j_limit = len(array[0])

    #check up left:
    if i > 0 and j > 0:
        if is_symbol(array[i-1][j-1]):
            return True
    #check up
    if i > 0:
        if is_symbol(array[i - 1][j]):
            return True
    #check up right
    if i > 0 and j < j_limit - 1:
        if is_symbol(array[i - 1][j + 1]):
            return True
    #check left
    if j > 0:
        if is_symbol(array[i][j - 1]):
            return True
    #check right
    if j < j_limit - 1:
        if is_symbol(array[i][j + 1]):
            return True
    #check bottom left
    if i < i_limit - 1 and j > 0:
        if is_symbol(array[i + 1][j - 1]):
            return True
    #check bottom
    if i < i_limit - 1:
        if is_symbol(array[i + 1][j]):
            return True
    #check bottom right
    if i < i_limit - 1 and j < j_limit - 1:
        if is_symbol(array[i + 1][j + 1]):
            return True


def is_surrounding_number(num, i, j):
    num_i = num[1]
    num_j_l = num[2]
    num_j_r = num[3]

    return abs(i - num_i) <= 1 and (abs(num_j_l - j) <= 1 or abs(num_j_r - j) <= 1)


def find_surrounding_numbers(all_numbers, i, j):
    surrounding_numbers = []

    for num in all_numbers:
        if is_surrounding_number(num, i, j):
            surrounding_numbers.append(num[0])

    return surrounding_numbers
