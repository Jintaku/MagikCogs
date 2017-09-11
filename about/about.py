import discord
from discord.ext import commands

class AboutMagikBot:
    """This is information about Magik Bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("Embed ?about coming soon!")

def setup(bot):
    bot.add_cog(Mycog(bot))
