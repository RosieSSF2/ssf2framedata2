import json

char = 'Bandana Dee'
move = 'Jab'

with open('data/moves.json', 'r') as m:
    moveinfo = json.load(m)
    
with open('data/characters.json', 'r') as c:
    charidentifier = json.load(c)
    
charid = charidentifier[f'{char}']['id']
moveid = moveinfo[f'{move}']

with open(f'data/info/{char}.json', 'r') as f:
    charinfo = json.load(f)
    
for i, j in enumerate(charinfo[f'{moveid}']):
    # Iterates through the different hits the move has
    print(f'Hit: {j}')
    
    # For every value listed in each hit prints the value name and value value
    for idx, info in enumerate(charinfo['1'][f'{j}']):
        print(f'{info}: {charinfo['1'][f'{j}'][f'{info}']}')