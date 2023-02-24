import discord
from discord.ext import commands

import src.message_search as message_search


class check_message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("check message is ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        search = message_search.message_search(message.content)
        flag, links = search.search()
        
        if flag:
            await message.channel.send(embed=discord.Embed(
                title="Looks like I caught a phish 🎣",
                description="Alas these seas be a no phising zone, catch yer carp elsewhere",
                color=0xff0000
            ))
            
            await message.delete()


async def setup(client):
    await client.add_cog(check_message(client))
    