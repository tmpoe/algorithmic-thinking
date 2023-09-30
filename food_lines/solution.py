
def get_shortest_line_index(lines: list):
    return lines.index(min(lines))

if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = list(map(int, input().split()))

    for _ in range(m):
        print(get_shortest_line_index(lines))
        lines[get_shortest_line_index(lines)] += 1