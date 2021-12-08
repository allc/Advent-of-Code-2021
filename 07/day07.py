import argparse
import statistics


def part1(input_file):
    with open(input_file, 'r') as f:
        positions = list(map(int, f.readline().split(',')))
    min_fuel = float('inf')
    for align in range(min(positions), max(positions) + 1):
        fuel = 0
        for p in positions:
            fuel += abs(align - p)
        min_fuel = min(min_fuel, fuel)
    return min_fuel


def part2(input_file):
    with open(input_file, 'r') as f:
        positions = list(map(int, f.readline().split(',')))
    min_fuel = float('inf')
    for align in range(min(positions), max(positions) + 1):
        fuel = 0
        for p in positions:
            move = abs(align - p)
            fuel += (1 + move) * move // 2
        min_fuel = min(min_fuel, fuel)
    return min_fuel


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
    