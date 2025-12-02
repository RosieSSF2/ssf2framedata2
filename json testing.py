import json
import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands

### Buttons ###

class HitboxView(View):
    def __init__(self, embeds, gif_pairs, hits, user: discord.User):
        super().__init__()
        self.embeds = embeds  # list of discord.Embed objects
        self.gif_pairs = gif_pairs  # list of tuples: (fullspeed_url, slowmo_url)
        self.hits = hits
        self.current_hit = 0
        self.user = user

        # GIF Speed Buttons
        self.add_item(GIFSpeedToggle("Full Speed", True, self))
        self.add_item(GIFSpeedToggle("Slow", False, self))
        
        # Hit buttons
        for idx, embed in enumerate(embeds):
            hit_name = hits[idx] if hits[idx] else f"Hit {idx+1}"
            if len(hits)>1: self.add_item(MoveSelect(hit_name, idx, self))

    def get_current_embed(self):
        return self.embeds[self.current_hit]

    def get_current_gif(self, slowmo: bool):
        urls = self.gif_pairs[self.current_hit]
        return urls[1] if slowmo else urls[0]

class GIFSpeedToggle(Button):
    def __init__(self, name: str, is_fullspeed: bool, view: HitboxView):
        self.is_fullspeed = is_fullspeed
        self.custom_view = view
        style = discord.ButtonStyle.blurple
        super().__init__(label=name, style=style)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.custom_view.user:
            await interaction.response.send_message("You're not allowed to use this button.", ephemeral=True)
            return

        idx = self.custom_view.current_hit
        embed = self.custom_view.get_current_embed()
        embed.set_image(url=self.custom_view.get_current_gif(slowmo=not self.is_fullspeed))
        await interaction.response.edit_message(embed=embed, view=self.custom_view)
        
class MoveSelect(Button):
    def __init__(self, name: str, index: int, view: HitboxView):
        self.index = index
        self.custom_view = view
        super().__init__(label=name, style=discord.ButtonStyle.gray)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.custom_view.user:
            await interaction.response.send_message("You're not allowed to use this button.", ephemeral=True)
            return

        self.custom_view.current_hit = self.index
        embed = self.custom_view.get_current_embed()
        # Set default image to full speed
        embed.set_image(url=self.custom_view.get_current_gif(slowmo=False))
        await interaction.response.edit_message(embed=embed, view=self.custom_view)


### Embeds and info ###

with open('data/info/Bandana Dee.json', 'r') as f:
    charinfo = json.load(f)
    

    
# print(charinfo['1'])

def ssf2_hitbox(char: str, move: str, user: discord.User):
    
    with open('data/moves.json', 'r') as m:
        moveinfo = json.load(m)
    
    with open('data/moves.json', 'r') as c:
        charidentifier = json.load(c)
    
    charid = charidentifier['char']['id']
    moveid = moveinfo[f'{move}']
    
    embeds = []
    gif_pairs = []  # (fullspeed_url, slowmo_url)
    hits = []
    
    for i, j in enumerate(charinfo['1']):
    # Iterates through the different hits the move has
        hits.append(j)
    
    # For every value listed in each hit prints the value name and value value
        for idx, info in enumerate(charinfo['1'][f'{j}']):
            
            desc = "\n".join(f'{info}: {charinfo['1'][f'{j}'][f'{info}']}')
            embed = discord.Embed(description=f'```\n{desc}```')
            
            embeds.append(embed)
            view = HitboxView(embeds, gif_pairs, hits, user)
            
    return embeds, view 

for i, j in enumerate(charinfo['1']):
    # Iterates through the different hits the move has
    print(f'Hit: {j}')
    
    # For every value listed in each hit prints the value name and value value
    for idx, info in enumerate(charinfo['1'][f'{j}']):
        print(f'{info}: {charinfo['1'][f'{j}'][f'{info}']}')