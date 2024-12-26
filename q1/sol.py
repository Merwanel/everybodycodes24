# Ancient Ant (A): Not very dangerous. Can be managed without using any potions.
# Badass Beetle (B): A big and strong bug that requires 1 potion to defeat.
# Creepy Cockroach (C): Fast and aggressive! This creature requires 3 potions to defeat it.
# Diabolical Dragonfly (D): A fast and tricky enemy, hard to hit. This creature requires 5 potions to defeat it.
monster_cost = {'A':0, 'B':1, 'C':3, 'D':5}
def solve(file : str, expect:int, monster_pairup=1) -> int :
    monsters = []
    with open(file, 'r') as f :
        for line in f :
            monsters = line.strip()
    cost = 0
    for i in range(0, len(monsters), monster_pairup) :
        nb_monster_in_group = 0
        for j in range(i, i+monster_pairup) :
            if 'x' == monsters[j] :
                continue
            cost += monster_cost[monsters[j]]
            nb_monster_in_group += 1
        if nb_monster_in_group == 2 :
            cost += nb_monster_in_group
        if nb_monster_in_group == 3 :
            cost += nb_monster_in_group * 2
    return cost, cost == expect


print(solve('example.txt', expect=5))
print(solve('input.txt', expect=1334) )
print(solve('example2.txt', expect=28, monster_pairup=2))
print(solve('input2.txt', expect=5383, monster_pairup=2))
print(solve('example3.txt', expect=30, monster_pairup=3))
print(solve('input3.txt', expect=28000, monster_pairup=3))