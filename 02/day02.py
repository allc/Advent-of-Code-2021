import argparse


def part1(input_file):
    x = 0
    y = 0
    with open(input_file) as f:
        for line in f.readlines():
            action, distance = line.split()
            if action == 'forward':
                x += int(distance)
            elif action == 'down':
                y += int(distance)
            elif action == 'up':
                y -= int(distance)
    return x * y


def part2(input_file):
    x = 0
    y = 0
    aim = 0
    with open(input_file) as f:
        for line in f.readlines():
            action, distance = line.split()
            if action == 'forward':
                x += int(distance)
                y += int(distance) * aim
            elif action == 'down':
                aim += int(distance)
            elif action == 'up':
                aim -= int(distance)
    return x * y


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('part', choices=['part1', 'part2'])
    argparser.add_argument('--input_file', default='input.txt')
    args = argparser.parse_args()
    func_dict = {
        'part1': part1,
        'part2': part2
    }
    print(func_dict[args.part](args.input_file))
    