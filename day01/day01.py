import sys
sys.path.append('..')


def solve_part_1(in_data):
    s = 50
    t = 0
    for l in in_data:
        d, n = l[0], int(l[1:])
        s = (s +n) %100 if d == 'R' else (s - n) % 100
        if s == 0:
            t +=1
    return t

def solve_part_2(in_data):
    s = 50
    t = 0
    for l in in_data:
        d, n = l[0], int(l[1:])
        for x in range(n):
            s = (s + 1 if d == 'R' else s - 1) % 100
            if s == 0:
                t += 1
   
    return t


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
