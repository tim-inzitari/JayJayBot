from cmath import exp
import os
import re
import discord
import datetime
import random
from dotenv import load_dotenv


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')



def main():

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)


    @client.event
    async def on_ready():
        print("Logged in as ", client.user.name)

  



    client.run(os.environ.get('DISCORD_TOKEN'))

if __name__ == "__main__":
    load_dotenv()
    main()
