import discord
from discord.ext import commands
from pythonping import ping
import datetime


class status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("status is ready")

    @commands.command()
    async def status(self, ctx):
        resttime = ping('google.com').rtt_avg_ms

        if resttime < 100:
            embed = discord.Embed(title="Status",
                                  description=f"Ping: {resttime}ms",
                                  type="rich",
                                  color=0x2EE738,
                                  timestamp=datetime.datetime.utcnow()
                                  )
        else:
            embed = discord.Embed(title="Status",
                                  description=f"We are currently experiencing issues with our servers. Please try again later.",
                                  type="rich",
                                  color=0xE7382E,
                                  timestamp=datetime.datetime.utcnow()
                                  )

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(status(client))
