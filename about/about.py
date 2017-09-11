import discord
from discord.ext import commands


    def __init__(self, bot):
        self.bot = bot
        
        class discord.Embed(**kwargs)
    """My custom cog that does stuff!"""

@commands.command(pass_context=True)
    async def about(self, ctx):
        """CTX example command"""
embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0xa6550d), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```", timestamp=datetime.datetime.utcfromtimestamp(1505140699))

embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
embed.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

embed.add_field(name="🤔", value="some of these properties have certain limits...")
embed.add_field(name="😱", value="try exceeding some of them!")
embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
embed.add_field(name="<:thonkang:219069250692841473>", value="these last two", inline=True)
embed.add_field(name="<:thonkang:219069250692841473>", value="are inline fields", inline=True)

await bot.say(content="this `supports` __a__ **subset** *of* ~~markdown~~ 😃 ```js\nfunction foo(bar) {\n  console.log(bar);\n}\n\nfoo(1);```", embed=embed)

def setup(bot):
    bot.add_cog(Mycog(bot))
