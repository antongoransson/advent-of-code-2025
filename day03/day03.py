import sys
sys.path.append('..')


def solve_part_1(in_data):
     return solve(in_data, 2)

def solve_part_2(in_data):
    return solve(in_data, 12)

def solve(in_data, size):
    t = 0
    for l in in_data:
        x, pos= '', 0
        for i in range(size):
           n, pos = find_largest_n(l, pos, i, size)     
           x += n
        t += int(x)
    return t

def find_largest_n(n_in, start, p, tot_size):
    l = len(n_in)
    n = None
    pos = None
    for i in range(start, l):
        v = n_in[i]
        if i > (l - (tot_size - p)):
            break
        if n is None or v > n:
            n = v
            pos = i
    return n, pos + 1

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [line.strip() for line in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
