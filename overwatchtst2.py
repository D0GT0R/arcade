import discord
from discord.ext import commands
import json
import requests

class Arcade:
	"""Where all the magic shit happens"""
	
	def __init__(self, bot):
		self.bot = bot
			
	@commands.command(no_pm=True)
	async def arcade(self):
		"""Returns arcade game info from the Overwatch API"""
		r = requests.get("https://overwatcharcade.today/api/overwatch/today")
		mode = r.text()
		sub1 =(mode["tile_1"])
		sub2 =(mode["tile_2"])
		sub3 =(mode["tile_3"])
		sub4 =(mode["tile_4"])
		sub5 =(mode["tile_5"])
		sub6 =(mode["tile_6"])
		sub7 =(mode["tile_7"])
		list_of_strings = [sub1["name"] , sub2["name"] , sub3["name"] , sub4["name"] , sub5["name"], sub6["name"], sub7["name"]]
		for backpack in [sub1,sub2,sub3,sub4,sub5,sub6,sub7]:
			await self.bot.say(backpack["name"] + " " + backpack["players"] + "\n")
		
def setup(bot):
    bot.add_cog(Arcade(bot))