from itertools import combinations
import sys
sys.path.append('..')
import aoc


def solve_part_1(tiles):
    return max((abs(x2-x1)+1)*(abs(y2-y1)+1) for (x1,y1),(x2,y2) in combinations(tiles, 2))

def solve_part_2(tiles):
    green_tiles = set()
    m_grid = minimize_grid(tiles)
    s_grid,v_map = to_sorted_grid(m_grid,tiles)
    c_t = s_grid[0]
    print(s_grid)
    add_green_tiles(s_grid[-1], s_grid[0], green_tiles)
    for t in s_grid[1:]:
        add_green_tiles(c_t, t, green_tiles)
        c_t = t
    m = -1
    flood_fill((1750,1750), green_tiles)
    print_grid(s_grid, green_tiles)
    for (x1,y1),(x2,y2) in combinations(s_grid, 2):
        x3,y3 = x1,y2
        x4,y4 = x2,y1
        if is_inside((x1,y1), (x3,y3), (x2,y2), (x4,y4), green_tiles):
            xx1,yy1 = v_map[(x1,y1)]
            xx2,yy2 = v_map[(x2,y2)]
            a = (abs(xx2-xx1)+1)*(abs(yy2-yy1)+1)
            m = max(m,a)
    return m

def is_ok(p1,p2, green_tiles):
    min_c = min(p1[0],p2[0])
    max_c = max(p1[0],p2[0])
    min_r = min(p1[1],p2[1])
    max_r = max(p1[1],p2[1])
    if min_r == max_r:
        for cc in range(min_c, max_c +1):
            if (cc,min_r) not in green_tiles:
                return False
        return True
    elif min_c == max_c:
        for rr in range(min_r, max_r +1):
            if (min_c,rr) not in green_tiles:
                return False
        return True
    else:
        assert False
    
def is_inside(p1,p2,p3,p4, green_tiles):
    return is_ok(p1,p2, green_tiles) and is_ok(p2,p3, green_tiles) and is_ok(p3,p4, green_tiles) and is_ok(p4,p1, green_tiles)

def to_sorted_grid(minimized, original):
    new_list = []
    m = {}
    for t in original:
        for k in minimized:
            moved = minimized[k]
            if (k[0], k[1]) == t:
                new_list.append((k[0] - moved[0], k[1]- moved[1]))
                m[(k[0] - moved[0], k[1]- moved[1])] = k
    assert len(original) == len(new_list)
    return new_list, m
    
def minimize_grid(tiles):
    min_c, min_r, max_c, max_r = aoc.get_size(tiles)
    rr = min_r
    new_tiles = {t:(0,0) for t in tiles}
    rows = set([t[1] for t in new_tiles])
    while rr <= max_r:
        has_point = rr in rows
        if not has_point:
            for t in new_tiles.keys():
                moved = new_tiles[t]
                if t[1] > rr:
                    new_tiles[(t[0], t[1])] = (moved[0], moved[1]+1)
        rr+=1
    cc = min_c
    cols = set([t[0] for t in new_tiles])
    while cc <= max_c:
        has_point = cc in cols
        if not has_point:
            for t in new_tiles.keys():
                moved = new_tiles[t]
                if t[0] > cc:
                    new_tiles[(t[0], t[1])] = (moved[0]+1, moved[1])
        cc+=1
    return new_tiles
    
            

def neighbours(p, diag=False):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diag:
        deltas += [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    x, y = p
    neigbours = set()
    for dx, dy in deltas:
        xx = x + dx
        yy = y + dy
        neigbours.add((xx, yy))
    return neigbours

def flood_fill(s, green_tiles):
    q=[s]
    green_tiles.add(s)
    i=0
    while q:
        i+=1
        node = q.pop()
        ns = neighbours(node, True)
        for p in ns:
            if p in green_tiles:
                continue
            q.append(p)
            green_tiles.add(p)
        if i % 10000==0:
            print('qsize: {}'.format(len(q)), 'area: {}'.format(len(green_tiles)))
        
def print_grid(tiles, green_tiles):
    min_c = min(x for x, y in tiles)
    max_c = max(x for x, y in tiles)
    min_r = min(y for x, y in tiles)
    max_r = max(y for x, y in tiles)
    s = '\n'
    for y in range(min_r-1, max_r +3):
        s += str(y) + ' |'
        for x in range(min_c -2, max_c + 3):
            if (x, y) in tiles:
                s += '#' 
            elif (x, y) in green_tiles:
                s += 'X' 
            else: 
                s+='.'
        s += '|\n'
    print(s)
    
    

def add_green_tiles(t1, t2, green_tiles):
    x1,y1 = t1
    x2,y2 = t2
    if x1 == x2:
        max_y,min_y = max(y1,y2), min(y1,y2)
        for yy in range(min_y, max_y+1):
            green_tiles.add((x1,yy))
    elif y1 == y2:
        max_x,min_x = max(x1,x2), min(x1,x2)
        for xx in range(min_x, max_x+1):
            green_tiles.add((xx,y1))
    else:
        assert False       

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        tiles = [tuple(map(int, line.strip().split(','))) for line in f]
    sol1 = solve_part_1(tiles)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(tiles)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
