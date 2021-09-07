from logging import WARNING
import discord
import os
import random
import datetime
from discord import channel
from discord.ext import commands,tasks
from discord.utils import get 


BOT_PREFIX = '!'


def main():

    bot = commands.Bot(command_prefix = BOT_PREFIX)  

    @bot.event
    async def on_ready():
        print("Logged in : " + bot.user.name + '\n')

    @bot.command(pass_context=True, aliases=['s'])
    async def sad(ctx):
        with open("quotes.txt") as file:
            quotes = []
            for i in file:
                quotes.append(i)    

            if ctx.message.author == bot.user:
                return
            
            if ctx.message.content.startswith('!sad'):

                await ctx.message.channel.send(quotes[random.randint(0,len(quotes)-1)])
        

    @bot.command(pass_context=True, aliases=['j', 'joi','J','JOIN','Join'])
    async def join(ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        
        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"The bot has connected to {channel}\n")
        
        await ctx.send(f"Joined {channel}")

    @bot.command(pass_context=True, aliases=['l', 'lea','L','LEAVE','Leave'])
    async def leave(ctx):
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            print(f"left {channel}")
            await ctx.send(f"Left {channel}")
        else:
            print(f"Bot was not connected to a channel")
            await ctx.send("I am not in a channel")




    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()

