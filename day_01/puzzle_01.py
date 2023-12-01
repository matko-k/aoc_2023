
def part_1():
    sum = 0

    with open('inputs/my_input_01.txt', 'r') as file:
        for line in file:
            num = ''
            for c in line:
                if c.isdigit():
                    num += c
                    break
            for c in reversed(line):
                if c.isdigit():
                    num += c
                    break
            sum += int(num)
    return sum

def part_2():
    sum = 0

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
               '1', '2', '3', '4', '5', '6', '7', '8', '9']
    with open('inputs/my_input_01.txt', 'r') as file:
        for line in file:
            found_numbers = {}
            for i in range(len(numbers)):
                pos = line.find(numbers[i])
                while pos != -1:
                    found_numbers[pos] = i
                    pos = line.find(numbers[i], pos+1)

            i = found_numbers[min(found_numbers.keys())]
            ii = found_numbers[max(found_numbers.keys())]
            first = (numbers[i + 9]) if i < 9 else numbers[i]
            last = (numbers[ii + 9]) if ii < 9 else numbers[ii]
            sum += int(first + last)

    return sum

if __name__ == "__main__":
    print(part_1())
    print(part_2())
