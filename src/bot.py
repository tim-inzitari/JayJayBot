from cmath import exp
import os
import re
import discord
import datetime
import random
from dotenv import load_dotenv
from discord import app_commands
from getCard import name_to_id, id_to_name, df, get_card_message_function

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')



def main():

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        await tree.sync()
        print("Logged in as ", client.user.name)

  
    @tree.command(
        name="cardinfo",
        description="CardInfo by name",
    )

    async def cardinfo(ctx, name: str):
        card_obj = get_card_message_function(name)
        await ctx.response.send_message(str(card_obj)[:1500])

    client.run(os.environ.get('DISCORD_TOKEN'))

if __name__ == "__main__":
    load_dotenv()
    main()
