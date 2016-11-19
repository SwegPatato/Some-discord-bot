import asyncio
import re

import discord

client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='Sweg is Bae'))
	print('connected to server as {}'.format(client.user))

@client.event
async def on_server_join(server):
        for i in server.channels:
                if i.type == 'text':
                        await client.send_message(i, 'I have joined!')
                


@client.event
async def on_message(message):
	if (not message.author.bot) and message.author != client.user:

		if not message.server:
			await client.send_message(message.channel, 'Nope. Message me on a real server please!')

		print('\nmessage from {user}: {msg} on channel: {chn}\n'.format(
			user=message.author, msg=message.content, chn=message.channel))
		
		ppattern = re.compile('8\=+\>')
		if ppattern.match(str(message.content)): #stuff here
			''' do
			stuff
			here
			'''
			await client.send_message(message.channel, '^ That is a dick')

		if message.content.lower().split()[0] in ['hi','hello','hey']:
			await client.send_message(message.channel, 'Hello {}!'.format(message.author.mention))

		if message.content.lower().split()[0] in ['bye','bai','pce']:
			await client.send_message(message.channel, 'bye {}!'.format(message.author.mention))


try:
	token = open("discord.token", "r").readline()
	print(token)
	client.run(token)
except:
	print("Please place your discord token in the \'discord.token\' file.")



