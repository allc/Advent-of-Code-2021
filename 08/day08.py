import argparse
import itertools


def part1(input_file):
    count = 0
    segs = [2, 3, 4, 7]
    with open(input_file, 'r') as f:
        for line in f.readlines():
            for disp in line[:-1].split()[-4:]:
                if len(disp) in segs:
                    count += 1
    return count


def part2(input_file):
    # segment_count2positions = {
    #     2: [(set(2, 5), 1)], # 1
    #     3: [(set(0, 2, 5), 7)], # 7
    #     4: [(set(1, 2, 3, 5), 4)], # 4
    #     5: [(set(0, 2, 3, 4, 6), 2), (set(0, 2, 3, 5, 6), 3), (set(0, 1, 3, 5, 6), 5)], # 2, 3, 5
    #     6: [(set(0, 1, 2, 4, 5, 6), 0), (set(0, 1, 3, 4, 5, 6), 6), (set(0, 1, 2, 3, 5, 6), 9)], # 0, 6, 9
    #     7: [(set(0, 1, 2, 3, 4, 5, 6), 8)] # 8
    # }
    position2value = {
        (0, 1, 2, 4, 5, 6): 0,
        (2, 5): 1,
        (0, 2, 3, 4, 6): 2,
        (0, 2, 3, 5, 6): 3,
        (1, 2, 3, 5): 4,
        (0, 1, 3, 5, 6): 5,
        (0, 1, 3, 4, 5, 6): 6,
        (0, 2, 5): 7,
        (0, 1, 2, 3, 4, 5, 6): 8,
        (0, 1, 2, 3, 5, 6): 9
    }
    result = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line[:-1].split()
            patterns = line[:10]
            signals = line[-4:]
            for p in itertools.permutations('abcdefg'):
                segment2position = {}
                for i, s in enumerate(p):
                    segment2position[s] = i
                can_parse = True
                for pattern in patterns:
                    position = tuple(sorted([segment2position[seg] for seg in pattern]))
                    if position not in position2value:
                        can_parse = False
                        break
                if can_parse:
                    intermediate_result = 0
                    for i, signal in enumerate(signals):
                        position = tuple(sorted([segment2position[seg] for seg in signal]))
                        if position in position2value:
                            intermediate_result += 10 ** (3 - i) * position2value[position]
                        else:
                            can_parse = False
                            break
                    if can_parse:
                        result += intermediate_result
                        break
    return result


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
    