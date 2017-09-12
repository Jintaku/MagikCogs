import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self):
        """About Magik Bot"""
        
        embed=discord.Embed(title="About Magik Bot", url='http://www.magikbot.co.uk', description="A discord bot made with love. Created for Discord Administration support. With hundreds of commands, admin, mod, support, games, fun and more. For more information see below:", color=0x207cee)
        embed.set_author(name="Magik bot", url='http://www.magikbot.co.uk', icon_url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.add_field(name="Discord Support", value= url="https://discord.gg/kQjTw5Z", description="Visit our Discord Server", inline=True)
        embed.add_field(name="Website", value= url="http://www.magikbot.co.uk", description="Visit our Website", inline=True)
        embed.add_field(name="Auther", value="UnseenMagik", inline=False)
        embed.add_field(name="Version", value="API version 0.16.11", inline=True)
        embed.set_footer(text="Magik Bot - Providing Discord support since September 2017")
        
        await self.bot.say(embed=embed)
        
def setup(bot):
    bot.add_cog(Mycog(bot))
