import argparse


def part1(input_file):
    count = 0
    last = float('inf')
    with open(input_file) as f:
        for line in f.readlines():
            depth = int(line)
            if depth > last:
                count += 1
            last = depth
    return count


def part2(input_file):
    with open(input_file) as f:
        depths = list(map(int, f.readlines()))
    count = 0
    last = float('inf')
    for i in range(len(depths) - 2):
        window_sum = sum(depths[i: i + 3])
        if window_sum > last:
            count += 1
        last = window_sum
    return count


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
    