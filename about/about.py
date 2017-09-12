import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self, ctx):
        """About Magik Bot"""
        author = ctx.message.author
        description = ("Short little description with a link to "
                       "the [guide](https://github.com/Redjumpman/Jumper-Cogs/wiki/Discord-Coding-Guide)")
        field_name = "More Support at:"
        field_contents = "This will be replaced with a URL"
        footer_text = "Magik Bot created in Discord.py by UnseenMagik since 2017."

        embed = discord.Embed(colour=0x0000FF, description=description)  # Can use discord.Colour()
        embed.title = "About Magik Bot"
        embed.set_author(name=str(author.name), icon_url=author.avatar_url)
        embed.add_field(name=field_name, value=field_contents)  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Mycog(bot))
