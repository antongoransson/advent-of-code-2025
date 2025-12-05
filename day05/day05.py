import sys
sys.path.append('..')
import aoc

def get_merged_range(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    if s1 <= s2 <=e1 <=e2:
        return s1, e2
    elif s1 <= s2 <=e2 <=e1:
        return s1, e1
    elif s2 <= s1 <=e2 <=e1:
        return s2, e1
    elif s2 <= s1 <=e1 <=e2:
        return s2, e2
    return None, None


def solve_part_1(ranges, fresh):
    return len(set(f for f in fresh for s, e in ranges if s <= f <= e))


def solve_part_2(ranges):
    while True:
        new_ranges=set()
        for r1 in ranges:
            merged_r = False
            for r2 in ranges:
                if r1 == r2:
                    continue
                s_n, e_n = get_merged_range(r1, r2)
                if s_n is not None:
                    merged_r = True
                    new_ranges.add((s_n, e_n))
            if not merged_r:
                new_ranges.add(r1)
        if len(ranges) == len(new_ranges):
            return sum(e-s+1 for s,e in ranges)
        ranges = new_ranges

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        ranges, ids = f.read().split('\n\n')
        ids = [int(i) for i in ids.split('\n')]
        ranges = set(tuple(map(int, r.split('-'))) for r in  ranges.split('\n'))
    sol1 = solve_part_1(ranges, ids)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(ranges)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
