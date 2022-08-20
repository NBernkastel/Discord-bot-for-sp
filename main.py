import discord
import config
from discord import utils
points = []
usid = []
class MyClient(discord.Client):
    async def on_ready(self):
        print('Бот {0}! активен'.format(self.user))
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=999735820095324282)
        await member.add_roles(role)
    async def on_message(self, message):
        if message.channel.id == config.channel:
            m_points = message.content.split("**")
            global points, usid
            points.append(int(m_points[1]))
            usid.append(message.id)
            print("Активные баллы",points, usid)
        else:
            print("не верные канал")

    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == config.channel and payload.emoji.name == config.emoji:
            member = payload.member
            role_now = int(str(member.roles[1]))
            jojo = role_now + int(points[usid.index(payload.message_id)])
            points.pop(usid.index(payload.message_id))
            usid.pop(usid.index(payload.message_id))
            await member.remove_roles(member.roles[1])
            role = utils.get(member.guild.roles, name=str(jojo))
            await member.add_roles(role)
            print("баллы добавлены")
        else:
            print("не верное эмодзи или канал")
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == config.channel and payload.emoji.name == config.emoji:
            channel = self.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            guild = await(client.fetch_guild(payload.guild_id))
            member = await (guild.fetch_member(payload.user_id))
            role_now = int(str(member.roles[1]))
            m_points = message.content.split("**")
            jojo = role_now - int(m_points[1])
            await member.remove_roles(member.roles[1])
            role = utils.get(member.guild.roles, name=str(jojo))
            await member.add_roles(role)
            print("баллы убраны")
            points.append(int(m_points[1]))
            usid.append(message.id)
        else:
            print("не верное эмодзи или канал")

client = MyClient()
client.run('')
