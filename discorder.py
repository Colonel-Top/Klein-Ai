# -*- coding: utf-8 -*-
import discord
import asyncio
import sys
import subprocess

client = discord.Client()
import codecs
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        text = message.content
        b = text.encode("cp874")
        #text = text.encode('ascii', 'ignore').decode('ascii')
        text = b.decode("cp874")
        '''tmpin = str(message.content)
        message = tmpin
        print(message.encode('utf-8').decode('utf-8'))
        #ret = subprocess.Popen(['python', 'chat.py',  message], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ret = ''
        '''
        text = str(text.encode('utf-8'))
        ret = str(subprocess.check_output([sys.executable, "chat.py",text]))

        ret = ret.replace('=','')
        ret = ret.replace('b\'','')
        ret = ret.replace('\\n\'','')
        ret = ret.replace('\\n',' ')
        print(ret)
        await client.send_message(message.channel, ret)
        print(text)
    except Exception as e:
        print(e)
client.run('MzU2NDg1MTI3MTUwMzcwODE3.DJcDMQ.u2nuYX49hPoq9BZEnK_lLGl80oE')
