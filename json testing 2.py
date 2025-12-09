import json

char = 'Bandana Dee'
move = 'Jab'


with open('data/stats/stats.json', 'r') as i:
        charinfo = json.load(i)
      
desc = ""
             
#for idx, j in enumerate(charinfo[char]):
#    # Iterates through the different stats a character has
#    desc = ""
#    print(charinfo[char][j])
    
for idx, info in enumerate(charinfo[char]["Stats"]):
    desc += f'{info}: {charinfo[char]["Stats"][info]}\n' 
    
print(charinfo[char]["Stats"])

'''
with open('data/characters.json', 'r') as c:
    charidentifier = json.load(c)

with open(f'data/info/{char}.json', 'r') as f:
    charinfo = json.load(f)

embeds = []
gif_pairs = []  # (fullspeed_url, slowmo_url)
hits = []
desc = ''

# Character info for embed title, author, etc
for idx, identifier in enumerate(charidentifier[char]):
    print(f'{identifier} {charidentifier[char][identifier]}')
                        # charidentifier[char][identifier] returns characters id, color, icon

# Move info for embed description    
for i, hit in enumerate(charinfo[move]["Hitboxes"]):
    # Iterates through the different hits the move has
    hits.append(hit)   
    
    # For every value listed in each hit prints the value name and value value
    for idx, info in enumerate(charinfo[move]["Hitboxes"][f'{hit}']):
        desc += f'{info}: {charinfo[move]["Hitboxes"][f'{hit}'][f'{info}']}\n'
        
    
    # Extract images
    #print(f'Image: {charinfo[move]["Images"]["Full Speed"][f"{hit}"]}')
    #print(f'Slowmo: {charinfo[move]["Images"]["Slowmo"][f"{hit}"]}')
    
print(hits)
'''