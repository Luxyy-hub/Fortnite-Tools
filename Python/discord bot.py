import discord
import requests

client = discord.Client()

# APY KEY
API_KEY = 'KEY'

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.content == '/fortnite':
        news_response = requests.get('https://fortniteapi.com/v2/news', headers={'Authorization': API_KEY})
        skin_response = requests.get('https://fortniteapi.com/v2/cosmetics/br/outfits?filterNewRarity=New', headers={'Authorization': API_KEY})
        news_data = news_response.json()
        skin_data = skin_response.json()
        skin_names = "\n".join([skin['name'] for skin in skin_data['data']])
        response = f"**New Skins:**\n{skin_names}\n\n**News:**\n{news_data['data']['message']}"
        await message.channel.send(response)

    elif message.content.startswith('/search skin'):
        skin_name = message.content.replace('/search skin', '').strip()
        response = requests.get(f'https://fortniteapi.com/v2/cosmetics/br/search/all?name={skin_name}&matchMethod=contains', headers={'Authorization': API_KEY})
        data = response.json()
        if len(data['data']) == 0:
            response = f"Skin '{skin_name}' not found."
        else:
            skin = data['data'][0]
            response = f"**{skin['name']}**\n\n{skin['description']}\n\nRarity: {skin['rarity']['value']}\nType: {skin['type']['value']}\nIntroduced: {skin['introduction']['source']['value']}"
        await message.channel.send(response)

client.run('BOT_TOKEN')
