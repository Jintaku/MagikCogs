import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
@client.event
async def on_message(message):
    if message.content.startswith('about'):
        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.title = "Cool title for my embed"
        embed.set_author(name=str(author.name), icon_url=author.avatar_url)
        embed.add_field(name=field_name, value=field_contents)  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Mycog(bot))
