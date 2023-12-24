
# copied from chatGPT, I wanted to avoid using solver lib
def gauss_elimination(A, B):
    n = len(B)

    # Augment the matrix A with the column vector B
    augmented_matrix = [A[i] + [B[i]] for i in range(n)]

    # Perform Gaussian elimination
    for i in range(n):
        # Make the diagonal element 1
        diag_elem = augmented_matrix[i][i]
        augmented_matrix[i] = [elem / diag_elem for elem in augmented_matrix[i]]

        # Eliminate other elements in the current column
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(augmented_matrix[i], augmented_matrix[j])]

    # Extract the solution vector
    solution = [row[-1] for row in augmented_matrix]

    return solution


def find_intersection(h1, h2):
    x1, y1, _ = h1[0]
    x2, y2, _ = h2[0]
    dx1, dy1, _ = h1[1]
    dx2, dy2, _ = h2[1]

    a1 = dy1/dx1
    a2 = dy2/dx2
    b1 = y1 - a1*x1
    b2 = y2 - a2*x2

    if a1 == a2:
        return None, None

    x = (b2 - b1) / (a1 - a2)
    return x, a1*x + b1


def parse_input(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z = [int(x) for x in line.strip().split(' @ ')[0].split(', ')]
            vx, vy, vz = [int(x) for x in line.strip().split(' @ ')[1].split(', ')]
            array.append(((x, y, z), (vx, vy, vz)))

    return array


def part_1():
    hailstones = parse_input('inputs/my_input_24.txt')

    low_limit = 200000000000000
    high_limit = 400000000000000
    count = 0
    for i in range(len(hailstones) - 1):
        for j in range(i + 1, len(hailstones)):
            h1 = hailstones[i]
            h2 = hailstones[j]
            x, y = find_intersection(h1, h2)

            if not x:
                continue
            t1 = (x - h1[0][0]) / h1[1][0]
            t2 = (x - h2[0][0]) / h2[1][0]

            if t1 < 0 or t2 < 0:
                continue

            if low_limit <= x <= high_limit and low_limit <= y <= high_limit:
                count += 1

    return count


def part_2():
    hailstones = parse_input('inputs/my_input_24.txt')
    
    x1, y1, z1 = hailstones[0][0]
    vx1, vy1, vz1 = hailstones[0][1]
    x2, y2, z2 = hailstones[1][0]
    vx2, vy2, vz2 = hailstones[1][1]
    x3, y3, z3 = hailstones[2][0]
    vx3, vy3, vz3 = hailstones[2][1]

    # matrices parameters found on paper + Google
    A = [
        [-(vy1 - vy2), vx1 - vx2, 0, y1 - y2, -(x1 - x2), 0],
        [-(vy1 - vy3), vx1 - vx3, 0, y1 - y3, -(x1 - x3), 0],
        [0, -(vz1 - vz2), vy1 - vy2, 0, z1 - z2, -(y1 - y2)],
        [0, -(vz1 - vz3), vy1 - vy3, 0, z1 - z3, -(y1 - y3)],
        [-(vz1 - vz2), 0, vx1 - vx2, z1 - z2, 0, -(x1 - x2)],
        [-(vz1 - vz3), 0, vx1 - vx3, z1 - z3, 0, -(x1 - x3)]
    ]

    B = [
        (y1 * vx1 - y2 * vx2) - (x1 * vy1 - x2 * vy2),
        (y1 * vx1 - y3 * vx3) - (x1 * vy1 - x3 * vy3),
        (z1 * vy1 - z2 * vy2) - (y1 * vz1 - y2 * vz2),
        (z1 * vy1 - z3 * vy3) - (y1 * vz1 - y3 * vz3),
        (z1 * vx1 - z2 * vx2) - (x1 * vz1 - x2 * vz2),
        (z1 * vx1 - z3 * vx3) - (x1 * vz1 - x3 * vz3)
    ]

    rock = gauss_elimination(A, B)
    return round(sum(rock[:3]))


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
