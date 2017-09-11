import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
@commands.command(pass_context=True)
    async def excom(self, ctx):
        """CTX example command"""
        author = ctx.message.author
        description = ("Short little description with a link to "
                       "the [guide](https://github.com/Redjumpman/Jumper-Cogs/wiki/Discord-Coding-Guide)")
        field_name = "Generic Name"
        field_contents = "Example contents for this field"
        footer_text = "Hi. I am a footer text. I look small when displayed."

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.title = "Cool title for my embed"
        embed.set_author(name=str(author.name), icon_url=author.avatar_url)
        embed.add_field(name=field_name, value=field_contents)  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Mycog(bot))
