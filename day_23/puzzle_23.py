import sys


def find_paths(graph, curr, exit, path, visited):
    path = path + [curr]

    if curr[0] == exit:
        return [path]

    paths = []

    for next in graph[curr[0]]:
        if next[0] in visited:
            continue
        visited.append(next[0])
        new_paths = find_paths(graph, next, exit, path, visited)
        visited.remove(next[0])
        for new_path in new_paths:
            paths.append(new_path)

    return paths


def find_nodes(array, curr, exit, nodes, last_node, previous, dist, directions_checked={}, part_2=False):
    sys.setrecursionlimit(100000)
    if curr == exit:
        if last_node not in nodes.keys():
            nodes[last_node] = set()
        nodes[last_node].add((curr, dist))
        return

    neighbours = []

    next = (curr[0] - 1, curr[1])
    bad_symbols = '#' if part_2 else '>#'
    if next != previous and next[0] >= 0 and array[next[1]][next[0]] not in bad_symbols:
        neighbours.append(next)

    next = (curr[0] + 1, curr[1])
    bad_symbols = '#' if part_2 else '<#'
    if next != previous and next[0] < len(array[0]) and array[next[1]][next[0]] not in bad_symbols:
        neighbours.append(next)

    next = (curr[0], curr[1] - 1)
    bad_symbols = '#' if part_2 else 'v#'
    if next != previous and next[1] >= 0 and array[next[1]][next[0]] not in bad_symbols:
        neighbours.append(next)

    next = (curr[0], curr[1] + 1)
    bad_symbols = '#' if part_2 else '^#'
    if next != previous and next[1] < len(array) and array[next[1]][next[0]] not in bad_symbols:
        neighbours.append(next)

    if len(neighbours) == 1:
        find_nodes(array, neighbours[0], exit, nodes, last_node, curr, dist + 1, directions_checked, part_2)
    else:
        for next in neighbours:
            if last_node not in nodes.keys():
                nodes[last_node] = set()
            nodes[last_node].add((curr, dist))

            if curr not in directions_checked:
                directions_checked[curr] = set()
            if next in directions_checked[curr]:
                continue
            directions_checked[curr].add(next)
            find_nodes(array, next, exit, nodes, curr, curr, 0, directions_checked, part_2)

    return


def parse_input(filename):
    array = []
    with open(filename, 'r') as file:
        for lc, line in enumerate(file):
            array.append([*line.strip()])

    return array


def part_1():
    array = parse_input('inputs/my_input_23.txt')

    start = (array[0].index('.'), 0)
    exit = (array[-1].index('.'), len(array) - 1)

    nodes = {start: set()}

    find_nodes(array, start, exit, nodes, start, start, 0)
    paths = find_paths(nodes, (start, 0), exit, [], [])

    path_lengths = []
    for path in paths:
        path_lengths.append(sum(x[1] for x in path) + len(path) - 2)

    return max(path_lengths)


def part_2():
    array = parse_input('inputs/my_input_23.txt')

    start = (array[0].index('.'), 0)
    exit = (array[-1].index('.'), len(array) - 1)
    nodes = {start: set()}

    find_nodes(array, start, exit, nodes, start, start, 0, {}, True)
    for node, nodelets in nodes.items():
        for n in nodelets:
            if n[0] == exit:
                new_exit = node
                added_length = n[1]
                break

    paths = find_paths(nodes, (start, 0),  new_exit, [], [])

    path_lengths = []
    for path in paths:
        path_lengths.append(sum(x[1] for x in path) + len(path) - 2)

    return max(path_lengths) + added_length + 1


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
