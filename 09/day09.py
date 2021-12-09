import argparse
import itertools


def part1(input_file):
    with open(input_file, 'r') as f:
        heightmap = [list(map(int, line[:-1])) for line in f.readlines()]
    result = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            adj_heights = []
            if row > 0:
                adj_heights.append(heightmap[row - 1][col])
            if row < len(heightmap) - 1:
                adj_heights.append(heightmap[row + 1][col])
            if col > 0:
                adj_heights.append(heightmap[row][col - 1])
            if col < len(heightmap[0]) - 1:
                adj_heights.append(heightmap[row][col + 1])
            if all([heightmap[row][col] < adj for adj in adj_heights]):
                result += heightmap[row][col] + 1
    return result


def part2(input_file):
    with open(input_file, 'r') as f:
        heightmap = [list(map(int, line[:-1])) for line in f.readlines()]
    graph = []
    for i in range(len(heightmap)):
        graph.append([(i, j) for j in range(len(heightmap[0]))])
    
    def union(graph, a, b):
        i, j = root(graph, a)
        graph[i][j] = root(graph, b)

    def root(graph, a):
        i, j = a
        if graph[i][j] != a:
            graph[i][j] = root(graph, graph[i][j])
        return graph[i][j]
        

    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            if heightmap[row][col] == 9:
                continue
            if row < len(heightmap) - 1:
                if heightmap[row + 1][col] < 9:
                    union(graph, (row, col), (row + 1, col))
            if col < len(heightmap[0]) - 1:
                if heightmap[row][col + 1] < 9:
                    union(graph, (row, col), (row, col + 1))

    count = {}
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            f = root(graph, (i, j))
            if f in count:
                count[f] += 1
            else:
                count[f] = 1
    areas = sorted(count.values(), reverse=True)
    return areas[0] * areas[1] * areas[2]


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
