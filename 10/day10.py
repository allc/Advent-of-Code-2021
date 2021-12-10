import argparse


pair = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def parse(line):
    stack = []
    err = 'None'
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if len(stack) == 0:
                err = c
                break
            else:
                p = stack[-1]
                if c == pair[p]:
                    stack.pop()
                else:
                    err = c
                    break
    return (stack, err)


def part1(input_file):
    err2score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        'None': 0
    }
    score = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            score += err2score[parse(line[:-1])[1]]
    return score


def part2(input_file):
    comp_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            stack, err = parse(line[:-1])
            if err == 'None':
                score = 0
                for c in reversed(stack):
                    score = score * 5 + comp_score[pair[c]]
                scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


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
