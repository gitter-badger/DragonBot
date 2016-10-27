#!/usr/bin/python
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
        print('-------------')
        print('Okay, Everything seems okay - lets fly!')
        print('Im logged in as ' + client.user.name)
        print('The bots user id is ' + client.user.id)
        print('Lets go..')
        print('-------------')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('MjQxMjE0Nzk3NDc4MjMyMDY0.CvOoTQ.coyK0nDGaA02y4RrfiyMfQCMcuU')
