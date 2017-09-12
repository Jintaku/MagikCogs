import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self):
        """About Magik Bot"""
        
        embed=discord.Embed(title="About Magik Bot", url='http://www.magikbot.co.uk', description="A discord bot made with love. Created for Discord Administration support. <br>With hundreds of commands, admin, mod, support, games, fun and more.<br> For more information see below:<p>", color=0x207cee)
        embed.set_author(name="Magik bot", url='http://www.magikbot.co.uk', icon_url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.add_field(name="Discord Support", value="https://discord.gg/kQjTw5Z", inline=True)
        embed.add_field(name="Website", value="http://www.magikbot.co.uk", inline=True)
        embed.add_field(name="Auther", value="UnseenMagik", inline=False)
        embed.add_field(name="Version", value="API version 0.16.11", inline=True)
        embed.set_footer(text="Magik Bot - Providing Discord support since September 2017")
        
        await self.bot.say(embed=embed)
        
def setup(bot):
    bot.add_cog(Mycog(bot))
