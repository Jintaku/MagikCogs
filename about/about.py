import discord
from discord.ext import commands

class about:
    """Magik Bot About!"""

    def __init__(self, bot):
        self.bot = bot

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        embed.add_field(name="Fiel1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        
        await client.send_message(message.channel, embed=embed)
        


def setup(bot):
    bot.add_cog(about(bot))
