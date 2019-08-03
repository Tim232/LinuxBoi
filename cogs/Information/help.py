import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 153, 34)
        )
        embed.set_author(name="→ All available bot commands!")
        embed.set_thumbnail(url="https://bit.ly/2YQgsWL")
        embed.add_field(name="—", value="→ Shows info about all available bot commands!"
                                        "\n→ Capitalization does not matter for the bot prefix." +
                                        "\n—")

        moderation = "`l!purge`, `l!warn`, `l!kick`, `l!ban`, `l!forceban`, `l!unban`, `l!nickname`, `l!resetnick`"
        information = "`l!help`, `l!stats`, `l!ping`, `l!whois`, `l!server`, `l!invite`"
        fun = "`l!say`, `l!coinflip`, `l!avatar`, `l!howgay`, `l!8ball`"
        utility = "`l!newsletter`, `l!poll`, `l!weather`, `l!mcbe`, `l!email`"
        # linux_info = "`l!wheretostart`, `l!channels`"

        embed.add_field(name="• Moderation Commands!", inline=False, value=moderation)
        embed.add_field(name="• Information Commands!", inline=False, value=information)
        embed.add_field(name="• Fun Commands!", inline=False, value=fun)
        embed.add_field(name="• Utility Commands!", inline=False, value=utility)
        # embed.add_field(name="• Linux information!", inline=False, value=linux_info)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
