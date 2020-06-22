import discord
from discord.ext import commands
import requests
import math

domain = 'localhost:7000'

token = 'NzI0NDU1NzI0NTkxMjE4NzQy.XvAcDQ.BZBXswqyl9xWL5g2-bLKkQbzz18'

client = commands.Bot(command_prefix='n!')
client.remove_command('help')
#read... set... goo..!
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!nhelp|version 1.0 now out!'))
    print('Hello Im {0.user}'.format(client))

@client.command()
async def player(ctx, *, arg):
    play_time = requests.get('http://'+domain+'/stat/'+arg+'/play_one_minute').text
    if int(play_time) == 0:
        embed = discord.Embed(color=0xF1C40F)
        embed.add_field(name=":warning: Player Not Found :warning:", value=arg+" is not a player", inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)
    else:
        #play_time = play_time/60+"Hours"
        deaths = requests.get('http://'+domain+'/stat/'+arg+'/deaths').text
        player_kills = requests.get('http://'+domain+'/stat/'+arg+'/player_kills').text
        walked = requests.get('http://'+domain+'/stat/'+arg+'/walk_one_cm').text
        walked_miles = int(walked) * 0.000006213711922
        walked_km = int(walked)/100000
        flown = requests.get('http://'+domain+'/stat/'+arg+'/fly_one_cm').text
        flown_miles = int(flown) * 0.000006213711922
        flown_km = int(flown)/100000
        jumps = requests.get('http://'+domain+'/stat/'+arg+'/jump').text
        fish = requests.get('http://'+domain+'/stat/'+arg+'/fish_caught').text
        armor = requests.get('http://'+domain+'/playerdata/'+arg+'/armor').json()
        coords = requests.get('http://'+domain+'/playerdata/'+arg+'/coords').json()
        player_api = requests.get('https://playerdb.co/api/player/minecraft/'+arg).json()
        if coords['Dimension'] == "minecraft:overworld":
            dimension = 'OverWorld'
        else:
            if coords['Dimension'] == "minecraft:the_nether":
                dimension = 'Nether'
            else:
                dimension = 'End'
        x_coords = "X: `"+str(coords['x'])+'\n`'
        y_coords = " Y: `"+str(coords['y'])+'\n`'
        z_coords = " Z: `"+str(coords['z'])+'`'
        coords = x_coords+y_coords+z_coords
        helmet = armor[3]
        if helmet['name'] == "Air":
            helmet = 'None'
        else:
            helmet_name = helmet['name']
            helmet_enchants = '\n'.join(helmet['enchants'])
            helmet_percent = "{:,.2f}".format((helmet['durability']/helmet['maxDamage'])*100)
            helmet = str(helmet_name)+'\n`'+str(helmet_enchants)+'\n'+str(helmet_percent)+'%`'
        chestplate = armor[2]
        if chestplate['name'] == "Air":
            chestplate = 'None'
        else:
            chestplate_name = chestplate['name']
            chestplate_enchants = '\n'.join(chestplate['enchants'])
            chestplate_percent = "{:,.2f}".format((chestplate['durability']/chestplate['maxDamage'])*100)
            chestplate = str(chestplate_name)+'\n`'+str(chestplate_enchants)+'\n'+str(chestplate_percent)+'%`'
        leggings = armor[1]
        if leggings['name'] == "Air":
            leggings = 'None'
        else:
            leggings_name = leggings['name']
            leggings_enchants = '\n'.join(leggings['enchants'])
            leggings_percent = "{:,.2f}".format((leggings['durability']/leggings['maxDamage'])*100)
            leggings = str(leggings_name)+'\n`'+str(leggings_enchants)+'\n'+str(leggings_percent)+'%`'
        boots = armor[0]
        if boots['name'] == "Air":
            boots = 'None'
        else:
            boots_name = boots['name']
            boots_enchants = '\n'.join(boots['enchants'])
            boots_percent = "{:,.2f}".format((boots['durability']/boots['maxDamage'])*100)
            boots = str(boots_name)+'\n`'+str(boots_enchants)+'\n'+str(boots_percent)+'%`'
        embed=discord.Embed(title=player_api['data']['player']['username'], description="", color=0x14b33c)
        embed.set_thumbnail(url="https://crafatar.com/renders/body/"+player_api['data']['player']['id']+"?overlay")
        embed.add_field(name="Deaths", value='`'+"{:,}".format(int(deaths))+'`', inline=True)
        embed.add_field(name="Distance Walked", value="`Miles: "+"{:,.2f}".format(walked_miles)+'`'+"\n`Km: "+"{:,.2f}".format(walked_km)+'`', inline=True)
        embed.add_field(name="Distance Flown", value="`Miles: "+"{:,.2f}".format(flown_miles)+'`'+"\n`Km: "+"{:,.2f}".format(flown_km)+'`', inline=True)
        embed.add_field(name="Players Killed", value='`'+"{:,}".format(int(player_kills))+'`', inline=True)
        embed.add_field(name="Times Jumped", value='`'+"{:,}".format(int(jumps))+'`', inline=True)
        embed.add_field(name="Fish Caught", value='`'+"{:,}".format(int(fish))+'`', inline=True)
        embed.add_field(name='Coordinates', value=coords, inline=True)
        embed.add_field(name='Dimension', value='`'+dimension+'`', inline=True)
        embed.add_field(name="Helmet", value=helmet, inline=True)
        embed.add_field(name="Chestplate", value=chestplate, inline=True)
        embed.add_field(name="Leggings", value=leggings, inline=True)
        embed.add_field(name="Boots", value=boots, inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)

@client.command()
async def ores(ctx, *, arg):
    play_time = requests.get('http://'+domain+'/stat/'+arg+'/play_one_minute').text
    if int(play_time) == 0:
        embed = discord.Embed(color=0xF1C40F)
        embed.add_field(name=":warning: Player Not Found :warning:", value=arg+" is not a player", inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)
    else:
        #normal ore
        coal = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/coal_ore').text
        iron = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/iron_ore').text
        lapis = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/lapis_ore').text
        gold = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/gold_ore').text
        redstone = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/redstone_ore').text
        diamond = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/diamond_ore').text
        emerald = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/emerald_ore').text
        #nether ores
        quartz = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/nether_quartz_ore').text
        nether_gold = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/nether_gold_ore').text
        ancient_debris = requests.get('http://'+domain+'/stat/'+arg+'/mined/block/ancient_debris').text

        player_api = requests.get('https://playerdb.co/api/player/minecraft/'+arg).json()

        embed=discord.Embed(title=player_api['data']['player']['username'], description="", color=0x14b33c)
        embed.set_thumbnail(url="https://crafatar.com/renders/body/"+player_api['data']['player']['id']+"?overlay")
        embed.add_field(name="Coal Ore Mined", value='`'+"{:,}".format(int(coal))+'`', inline=True)
        embed.add_field(name="Iron Ore Mined", value='`'+"{:,}".format(int(iron))+'`', inline=True)
        embed.add_field(name="Lapis Lazuli Ore Mined", value='`'+"{:,}".format(int(lapis))+'`', inline=True)
        embed.add_field(name="Gold Ore Mined", value='`'+"{:,}".format(int(gold))+'`', inline=True)
        embed.add_field(name="Redstone ore Mined", value='`'+"{:,}".format(int(redstone))+'`', inline=True)
        embed.add_field(name="Diamond Ore Mined", value='`'+"{:,}".format(int(diamond))+'`', inline=True)
        embed.add_field(name="Emerald Ore Mined", value='`'+"{:,}".format(int(emerald))+'`', inline=True)
        embed.add_field(name="Quartz Ore Mined", value='`'+"{:,}".format(int(quartz))+'`', inline=True)
        embed.add_field(name="Nether Gold Ore Mined", value='`'+"{:,}".format(int(nether_gold))+'`', inline=True)
        embed.add_field(name="Ancient Debris Mined", value='`'+"{:,}".format(int(ancient_debris))+'`', inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)

@client.command()
async def mob(ctx, arg1, arg2):
    play_time = requests.get('http://'+domain+'/stat/'+arg1+'/play_one_minute').text
    if int(play_time) == 0:
        embed = discord.Embed(color=0xF1C40F)
        embed.add_field(name=":warning: Player Not Found :warning:", value=arg+" is not a player", inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)
    else:
        killed = requests.get('http://'+domain+'/stat/'+arg1+'/killed/entity_type/'+arg2).text
        killed_by = requests.get('http://'+domain+'/stat/'+arg1+'/killed_by/entity_type/'+arg2).text
        player_api = requests.get('https://playerdb.co/api/player/minecraft/'+arg1).json()

        embed=discord.Embed(title=player_api['data']['player']['username'], description="", color=0x14b33c)
        embed.set_thumbnail(url="https://crafatar.com/renders/body/"+player_api['data']['player']['id']+"?overlay")
        embed.add_field(name=player_api['data']['player']['username']+" Has Killed a " +arg2, value='`'+"{:,}".format(int(killed))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Been Killed By a " +arg2, value='`'+"{:,}".format(int(killed_by))+" Time(s)"+'`', inline=False)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)

@client.command()
async def block(ctx, arg1, arg2):
    play_time = requests.get('http://'+domain+'/stat/'+arg1+'/play_one_minute').text
    if int(play_time) == 0:
        embed = discord.Embed(color=0xF1C40F)
        embed.add_field(name=":warning: Player Not Found :warning:", value=arg+" is not a player", inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)
    else:
        mined = requests.get('http://'+domain+'/stat/'+arg1+'/mined/block/'+arg2).text
        used = requests.get('http://'+domain+'/stat/'+arg1+'/used/item/'+arg2).text
        crafted = requests.get('http://'+domain+'/stat/'+arg1+'/crafted/item/'+arg2).text
        pickedup = requests.get('http://'+domain+'/stat/'+arg1+'/picked_up/item/'+arg2).text
        player_api = requests.get('https://playerdb.co/api/player/minecraft/'+arg1).json()

        embed=discord.Embed(title=player_api['data']['player']['username'], description="", color=0x14b33c)
        embed.set_thumbnail(url="https://crafatar.com/renders/body/"+player_api['data']['player']['id']+"?overlay")
        embed.add_field(name=player_api['data']['player']['username']+" Has Mined " +arg2, value='`'+"{:,}".format(int(mined))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Used (Placed) " +arg2, value='`'+"{:,}".format(int(used))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Crafted " +arg2, value='`'+"{:,}".format(int(crafted))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Picked Up " +arg2, value='`'+"{:,}".format(int(pickedup))+" Time(s)"+'`', inline=False)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)

@client.command()
async def item(ctx, arg1, arg2):
    play_time = requests.get('http://'+domain+'/stat/'+arg1+'/play_one_minute').text
    if int(play_time) == 0:
        embed = discord.Embed(color=0xF1C40F)
        embed.add_field(name=":warning: Player Not Found :warning:", value=arg1+" is not a player", inline=True)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)
    else:
        broken = requests.get('http://'+domain+'/stat/'+arg1+'/broken/item/'+arg2).text
        used = requests.get('http://'+domain+'/stat/'+arg1+'/used/item/'+arg2).text
        crafted = requests.get('http://'+domain+'/stat/'+arg1+'/crafted/item/'+arg2).text
        pickedup = requests.get('http://'+domain+'/stat/'+arg1+'/picked_up/item/'+arg2).text
        player_api = requests.get('https://playerdb.co/api/player/minecraft/'+arg1).json()

        embed=discord.Embed(title=player_api['data']['player']['username'], description="", color=0x14b33c)
        embed.set_thumbnail(url="https://crafatar.com/renders/body/"+player_api['data']['player']['id']+"?overlay")
        embed.add_field(name=player_api['data']['player']['username']+" Has Used " +arg2, value='`'+"{:,}".format(int(used))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Crafted " +arg2, value='`'+"{:,}".format(int(crafted))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Broken " +arg2, value='`'+"{:,}".format(int(broken))+" Time(s)"+'`', inline=False)
        embed.add_field(name=player_api['data']['player']['username']+" Has Picked Up " +arg2, value='`'+"{:,}".format(int(pickedup))+" Time(s)"+'`', inline=False)
        embed.set_footer(text="Need_Not 2.0 | Soon to overthrow Need_Not")
        await ctx.send(embed=embed)


client.run(token)
