
import os
import random
import datetime


import discord
from dotenv import load_dotenv
import sys
from discord.ext.commands import Bot
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
 
 

@client.event
async def on_message(message):
    if message.author == client.user:
         return

        

    time = datetime.datetime.now()
    x=(time.strftime("%d-%m-%Y"))

    time_table ={1:'',2:'',3:'',4:'',5:'Eng @9 , Math @ 11, Phy T @1 , Phy P @2',6:''}

    @Bot.command()(name="command")
    async def _command(ctx):
     def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in [1,2,3,4,5,6 ]

     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "1":
         await ctx.send("1,2,3,4,5,6")

     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "1":
         await ctx.send(x,time_table[1])

     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "2":
            await ctx.send(x,time_table[2])
     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "3":
            await ctx.send(x,time_table[3])    
     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "4":
            await ctx.send(x,time_table[4])
     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "5":
            await ctx.send(x,time_table[5])
     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "5":
            await ctx.send(x,time_table[5])


client.run(TOKEN)
