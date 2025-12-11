import sys
sys.path.append('..')


def solve_part_1(servers):
    q = [x for x in servers['you']]
    s = 0
    
    while q:
        p = q.pop()
        if p == 'out':
            s+=1
        else:
            next_out = servers[p]
            q+=next_out
    return s

def n_paths(start,stop,servers, m):
    if (start, stop) in m:
        return m[(start,stop)]
    if start == stop:
        return 1
    if start == 'out':
        return 0
    t = sum(n_paths(s, stop, servers, m) for s in servers[start])
    m[(start,stop)] = t
    return t
    
def solve_part_2(servers):
    m={}
    return n_paths('svr','dac',servers,m) * n_paths('dac', 'fft',servers,m) * n_paths('fft', 'out', servers,m) + n_paths('svr','fft',servers,m) * n_paths('fft', 'dac',servers,m) * n_paths('dac', 'out', servers,m)

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        servers={}
        for l in f.read().splitlines():
            s,o=l.split(':')
            servers[s] = o.split()
    sol1 = solve_part_1(servers)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(servers)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
