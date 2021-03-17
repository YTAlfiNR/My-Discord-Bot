import discord
import os
import datetime
import random
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive

client = commands.Bot(command_prefix = 's!')
client.remove_command("help")
status = cycle(['s!help | Semua yang sirna kan kembali', 's!help | Semua yang sirna kan kembali.', 's!help | Semua yang sirna kan kembali..', 's!help | Semua yang sirna kan kembali...', 's!help | Semua yang sirna kan terganti', 's!help | Semua yang sirna kan terganti.', 's!help | Semua yang sirna kan terganti..', 's!help | Semua yang sirna kan terganti...', 's!help | Dan ku bertanya untuk apa', 's!help | Dan ku bertanya untuk apa.', 's!help | Dan ku bertanya untuk apa..', 's!help | Dan ku bertanya untuk apa...', 's!help | Angan yang belum di ja', 's!help | Angan yang belum di jawab juga', 's!help | ...', 's!help | Amin paling serius', 's!help | (Detik jam)', 's!help | Simpul jari yang erat (Sang gerilyawan)', 's!help | ...', 's!help | Doa semakin berat', 's!help | (Berdentang)', 's!help | (Mengingatkan)', 's!help | Rasakan lah (Ciri pikiran)', 's!help | Semua perasaanmu (Khas pagi buta menyerang aku)', 's!help | ...', 's!help | Malam ini (Yang tegang)', 's!help | Milikmu sendiri', 's!help | (Terus - terusan)'])

players = {}

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("gak ada perm")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("mangsut")
        await ctx.message.delete()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use s!help <command> for extended information")

    em.add_field(name = "Moderation", value = "`kick`, `ban`, `clear`, `nuke`, `lockdown`")
    em.add_field(name = "untitled", value = "`ping`, `echo`, `suggest`, `avatar` , `whois`")
    em.add_field(name = "Music", value = "`play`, `pause`, `queue`, `repeat`, `resume`, `skip`, `stop`, `volume`")
    await ctx.send(embed = em)



@help.command()
async def kick(ctx):

    em = discord.Embed(title = "Kick", description = "kick member dari server",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!kick <member> [alasan]")

    await ctx.send(embed = em)


@help.command()
async def ban(ctx):

    em = discord.Embed(title = "Ban", description = "Ban member dari server",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!ban <member> [alasan]")

    await ctx.send(embed = em)

@help.command()
async def clear(ctx):

    em = discord.Embed(title = "Clear", description = "Menghapus pesan server",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!clear <jumlah>")

    await ctx.send(embed = em)

@help.command()
async def nuke(ctx):

    em = discord.Embed(title = "Nuke", description = "Bom atom",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!nuke <#nama-channel>")

    await ctx.send(embed = em)

@help.command()
async def echo(ctx):

    em = discord.Embed(title = "Echo", description = "ya begitulah",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!echo <pesan random>")

    await ctx.send(embed = em)

@help.command()
async def lockdown(ctx):

    em = discord.Embed(title = "Lockdown", description = "Ngelock channel",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!lockdown [#nama-channel]")

    await ctx.send(embed = em)

@help.command()
async def suggest(ctx):

    em = discord.Embed(title = "Suggest", description = "memberikan saran",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!suggest <saran kamu>")

    await ctx.send(embed = em)

@help.command()
async def covid(ctx):

    em = discord.Embed(title = "Covid-19 Cases", description = ".",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "s!covid <nama negara>")

    await ctx.send(embed = em)

@client.command()
async def echo(ctx, *, args):
    if args == ('@everyone'):
        await ctx.send('no no haram')
    elif args == ('alfi tolol'):
        await ctx.send('no.')
    elif args == ('@here'):
        await ctx.send('still haram')
    else:
        await ctx.send(args)

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

keep_alive()
client.run('TOKEN BOT KAMU')
