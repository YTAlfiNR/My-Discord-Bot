import discord
import random
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member,*,reason= "No reason provided"):
        try:
            await ctx.send("terkick, Reason: "+reason)
        except:
            await ctx.send("yang gw kick mati dmnya, tapi udah gua kick santuy")
        
        await member.kick(reason=reason)
        await print(member.name + " di kick")

    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member,*,reason= "No reason provided"):
        await ctx.send(member.name + " dah ditelan bumi, Reason:"+reason)
        await member.ban(reason=reason)
        await print(member.name + " di ban")

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('s!')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator)==(member_name,member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name +" telah di unbanned.")
                await print(member.name + " di unban")

        await ctx.send(member+" orak eneng")

    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member : discord.Member):
        muted_role = ctx.guild.get_role(770794838999433227)

        await member.add_roles(muted_role)

        await ctx.send(member.mention + " kena penyakit bisu")

    @commands.command(aliases=['boom'])
    @commands.has_permissions(manage_messages=True)
    async def nuke(self,ctx,channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("Channel yang mana?")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Sudah di hancurin")
            await nuke_channel.delete()
            await new_channel.send("udah gua kasih bom atom")
            await ctx.send("Channel berhasil di ledakan")

        else:
            await ctx.send(f"gak ada yang namanya {channel.name} !")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"`{channel.name}` lagi lockdown")
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"`{channel.name}` lagi lockdown")
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"`{channel.name}` dah gak ada covid")

    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, limit=50, member: discord.Member=None):
        await ctx.message.delete()
        msg = []
        try:
            limit = int(limit)
        except:
            return await ctx.send("Please pass in an integer as limit")
        if not member:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f"Purged {limit} messages", delete_after=3)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)

def setup(client):
    client.add_cog(Moderation(client))
