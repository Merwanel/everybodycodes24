
import collections

def rolling_hash_marking(rune:str, inscription:str) -> tuple[int, set[int]] :
    if len(rune) > len(inscription) :
        return 0, set()
    nb_match = 0
    marking = set()
    hash_rune = 0
    for letter in rune :
        hash_rune *= 10
        hash_rune += ord(letter)
    hash_inscription = 0
    for i in range(len(rune)) :
        hash_inscription *= 10
        hash_inscription += ord(inscription[i])
    if hash_inscription == hash_rune and inscription[:len(rune)] == rune :
        nb_match += 1
        marking.update(range(i-len(rune)+1, i+1))
        
    for i in range(len(rune), len(inscription)) :
        i = i % len(inscription)
        
        hash_inscription *= 10
        hash_inscription += ord(inscription[i])
        hash_inscription -= 10 ** (len(rune)) * ord(inscription[i-len(rune)])
        if hash_inscription == hash_rune and inscription[i-len(rune)+1:i+1] == rune :
            nb_match += 1
            marking.update(range(i-len(rune)+1, i+1))
            
    return nb_match, marking

def solve(file : str, expect:tuple[int,int]) -> tuple[int, bool, int, bool] :
    possible_runes: str = []
    inscriptions : list[str] = []
    with open(file, 'r') as f :
        for i, line in enumerate(f) :
            if line =='\n' :
                continue
            if i == 0 :
                possible_runes = line.strip()[6:].split(',')
            else :
                inscriptions.append(line.strip())
    nb_rune = 0
    nb_symbol = 0
    for inscription in inscriptions :
        marking_inscription = set()
        for rune in possible_runes :
            nb_match, marking = rolling_hash_marking(rune, inscription)
            _ , marking_reverse = rolling_hash_marking(rune[::-1], inscription)
            nb_rune += nb_match
            marking_inscription |= marking | marking_reverse
        nb_symbol += len(marking_inscription)
    return nb_rune, nb_rune == expect[0], nb_symbol, nb_symbol == expect[1]



def rolling_hash_marking_part3(rune:str, seq:list[tuple[str, int, int]], is_looping=False) -> set[int] :
    if len(rune) > len(seq)  :
        return set()
    nb_match = 0
    marking = set()
    hash_rune = 0
    q = collections.deque([])
    for letter in rune :
        hash_rune *= 10
        hash_rune += ord(letter)
    hash_seq = 0
    for i in range(len(rune)) :
        letter, r, c = seq[i]
        hash_seq *= 10
        hash_seq += ord(letter)
        q.append((letter, r, c))
    if hash_seq == hash_rune and ''.join( letter for letter , _ , _ in q) == rune :
        nb_match += 1
        marking.update((r, c) for _ , r , c in q)
        
    for i in range(len(rune), len(seq)*(2 if is_looping else 1)) :
        i = i % len(seq)

        letter, r, c = seq[i]
        
        hash_seq *= 10
        hash_seq += ord(letter)
        hash_seq -= 10 ** (len(rune)) * ord(seq[i-len(rune)][0])
        
        q.append((letter, r, c))
        q.popleft()
        if hash_seq == hash_rune and  ''.join( letter for letter , _ , _ in q) == rune :
            nb_match += 1
            marking.update((r, c) for _ , r , c in q)
    return marking

def solve_part3(file : str, expect:int):
    possible_runes: str = []
    inscriptions : list[str] = []
    with open(file, 'r') as f :
        for i, line in enumerate(f) :
            if line =='\n' :
                continue
            if i == 0 :
                possible_runes = line.strip()[6:].split(',')
            else :
                inscriptions.append(line.strip())
    
    marking_inscription = set()
    for rune in possible_runes :
        for r in range(len(inscriptions)) :
            inscription = [(inscriptions[r][c], r, c) for c in range(len(inscriptions[0]))]
            marking = rolling_hash_marking_part3(rune, inscription, is_looping=True)
            marking_reverse = rolling_hash_marking_part3(rune[::-1], inscription, is_looping=True)
            marking_inscription |= marking | marking_reverse
        for c in range(len(inscriptions[0])) :
            inscription = [(inscriptions[r][c], r, c) for r in range(len(inscriptions))]
            marking = rolling_hash_marking_part3(rune, inscription)
            marking_reverse = rolling_hash_marking_part3(rune[::-1], inscription)
            marking_inscription |= marking | marking_reverse
    return len(marking_inscription), len(marking_inscription) == expect

    
print(solve('example.txt', expect=(4,15)))
print(solve('input.txt', expect=(33,77)) )
print(solve('example2.txt', expect=(14,42)))
print(solve('input2.txt', expect=(4505,5139)))
print(solve_part3('example3.txt', expect=10))
print(solve_part3('input3.txt', expect=11137))
