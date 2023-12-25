import queue
import sys


def cut_most_visited_edge(graph):
    sorted_keys = sorted(graph.keys())
    visited = {}
    for i in range(len(sorted_keys) - 1):
        for j in range(i + 1, len(sorted_keys)):
            visited[sorted_keys[i] + sorted_keys[j]] = 0

    for node in graph.keys():
        paths = dijkstra(graph, node)
        for end_node in graph.keys():
            if end_node == node:
                continue
            current = end_node
            while True:
                next = paths[current]
                if not next:
                    break
                key = current + next if next > current else next + current
                visited[key] = visited[key] + 1
                current = next

    most_visited = sorted(visited.items(), key=lambda x: x[1])[-1][0]
    first = most_visited[:3]
    second = most_visited[3:]
    graph[first].remove(second)
    graph[second].remove(first)
    print(first, second)
    return first, second


def dijkstra(graph, start):
    open = queue.PriorityQueue()
    open.put((0, start))
    distances = {node: sys.maxsize for node in graph.keys()}
    distances[start] = 0
    paths = {node: None for node in graph.keys()}
    closed = set()

    while not open.empty():
        dist, node = open.get()

        if node in closed:
            continue
        closed.add(node)

        if dist > distances[node]:
            continue

        for next in graph[node]:
            if dist + 1 < distances[next]:
                distances[next] = dist + 1
                paths[next] = node
                open.put((dist + 1, next))

    return paths


def parse_input(filename):
    wiring = {}
    with open(filename, 'r') as file:
        for line in file:
            node = line.strip().split(': ')[0]
            connections = set(list(line.strip().split(': ')[1].split()))

            if node in wiring:
                wiring[node].update(connections)
            else:
                wiring[node] = connections

            for c in connections:
                if c in wiring:
                    wiring[c].update([node])
                else:
                    wiring[c] = set([node])

    return wiring


def part_1():
    wiring = parse_input('inputs/my_input_25.txt')

    for i in range(3):
        cut1, cut2 = cut_most_visited_edge(wiring)

    group1 = dijkstra(wiring, cut1)
    group2 = dijkstra(wiring, cut2)

    res1 = sum(1 for n in group1 if group1[n]) + 1
    res2 = sum(1 for n in group2 if group2[n]) + 1

    return res1 * res2


def part_2():

    return


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
