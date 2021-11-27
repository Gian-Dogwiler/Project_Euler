longest_cycle_unit = 0
longest_cycle_num = 0

def getReciprocalCycle(d: int):
    rest_seq = []
    fraq_seq = []
    rest = 1
    while rest not in rest_seq:
        if rest == 0:
            return fraq_seq
        rest_seq.append(rest)
        rest *= 10
        new_fraq = rest // d
        rest = rest % d
        fraq_seq.append(new_fraq)
    return fraq_seq

for i in range(1,1000):
    new_cycle = getReciprocalCycle(i)
    if len(new_cycle) > longest_cycle_unit:
        longest_cycle_unit = len(new_cycle)
        longest_cycle_num = i

print(longest_cycle_num)
print(longest_cycle_unit)