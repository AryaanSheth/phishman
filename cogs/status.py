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
        embed = discord.Embed(title="Status",
                              description=f"Ping: {resttime}ms",
                              type="rich",
                              color=0x59E032,
                              timestamp=datetime.datetime.utcnow()
                              )
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(status(client))
