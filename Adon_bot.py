import discord
import random

TOKEN = '12345'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel}')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-the-builder':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'fuck':
            await message.channel.send(f'Ah yes! Another ancient Coborlwitz family technique!')
            return
        elif user_message.lower() == 'fucking':
            await message.channel.send(f'Ah yes! Another ancient Coborlwitz family technique!')
            return
        elif user_message.lower() == 'bitch':
            response = f'Was that an insult to the Coborlwitz family name {username}?! Youll pay for that! Face the Coborlwitz 140 year old Rock-cutting Whirlwind!!: '
            await message.channel.send(response)
            return
        elif user_message.lower() == 'pussy':
            response = f'Was that an insult to the coborlwitz family name {username}?! Youll pay for that! Face the Coborlwitz 200 year old torture technique: Hundred - year Convulsion Death!!: '
            await message.channel.send(response)
            return
        elif user_message.lower() == 'sorry':
            response = f'Hmph... as expected. Now kneel before me and perhaps Ill allow you to live as my armys prisoner, hehehe...'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'ban':
            response = f'Ban?! You cant ban me! Do you know who my brother is?? Take this: 1000 year old Coborlwitz family crossbow technique: Furious Attack Thunderclap Burst!!!'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'the':
            response = f'Yes, THE, I am THE great general Adon of the Chuder armys Blue Whale Knights. Tremble in my presence and kneel before me!'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

client.run(TOKEN)
