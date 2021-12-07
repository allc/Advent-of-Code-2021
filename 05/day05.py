import argparse


def part1(input_file):
    lines = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            l = l[:-1].split(' -> ')
            x1, y1 = map(int, l[0].split(','))
            x2, y2 = map(int, l[1].split(','))
            lines.append((x1, y1, x2, y2))
    ocean_floor = []
    for _ in range(1000):
        ocean_floor.append([0] * 1000)
    count = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                ocean_floor[x1][y] += 1
                if ocean_floor[x1][y] == 2:
                    count += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                ocean_floor[x][y1] += 1
                if ocean_floor[x][y1] == 2:
                    count += 1
    return count


def part2(input_file):
    lines = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            l = l[:-1].split(' -> ')
            x1, y1 = map(int, l[0].split(','))
            x2, y2 = map(int, l[1].split(','))
            lines.append((x1, y1, x2, y2))
    ocean_floor = []
    ocean_floor_size = 1000
    for _ in range(ocean_floor_size):
        ocean_floor.append([0] * ocean_floor_size)
    count = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                ocean_floor[x1][y] += 1
                if ocean_floor[x1][y] == 2:
                    count += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                ocean_floor[x][y1] += 1
                if ocean_floor[x][y1] == 2:
                    count += 1
        elif x1 < x2:
            if y1 < y2:
                for i in range(x2 - x1 + 1):
                    ocean_floor[x1 + i][y1 + i] += 1
                    if ocean_floor[x1 + i][y1 + i] == 2:
                        count += 1
            else:
                for i in range(x2 - x1 + 1):
                    ocean_floor[x1 + i][y1 - i] += 1
                    if ocean_floor[x1 + i][y1 - i] == 2:
                        count += 1
        else:
            if y1 < y2:
                for i in range(x1 - x2 + 1):
                    ocean_floor[x1 - i][y1 + i] += 1
                    if ocean_floor[x1 - i][y1 + i] == 2:
                        count += 1
            else:
                for i in range(x1 - x2 + 1):
                    ocean_floor[x1 - i][y1 - i] += 1
                    if ocean_floor[x1 - i][y1 - i] == 2:
                        count += 1
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
    