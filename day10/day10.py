import sys
sys.path.append('..')
import aoc
import z3


def solve_part_1(machines):
    return sum(press_buttons(ld, ''.join(['.']*len(ld)), buttons) for (ld, buttons, _) in machines)

def press_light_button(button, ld):
    ld_copy= [x for x in ld]
    for l in button:
        ld_copy[l] = '#' if ld_copy[l] == '.' else '.'
    return"".join(ld_copy)
        
def press_buttons(target_ld, current_ld, buttons):
    i = 0
    variants = [current_ld]
    memo = {}
    buttons_with_str = [(b, ''.join([str(x) for x in b])) for b in buttons]
    while True:
        new_variants = []
        for v in variants:
            for (b,s_b) in buttons_with_str:
                if (s_b, v) in memo:
                    # If we reach same state again it can never be the fastest
                    pass
                else:
                    button_ld = press_light_button(b, v)
                    if button_ld == target_ld:
                        return i + 1
                    else:
                        memo[(s_b, v)] = button_ld
                        new_variants.append(button_ld)
        variants = new_variants
        i+=1

def solve_part_2(machines):
    s = 0
    for (_, buttons,joltage) in machines:
        clicks = z3.Int('clicks')
        button_clicks = []
        o = z3.Optimize()
        for i in range(len(buttons)):
            bi = z3.Int('b'+str(i))
            o.add(bi >=0)
            button_clicks.append(bi)
        
        for i in range(len(joltage)):
            j_i = z3.Int('j'+str(i))
            o.add(j_i == joltage[i])
            o.add(j_i == z3.Sum([button_clicks[j] for j in range(len(button_clicks)) if i in buttons[j]]))
                
        o.add(z3.Sum(button_clicks) == clicks)
        o.minimize(clicks)
        o.check()
        m = o.model()
        s += m[clicks].as_long()
    return s

def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        machines=[]
        for l in f.read().splitlines():
            c = l.split(' ')
            ld = c[0][1:-1]
            buttons = [aoc.get_ints(b) for b in c[1:-1]]
            j = aoc.get_ints(c[-1])
            machines.append([ld, buttons, j])
    sol1 = solve_part_1(machines)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(machines)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
