import sys
sys.path.append('..')


def solve_part_1(problems):
    t = 0
    for p in problems:
        op = p[-1]
        p_n = int(p[0])
        for n in p[1:-1]:
            n = int(n)
            p_n = p_n * n if '*' in op else p_n + n
        t += p_n
    return t


def solve_part_2(problems):
    t = 0
    for p in problems:
        op = p[-1]
        s = max([len(x) for x in p])
        new_ps = ['' for _ in range(s)]
        for i in range(s - 1, -1, -1):
            for n in p[:-1]:
                if i < len(n):
                    new_ps[i]+=n[i]
        p_n = int(new_ps[0])
        for n in new_ps[1:]:
            n = int(n)
            p_n = p_n * n if '*' in op else p_n + n
        t += p_n
    return t

def get_problem(i, lines):
    numbers=[]
    for l in lines:
        l_i = i
        has_started_n = False    
        has_finished_n = False
        n = ''
        while not has_finished_n:
            v = ' ' if l_i == len(l) else l[l_i]
            n += v
            if v in '1234567890*+':
                has_started_n = True
            if has_started_n and v not in '1234567890+*' or l_i == len(l):
                has_finished_n = True
            l_i += 1
        numbers.append(n)
    s = max([len(x) for x in numbers])
    return [x[:s-1] for x in numbers]

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    problems = []
    with open(in_f) as f:
        lines = [line for line in f.read().splitlines()]
        i = 0
        while i < len(lines[0]):
            problem = get_problem(i, lines)
            i += max([len(p) for p in problem]) + 1
            problems.append(problem)
    sol1 = solve_part_1(problems)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(problems)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
