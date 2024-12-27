
def solve(file : str, expect:tuple[int,int], does_diagonals_matter=False) -> tuple[int, bool, int, bool] :
    grid : list[str] = []
    with open(file, 'r') as f :
        for i, line in enumerate(f) :
            grid.append(list(line.strip()))
    N, M = len(grid), len(grid[0])
    nb_dig = 0 
    
    # 1st dig
    for r in range(N) :
        for c in range(M) :
            if grid[r][c] == '#' :
                grid[r][c] = 1
                nb_dig += 1
            else :
                grid[r][c] = 0
                
    # suubsequent digs
    have_dug_atleast_1 = True
    required_depth = 1
    while have_dug_atleast_1 :
        have_dug_atleast_1 = False
        for r in range(1,N-1) :
            for c in range(1,M-1) :
                is_digging_allowed = False
                if does_diagonals_matter :
                    is_digging_allowed = min(grid[r][c],  grid[r-1][c],  grid[r][c-1], grid[r+1][c],  grid[r][c+1],  grid[r-1][c-1],  grid[r+1][c-1], grid[r+1][c+1],  grid[r-1][c+1]) >=  required_depth
                else :
                    is_digging_allowed = min(grid[r][c],  grid[r-1][c],  grid[r][c-1], grid[r+1][c],  grid[r][c+1]) >=  required_depth
                if is_digging_allowed :
                    grid[r][c] = required_depth + 1
                    nb_dig += 1
                    have_dug_atleast_1 = True
        required_depth += 1
                
    [print("".join(map(str,row))) for row in grid]
    return nb_dig, nb_dig == expect



    
print(solve('example.txt', expect=35))
print(solve('input.txt', expect=124 ))
print(solve('input2.txt', expect=2737))
print(solve('example3.txt', expect=29, does_diagonals_matter=True))
print(solve('input3.txt', expect=10365, does_diagonals_matter=True))