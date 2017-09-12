import discord
from discord.ext import commands

class about:
    """Magik Bot About!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self):
        """This does stuff!"""

        #Your code will go here
        
embed=discord.Embed(title="basic test", url='http://www.mydomain.com', description="This is a description", color=0x207cee)
embed.set_author(name="UnseenMagik", url='http://www.discordlink.com', icon_url='http://imageicon.com')
embed.set_thumbnail(url='http://www.imageurl.com')
embed.add_field(name="Test Field 1", value="Result", inline=True)
embed.add_field(name="Test Field 2", value="Inline text", inline=True)
embed.set_footer(text="Footer notes here. ")


await self.bot.say(embed=embed)
        


def setup(bot):
    bot.add_cog(about(bot))
