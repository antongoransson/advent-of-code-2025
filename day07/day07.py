import sys
sys.path.append('..')
import aoc

def solve_part(start, grid):
    max_r,_  = aoc.get_max_size(grid)
    curr = set([start])
    t = 0
    paths = set([start])
    for r in range(0, max_r + 2):
        new_curr = set()
        for p in curr:
            new_p = (p[0] + 1, p[1])
            if new_p in grid:
                new_p1 = (p[0] + 1, p[1] - 1)
                new_p2 = (p[0] + 1, p[1] + 1)
                new_curr.add(new_p1)
                new_curr.add(new_p2)
                paths.add(new_p1)
                paths.add(new_p2)
                t+=1
            else:
                new_curr.add(new_p)
                paths.add(new_p)
        curr = new_curr
    return t, paths

def solve_part_1(start, grid):
    return solve_part(start, grid)[0]
                

def solve_part_2(start, grid):
    paths = solve_part(start,grid)[1]
    max_r,_  = aoc.get_max_size(paths)
    return n_timelines(paths, start,max_r+1, {}) +1

def n_timelines(grid, node, target_r, memo):
    if node in memo:
        return memo[node]
    next_node = (node[0] + 1, node[1])
    if next_node[0] == target_r:
        return 0
    elif next_node in grid:
        s = n_timelines(grid, next_node, target_r, memo)
        memo[node] = s
        return s
    else:
        next_node_l = (next_node[0], next_node[1] -1)
        assert  next_node_l in grid
        next_node_r = (next_node[0], next_node[1] +1)
        assert  next_node_r in grid
        s_r = n_timelines(grid, next_node_r, target_r, memo)
        s_l = n_timelines(grid, next_node_l, target_r, memo)
        memo[node] = s_r + s_l + 1
        return s_r + s_l +1
    

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        lines = f.read().splitlines()
        grid = set()
        for r,l in enumerate(lines):
            for c, v in enumerate(l):
                if v == 'S':
                    start = (r,c)
                if v == '^':
                    grid.add((r,c))
    sol1 = solve_part_1(start, grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(start, grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
