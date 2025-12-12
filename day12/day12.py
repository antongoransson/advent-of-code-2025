import sys
sys.path.append('..')
import aoc


def solve_part_1(presents, trees):
    return len([1 for (r,c), n in trees if sum(len(p)*n[i] for i,p in enumerate(presents)) <= r*c])


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    presents = []
    trees=[]
    with open(in_f) as f:
        f = f.read().split('\n\n')
        parse_presents = f[:6]
        for p_i, p in enumerate(parse_presents):
            tp = p.split('\n')[1:]
            presents.append(set())
            for c, t in enumerate(tp):
                for r, x in enumerate(t):
                    if x == '#':
                        presents[p_i].add((c, r))
        for ct in f[6].split('\n'):
            ints = aoc.get_ints(ct)
            trees.append(((ints[0], ints[1]), ints[2:]))
    sol1 = solve_part_1(presents, trees)
    print(f'Part 1: {sol1}')

if __name__ == "__main__":
    main()
