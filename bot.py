import discord
import requests
import json
import random
import twitch
import datetime
from bs4 import BeautifulSoup 
from discord import Spotify
from discord import Member
from discord.ext import commands
from twitch import TwitchClient
from googletrans import Translator


token = 'Your-DiscordBot-Token'
prefix = '!'


client = commands.Bot(command_prefix = prefix)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your-activity"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
   await client.get_channel(744232867961241650).send(f"{member.mention} joined the server! :heart:")

@client.event
async def on_member_remove(member):
   await client.get_channel(744232867961241650).send(f"{member.mention} left the server! :slight_frown: ")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message)) 
    if   message.content.lower().startswith('sa'):
        await message.channel.send('As {0.author.mention}'.format(message)) 
    if  message.content.lower().startswith('merhaba'):
        await message.channel.send('Merhaba {0.author.mention}'.format(message)) 
    if   message.content.lower().startswith('selam'):
        await message.channel.send('As {0.author.mention}'.format(message)) 
    if message.content.lower().startswith('günaydın'):
        await message.channel.send('Günaydın {0.author.mention}'.format(message)) 
    if message.content.startswith(prefix + 'twitch'):
        cli = TwitchClient(client_id='Your Twitch Client ID', oauth_token='your-oauth-token')
        channel = cli.channels.get_by_id(115307371)
        embed = discord.Embed(color=0x9932CC)
        embed.title = "Your Twitch Channel Name" 
        embed.add_field(name="Followers", value=(channel.followers))
        embed.add_field(name="Views", value=(channel.views))
        embed.add_field(name="Category", value=(channel.game))
        embed.add_field(name="Stream Title", value=(channel.status))
        embed.add_field(name="Partner", value=(channel.partner))
        embed.set_thumbnail(url=(channel.logo))
        embed.description = f'https://twitch.tv/your-channel-name'
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'commands'):
        await message.channel.send('!twitch !instagram !imdb !zar !spotify !userinfo !server')
    if message.content.startswith(prefix + 'facebook'):
        await message.channel.send('**Your Facebook Page ** ' +  '\n' + 'https://facebook.com/your-facebook-account-name') 
    if message.content.startswith(prefix + 'dice'):
        zar = random.randint(1, 6)
        msg =  zar , "{0.author.mention}".format(message)
        await message.channel.send(msg)
    if message.content.startswith(prefix + 'instagram'):
        html = requests.get('https://www.instagram.com/your-username/')
        soup = BeautifulSoup(html.text, 'html.parser')
        item = soup.select_one("meta[property='og:description']")
        followers = item.get("content").split(",")[0].strip()
        following = item.get("content").split(",")[1].strip()
        embed = discord.Embed(color=0xF3E416)
        embed.title = "Instagram"
        embed.add_field(name="Username", value="your-instagram-username")
        embed.add_field(name="Followers", value=followers)
        embed.add_field(name="Following", value=following)
        embed.add_field(name="URL",value="https://www.instagram.com/your-instagram-username")
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'imdb'):
        await message.channel.send("Input Movie/TV Series Name :arrow_down:")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgcallback = msg.content
        r = requests.get("http://www.omdbapi.com/?apikey=your-omdbapi-key" + msgcallback) 
        ratings = r.json()["imdbRating"]
        embed = discord.Embed(color=0xF3E416)
        embed.title = r.json()["Title"]
        embed.add_field(name="Released Date", value=r.json()["Released"])
        embed.add_field(name="Category", value=r.json()["Genre"])
        embed.add_field(name="Rating", value=str(ratings))
        embed.add_field(name="Director", value=r.json()["Director"])
        embed.add_field(name="Actors", value=r.json()["Actors"])
        embed.add_field(name="Country", value=r.json()["Country"])
        embed.add_field(name="Type", value=r.json()["Type"])
        embed.set_thumbnail(url=r.json()["Poster"])
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'help translate'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "PubyBot TRANSLATOR" 
        embed.add_field(name="!çeviri tr", value="This command is for translating from English to Turkish!")
        embed.add_field(name="!çeviri en", value="This command is for translating from Turkish to English language!")
        embed.add_field(name="!çeviri de", value="This command is for translating from Turkish to German!")
        embed.set_thumbnail(url="https://seeklogo.com/images/G/google-translate-logo-66F8665D22-seeklogo.com.png")
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'userinfo'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "User Information Panel" 
        embed.add_field(name="Username",  value=message.author)
        embed.add_field(name="User ID", value=message.author.id)
        embed.add_field(name="Role", value=message.author.top_role.mention)
        embed.add_field(name="Activity", value=(f"{str(message.author.activity.type).split('.')[-1].title() if message.author.activity else 'N/A'} {message.author.activity.name if message.author.activity else ''}"))
        embed.add_field(name="Account Registration Date", value=message.author.created_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.add_field(name="Server Join Date", value=message.author.joined_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'server'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "Server Information Panel" 
        f = client.get_guild(728275568126197790)
        embed.add_field(name="Server Owner", value=f.owner)
        embed.add_field(name="Server ID", value=f.id)
        embed.add_field(name="Server Name", value=f.name)
        embed.add_field(name="Server Organization Date", value=f.created_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.add_field(name="Region", value=f.region)
        embed.add_field(name="Member", value=f.member_count)
        embed.set_thumbnail(url=f.icon_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'spotify'):
       spot = next((activity for activity in message.author.activities if isinstance(activity, discord.Spotify)), None)
       embed = discord.Embed(color=0x32CD32)
       embed.title = "Spotify"
       embed.add_field(name="Artist", value=spot.artist)
       embed.add_field(name="Title", value=spot.title)
       embed.add_field(name="Album", value=spot.album)
       embed.add_field(name="URL", value=f"[{spot.title}](https://open.spotify.com/track/{spot.track_id})")
       embed.set_thumbnail(url=spot.album_cover_url)
       await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'translate tr'):
        await message.channel.send("Enter Text/Word to Translate: ")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgback = msg.content
        translator = Translator()
        r = translator.translate(msgback, src='en', dest='tr')
        await message.channel.send(r)
    if message.content.startswith(prefix + 'translate en'):
        await message.channel.send("Enter Text/Word to Translate: ")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgback = msg.content
        translator = Translator()
        r = translator.translate(msgback, src='tr', dest='en')
        await message.channel.send(r)
    if message.content.startswith(prefix + 'translate de'):
        await message.channel.send("Enter Text/Word to Translate: ")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgback = msg.content
        translator = Translator()
        r = translator.translate(msgback, src='tr', dest='de')
        await message.channel.send(r)
    if message.content.startswith(prefix + 'clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    await message.channel.purge(limit=count)
    if message.content.startswith(prefix + 'water'):
        user = client.get_user(User ID to which you want to send a message)
        await user.send('You should drink water!')  

client.run(token) 
