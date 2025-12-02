import sys
sys.path.append('..')

d={
    2:[2],
    3:[3],
    4:[4],
    5:[5],
    6:[3,6],
    7:[7],
    8:[4,8],
    9:[3,9],
    10:[5,10],
}

def solve(in_data):
    t1 = 0
    t2 = 0
    for x1,x2 in in_data:
        for v in range(x1, x2+1):
            if is_faulty(v, True):
                t1+=v
                t2+=v
            elif is_faulty(v, False):
                t2+=v
    return t1, t2
            
def is_faulty(v, part1 = False):
    s = str(v)
    l = len(s)
    if l == 1:
        return False
    if part1:
        m = len(s) // 2
        return s[:m] == s[m:]
    for n in d[l]:
        size = l // n
        split_v = s[:size]
        faulty = True
        for i in range(size, l, size):
            part_v = s[i:i+size]
            if split_v != part_v:
                faulty =  False
                break
        if faulty:
            return True
    return False


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        l = f.read()
        ranges = l.split(',')
        in_data=[list(map(int, r.split('-'))) for r in ranges]
    sol1,sol2 = solve(in_data)
    print(f'Part 1: {sol1}')

    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
