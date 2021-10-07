#coding:UTF-8
import discord
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import locale

TOKEN = "token"
client = discord.Client()
JST = timezone(timedelta(hours=+9), 'JST')

@tasks.loop(seconds=60)
async def loop():
	now = datetime.now(JST).strftime('%H:%M')
	if now == '00:00':
		for channel in client.get_all_channels():
			if channel.name == '出欠確認':
				now = datetime.now(JST)
				wd = ["月", "火", "水", "木", "金", "土", "日"]
				await channel.send('@everyone '+now.strftime('%m/%d\('+wd[now.weekday()]+'\)'))
				for num in range(4):
				message = await channel.send(num+'戦目')
				await message.add_reaction('⭕')
				await message.add_reaction('❌')
loop.start()
client.run(TOKEN)