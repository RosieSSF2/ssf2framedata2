import json

char = 'Bandana Dee'
move = 'Jab'

with open(f'data/info/{char}.json', 'r') as f:
    charinfo = json.load(f)
    
for i, j in enumerate(charinfo[move]):
    # Iterates through the different hits the move has
    print(f'Hit: {j}')
    
    # For every value listed in each hit prints the value name and value value
    for idx, info in enumerate(charinfo[move][f'{j}']):
        print(f'{info}: {charinfo[move][f'{j}'][f'{info}']}')