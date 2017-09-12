import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self):
        """About Magik Bot"""
        
        embed=discord.Embed(title="<b>About Magik Bot<b>", url='http://www.magikbot.co.uk', description="A discord bot made with love. Created for Discord Administration support. <br>With hundreds of commands, admin, mod, support, games, fun and more.<br> For more information see below:<p>", color=0x207cee)
        embed.set_author(name="Magik bot", url='http://www.magikbot.co.uk', icon_url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.add_field(name="<b>Discord Support</b>", value="<a href="https://discord.gg/kQjTw5Z">Visit our Discord Server</a>", inline=True)
        embed.add_field(name="<b>Website</b>", value="<a href="http://www.magikbot.co.uk">Visit our Website</a>", inline=True)
        embed.add_field(name="<b>Auther</b>", value="UnseenMagik", inline=False)
        embed.add_field(name="<b>Version</b>", value="API version 0.16.11", inline=True)
        embed.set_footer(text="<i>Magik Bot - Providing Discord support since September 2017</i>")
        
        await self.bot.say(embed=embed)
        
def setup(bot):
    bot.add_cog(Mycog(bot))
