import sys
sys.path.append('..')
import aoc


def solve_part_1(grid):
    return len([p for p in grid if len(aoc.neighbours(grid, p, True)) < 4])

def solve_part_2(grid:dict):
    t = 0
    changed = True
    while changed:
        changed = False
        for p in [k for k in grid.keys()]:
            if len(aoc.neighbours(grid, p, True)) < 4:
                del grid[p]
                t += 1
                changed = True
    return t


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        grid = {(r,c): v for r, line in enumerate(f) for c,v in enumerate(line.strip()) if v == '@'}
    sol1 = solve_part_1(grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
