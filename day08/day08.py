from itertools import combinations
import sys
sys.path.append('..')
import aoc
import math


def solve_part_1(boxes):
    dists = {}
    for b1, b2 in combinations(boxes, 2):
        x1,y1,z1 = b1
        x2,y2,z2 = b2
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2+(z1-z2)**2)
        dists[d] = (b1, b2)
    shortest = sorted(dists.keys())
    circuits = []
    i = 0
    while not (len(circuits) == 1 and len(circuits[0]) == len(boxes)):
        d = shortest[i]
        b1,b2 = dists[d]
        added = False
        found = []
        i += 1
        for j,c in enumerate(circuits):
            if b1 in c or b2 in c:
                c.add(b1)
                c.add(b2)
                added = True
                found.append(j)
        if added:
            new_s=set()
            for j in found[::-1]:
                new_s |=circuits[j]
                del circuits[j]
            circuits.append(new_s)
        else:
            circuits.append(set([b1,b2]))
        if i == 1000:
            c_s = sorted([len(c) for c in circuits])
            p1 = c_s[-1] * c_s[-2] * c_s[-3]
        lb1,lb2 = b1,b2
    return p1, lb1[0] * lb2[0]


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    boxes = []
    with open(in_f) as f:
        for line in f:
            x,y,z= aoc.get_ints(line)
            boxes.append((x,y,z))
    sol1,sol2 = solve_part_1(boxes)
    print(f'Part 1: {sol1}')

    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
