import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("mbed=discord.Embed(title="About Magik Bot", url='http://www.magikbot.co.uk', description="The information below is based on Magik Bot", color=0x0000FF)19embed.set_author(name="UnseenMagik", url='http://www.magikbot.co.uk', icon_url='https://images-ext-2.discordapp.net/external/zRHyBp5vB6IbOs3Q18jGh3VBSevFkg1TCtjnJr-YGO4/https/cdn.discordapp.com/icons/316991694480605208/3931424b8f0a7d908c1c04b8620e3680.jpg?width=100&height=100')20embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/zRHyBp5vB6IbOs3Q18jGh3VBSevFkg1TCtjnJr-YGO4/https/cdn.discordapp.com/icons/316991694480605208/3931424b8f0a7d908c1c04b8620e3680.jpg?width=100&height=100')21embed.add_field(name="What is Magik Bot", value="Magik Bot is used as an Admin Control Bot for your Discord Server.<br>With over 400 commands available.<br>Hosted by UnseenMagik and written in Python.", inline=False)22embed.add_field(name="Discord Support", value="http://discord.gg/kQjTw5Z", inline=True)23embed.add_field(name="Magik Bots Website", value="http://www.magikbot.co.uk", inline=True)24embed.set_footer(text="Thanks for using Magik Bot - Serving Discord users since September 2017")25await self.bot.say(embed=embed)")

def setup(bot):
    bot.add_cog(Mycog(bot))
