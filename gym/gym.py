from cogs.utils.checks import is_owner_check
from urllib.parse import quote
import discord
from discord.ext import commands
import aiohttp


numbs = {
    "next": "➡",
    "back": "⬅",
    "install": "✅",
    "exit": "❌"
}


class Gym:
    """Search for Gyms"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        
    def __unload(self):
        self.session.close()

    @commands.group(pass_context=True, aliases=['gy'])
    async def gym(self, ctx):
        """Search for Gyms"""

        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    async def _search_redportal(self, ctx, url):
        # future response dict
        data = None


            # a list of embeds
            embeds = []

            for cog in data['results']['list']:
                embed = discord.Embed(title=cog['name'],
                embed.add_field(name='Type', value='type', inline=True)
                embed.add_field(name='Author', value='author', inline=True)
                embed.add_field(name='Repo', value='repo', inline=True)
                embed.add_field(name='cog', value='cog install', inline=False)
                embed.set_footer(text='footer')

                embeds.append(embed)

            return embeds, data

        else:
            return None



    async def cogs_menu(self, ctx, cog_list: list,
                        message: discord.Message=None,
                        page=0, timeout: int=30, edata=None):
        """menu control logic for this taken from
           https://github.com/Lunar-Dust/Dusty-Cogs/blob/master/menu/menu.py"""
        cog = cog_list[page]
    
        is_owner_or_co = is_owner_check(ctx)
        if is_owner_or_co:
            expected = ["➡", "✅", "⬅", "❌"]
        else:
            expected = ["➡", "⬅", "❌"] 

        if not message:
            message =\
                await self.bot.send_message(ctx.message.channel, embed=cog)
            await self.bot.add_reaction(message, "⬅")
            await self.bot.add_reaction(message, "❌")

            if is_owner_or_co:
                await self.bot.add_reaction(message, "✅")

            await self.bot.add_reaction(message, "➡")
        else:
            message = await self.bot.edit_message(message, embed=cog)
        react = await self.bot.wait_for_reaction(
            message=message, user=ctx.message.author, timeout=timeout,
            emoji=expected
        )
        if react is None:
            try:
                try:
                    await self.bot.clear_reactions(message)
                except:
                    await self.bot.remove_reaction(message, "⬅", self.bot.user)
                    await self.bot.remove_reaction(message, "❌", self.bot.user)
                    if is_owner_or_co:
                        await self.bot.remove_reaction(message, "✅", self.bot.user)
                    await self.bot.remove_reaction(message, "➡", self.bot.user)
            except:
                pass
            return None
        reacts = {v: k for k, v in numbs.items()}
        react = reacts[react.reaction.emoji]
        if react == "next":
            page += 1
            next_page = page % len(cog_list)
            try:
                await self.bot.remove_reaction(message, "➡", ctx.message.author)
            except:
                pass
            return await self.cogs_menu(ctx, cog_list, message=message,
                                        page=next_page, timeout=timeout, edata=edata)
        elif react == "back":
            page -= 1
            next_page = page % len(cog_list)
            try:
                await self.bot.remove_reaction(message, "⬅", ctx.message.author)
            except:
                pass
            return await self.cogs_menu(ctx, cog_list, message=message,
                                        page=next_page, timeout=timeout, edata=edata)
        elif react == "install":
            if not is_owner_or_co:
                await self.bot.say("This function is only available to the bot owner.")
                return await self.cogs_menu(ctx, cog_list, message=message,
                                            page=page, timeout=timeout, edata=edata)
            else:
                INSTALLER = self.bot.get_cog('Downloader')
                if not INSTALLER:
                    await self.bot.say("The downloader cog must be loaded to use this feature.")
                    return await self.cogs_menu(ctx, cog_list, message=message,
                                                page=page, timeout=timeout, edata=edata)

                repo1, repo2 = edata['results']['list'][page]['repo']['name'], edata['results']['list'][page]['links']['github']['repo']
                cog1, cog2 = edata['results']['list'][page]['repo']['name'], edata['results']['list'][page]['name']

                await ctx.invoke(INSTALLER._repo_add, repo1, repo2)
                await ctx.invoke(INSTALLER._install, cog1, cog2)

                return await self.bot.delete_message(message)
        else:
            try:
                return await self.bot.delete_message(message)
            except:
                pass


def setup(bot):
    bot.add_cog(Gym(bot))
