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


token = 'NzIxNjkxMTk0OTMyODU0ODM0.XuYNTQ.OdwqrKFJige3PjVyS9MePXKnnAM'
prefix = '!'


client = commands.Bot(command_prefix = prefix)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="twitch.tv/gulsahky"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
   await client.get_channel(744232867961241650).send(f"{member.mention} sunucuya katıldı! :heart:")

@client.event
async def on_member_remove(member):
   await client.get_channel(744232867961241650).send(f"{member.mention} sunucudan ayrıldı! :slight_frown: ")


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
        cli = TwitchClient(client_id='5kmpg682m210rk1qipmxhicd4qh4st', oauth_token='oauth:fih3kjipc7k8kh5zpm3lux9sniso0w')
        channel = cli.channels.get_by_id(115307371)
        embed = discord.Embed(color=0x9932CC)
        embed.title = "GULSAHKY" 
        embed.add_field(name="Takipçi", value=(channel.followers))
        embed.add_field(name="Görüntülenme", value=(channel.views))
        embed.add_field(name="Kategori", value=(channel.game))
        embed.add_field(name="Yayın Başlığı", value=(channel.status))
        embed.add_field(name="Partner", value=(channel.partner))
        embed.set_thumbnail(url=(channel.logo))
        embed.description = f'https://twitch.tv/gulsahky'
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'komutlar'):
        await message.channel.send('!twitch !instagram !imdb !zar !spotify !userinfo !server')
    if message.content.startswith(prefix + 'facebook'):
        await message.channel.send('**GULSAHKY Facebook Page ** ' +  '\n' + 'https://facebook.com/gulsahky') 
    if message.content.startswith(prefix + 'zar'):
        zar = random.randint(1, 6)
        msg =  zar , "{0.author.mention}".format(message)
        await message.channel.send(msg)
    if message.content.startswith(prefix + 'instagram'):
        html = requests.get('https://www.instagram.com/gulsahky/')
        soup = BeautifulSoup(html.text, 'html.parser')
        item = soup.select_one("meta[property='og:description']")
        name = item.find_previous_sibling().get("content").split("•")[0]
        followers = item.get("content").split(",")[0]
        following = item.get("content").split(",")[1].strip()
        embed = discord.Embed(color=0xF3E416)
        embed.title = "Instagram"
        embed.add_field(name="Kullanıcı Adı", value=name)
        embed.add_field(name="Takipçi", value=followers)
        embed.add_field(name="Takip Edilen", value=following)
        embed.add_field(name="URL",value="https://www.instagram.com/gulsahky")
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'imdb'):
        await message.channel.send("İçerik Adı Giriniz :arrow_down:")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgcallback = msg.content
        r = requests.get("http://www.omdbapi.com/?apikey=50b2eecc&t=" + msgcallback) 
        ratings = r.json()["imdbRating"]
        embed = discord.Embed(color=0xF3E416)
        embed.title = r.json()["Title"]
        embed.add_field(name="Çıkış Tarihi", value=r.json()["Released"])
        embed.add_field(name="Kategori", value=r.json()["Genre"])
        embed.add_field(name="Puan", value=str(ratings))
        embed.add_field(name="Yönetmen", value=r.json()["Director"])
        embed.add_field(name="Oyuncular", value=r.json()["Actors"])
        embed.add_field(name="Menşei", value=r.json()["Country"])
        embed.add_field(name="Türü", value=r.json()["Type"])
        embed.set_thumbnail(url=r.json()["Poster"])
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'bilgi çeviri'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "PubyBot TRANSLATOR" 
        embed.add_field(name="!çeviri tr", value="Bu komut İngilizce'den Türkçe diline çeviri yapmak içindir!")
        embed.add_field(name="!çeviri en", value="Bu komut Türkçe'den İngilizce diline çeviri yapmak içindir!")
        embed.add_field(name="!çeviri de", value="Bu komut Türkçe'den Almanca diline çeviri yapmak içindir!")
        embed.set_thumbnail(url="https://seeklogo.com/images/G/google-translate-logo-66F8665D22-seeklogo.com.png")
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'userinfo'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "Kullanıcı Bilgileri Paneli" 
        embed.add_field(name="Kullanıcı Adı",  value=message.author)
        embed.add_field(name="Kullanıcı ID", value=message.author.id)
        embed.add_field(name="Rol", value=message.author.top_role.mention)
        embed.add_field(name="Aktivite", value=(f"{str(message.author.activity.type).split('.')[-1].title() if message.author.activity else 'N/A'} {message.author.activity.name if message.author.activity else ''}"))
        embed.add_field(name="Hesap Açılış Tarihi", value=message.author.created_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.add_field(name="Sunucuya Katılma Tarihi", value=message.author.joined_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'server'):
        embed = discord.Embed(color=0x10A1C5)
        embed.title = "Sunucu Bilgileri Paneli" 
        f = client.get_guild(728275568126197790)
        embed.add_field(name="Sunucu Sahibi", value=f.owner)
        embed.add_field(name="Sunucu ID", value=f.id)
        embed.add_field(name="Sunucu Adı", value=f.name)
        embed.add_field(name="Sunucu Kuruluş Tarihi", value=f.created_at.strftime("%a, %#d-%m-%Y, %H:%M"))
        embed.add_field(name="Bölge", value=f.region)
        embed.add_field(name="Üye", value=f.member_count)
        embed.set_thumbnail(url=f.icon_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'spotify'):
       spot = next((activity for activity in message.author.activities if isinstance(activity, discord.Spotify)), None)
       embed = discord.Embed(color=0x32CD32)
       embed.title = "Spotify"
       embed.add_field(name="Şarkıcı", value=spot.artist)
       embed.add_field(name="Şarkı", value=spot.title)
       embed.add_field(name="Albüm", value=spot.album)
       embed.add_field(name="URL", value=f"[{spot.title}](https://open.spotify.com/track/{spot.track_id})")
       embed.set_thumbnail(url=spot.album_cover_url)
       await message.channel.send(embed=embed)
    if message.content.startswith(prefix + 'çeviri tr'):
        await message.channel.send("Çevirilecek Metin/Kelime Giriniz: ")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgback = msg.content
        translator = Translator()
        r = translator.translate(msgback, src='en', dest='tr')
        await message.channel.send(r)
    if message.content.startswith(prefix + 'çeviri en'):
        await message.channel.send("Çevirilecek Metin/Kelime Giriniz: ")
        msg = await client.wait_for('message', check=lambda message: message.author)
        msgback = msg.content
        translator = Translator()
        r = translator.translate(msgback, src='tr', dest='en')
        await message.channel.send(r)
    if message.content.startswith(prefix + 'çeviri de'):
        await message.channel.send("Çevirilecek Metin/Kelime Giriniz: ")
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
    if message.content.startswith(prefix + 'su'):
        user = client.get_user(415506092702040064)
        await user.send('Su iç!')  

client.run(token) 
