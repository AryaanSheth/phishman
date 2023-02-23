import discord
from discord.ext import commands
import os
import asyncio
import configparser
import threading
import time

import src.datacalls.update.update_data as update_data

config = configparser.ConfigParser()
config.read('config.ini')
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('!'), 
                      intents=discord.Intents.all(), 
                      help_command=None)


def update_data_thread():
    while True:
        try:
            update_data.UpdateData().write_to_database()
            with open("logs/database.log", "a") as f:
                f.write(f"Data updated successfully at {time.ctime()}\n")
            print("Data updated successfully")
            time.sleep(86400)
        except Exception as e:
            with open("error.log", "a") as f:
                f.write(f"{e}\n")


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    print("client is ready")
    await load()
    await client.start(config['DEFAULT']['Token'])

if __name__ == "__main__":
    threading.Thread(target=update_data_thread).start()
    asyncio.run(main())
