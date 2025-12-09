import discord
from discord import app_commands
from discord.ext import commands

import json
import sqlite3

def ssf2_charinfo(char: str):
    '''
    The function used by the character commands to collect the data required
    
    Returns:
        A discord embed
    '''
    with open('data//stats/stats.json', 'r') as i:
        charinfo = json.load(i)
    
    desc = ''
             
    for idx, info in enumerate(charinfo[char]["Stats"]):
        desc += f'{info}: {charinfo[char]["Stats"][info]}\n'       
    
        embed = discord.Embed(description=f'```py\n{desc}```', color=int(charinfo[char]['Embed Info']['color'], 16))
        embed.set_image(url=charinfo[char]['Embed Info']['image'])
        embed.set_author(name=f'{char} Information', icon_url=charinfo[char]['Embed Info']['icon'])
        embed.set_footer(text='Up to date as of patch 1.4.0.1')
        
    return embed        


class Stats(commands.Cog):
    """Send displays of idle stance, and character stats."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    characters = [
        'Bandana Dee', 'Black Mage', 'Bomberman', 'Bowser', 'Captain Falcon',
        'Chibi-Robo', 'Donkey Kong', 'Falco', 'Fox', 'Ganondorf',
        'Goku', 'Ichigo', 'Isaac', 'Jigglypuff', 'Kirby',
        'Krystal', 'Link', 'Lloyd', 'Lucario', 'Luffy',
        'Luigi', 'Mario', 'Marth', 'Mega Man', 'Meta Knight',
        'Mr. Game and Watch', 'Naruto', 'Ness', 'PAC-MAN', 'Peach',
        'Pichu', 'Pikachu', 'Pit', 'Rayman', 'Ryu',
        'Samus', 'Sandbag', 'Sheik', 'Simon', 'Sonic',
        'Sora', 'Tails', 'Waluigi', 'Wario', 'Yoshi',
        'Zelda', 'Zero Suit Samus', 'King Dedede'
    ]

    async def character_autocomplete(self, interaction: discord.Interaction, current: str):
        return [
            app_commands.Choice(name=char, value=char)
            for char in self.characters
            if current.lower() in char.lower()
        ][:25]

    @app_commands.command(name='stats')
    @app_commands.describe(character="Choose a character")
    @app_commands.autocomplete(character=character_autocomplete)
    async def stats(self, interaction: discord.Interaction, character: str):
        """Show frame data and hitbox info for a character."""
        ssf2_embed = ssf2_charinfo(character)
        await interaction.response.send_message(embed=ssf2_embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Stats(bot))