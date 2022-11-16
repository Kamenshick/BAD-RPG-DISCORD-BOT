import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import Activity, ActivityType
import datetime
import random
import json
from discord.utils import get


intents = discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)
intents.members = True
Bot = commands.Bot(command_prefix="/", intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_member_join(member):
	channel = Bot.get_channel(809288477501292544)
	role = discord.utils.get(member.guild.roles,id=812759375374319626)
	await member.add_roles(role)
	await asyncio.sleep(2)
	await channel.send(f"{member.mention} Добро пожаловать на сервер! Обязательно посети канал <#809288027896676352> ")
#@Bot.event
#async def on_member_remove(member):
 #   channel = Bot.get_channel(852937583290089522)
  #  await channel.send(f"{member} Покинул нас!")

def provrek_buy(arg):
	wep = 0
	arm = 0
	other = 0
	pot = 0
	if arg == 'Стальной меч':
		cost = 100
		uron = 5
		uvr = 4
		wep = 1
		st = "Steel sword"
	elif arg == 'Кинжал':
		cost = 75
		uron = 2
		uvr = 2
		wep = 1
		st = "Dagger"
	elif arg == 'Алебарда':
		cost = 350
		uron = 7
		uvr = 2
		wep = 1
		st = "Alebarda"
	elif arg == 'Бёрдыш':
		cost = 500
		uron = 10
		uvr = 5
		wep = 1
		st = "Berdish"
	elif arg == 'Качественный палаш':
		cost = 1000
		uron = 12
		uvr = 6
		wep = 1
		st = "Palash"
	elif arg == 'Улучшенная рапира':
		cost = 1200
		uron = 15
		uvr = 9
		wep = 1
		st = "Rapira"
	elif arg == 'Лук':
		cost = 800
		uron = 7
		uvr = 2
		wep = 1
		st = "Onin"
	elif arg == 'Мантия': 
		cost = 80
		zach = 3
		otds = 0
		arm = 1
		st = "Cloak"
	elif arg == 'Кожаная броня':  
		cost = 110
		zach = 4
		otds = 1
		arm = 1
		st = "Kosh Arm"
	elif arg == 'Кольчуга':
		cost = 140 
		zach = 5
		otds = 2
		arm = 1
		st = "Сhain armor"
	elif arg == 'Латы':
		cost = 600
		zach = 10
		otds = 4
		arm = 1
		st = "Lati"
	elif arg == 'Зерцальный доспех':
		cost = 1500
		zach = 21
		otds = 10
		arm = 1
		st = "Zerchal"
	elif arg == 'Кираса с тассетами':
		cost = 800
		zach = 15
		otds = 7
		arm = 1
		st = "Kirassa"
	elif arg == 'Льяная рубаха':
		cost = 0
		zach = 1
		otds = 0
		arm = 1
		st = "Lien"
	elif arg == 'Зелье здоровья':
		cost = 25 
		st = "Health potion"
		pot = 1
	elif arg == 'Зелье Силы':
		cost = 60 
		st = "Attack potion" 
		pot = 1
	elif arg == 'Кирка':
		helth = 5
		other = 1
		cost = 50
		st = "Miner" 
	elif arg == 'Очень прочная кирка':
		helth = 15
		other = 1
		cost = 100
		st = "Good Miner"
	elif arg == 'Стрелы':
		helth = 15 
		other = 1
		cost =30
		st = "Strely"
	if wep != 0:
		k = [cost,uron,uvr,st]
		return(k)
	elif arm != 0:
		k = [cost,zach,otds,st]
		return(k)
	elif pot != 0:
		k = [cost,st]
		return(k)
	elif other != 0:
		k = [cost,helth,st]
		return(k)

queue = []
@Bot.command()
async def bonus(ctx):
	with open('economy.json', 'r') as f:
		money = json.load(f)
	if not str(ctx.author.id) in queue:
		emb = discord.Embed(description=f'**{ctx.author}** Вы получили свой ежедневный бонус в 40 :diamonds:')
		await ctx.send(embed= emb)
		money[str(ctx.author.id)]['Money'] += 40
		queue.append(str(ctx.author.id))
		with open('economy.json', 'w') as f:
			json.dump(money, f)
		await asyncio.sleep(60*1440)
		queue.remove(str(ctx.author.id))
	if str(ctx.author.id) in queue:
		emb = discord.Embed(description=f'**{ctx.author}** Вы уже получили свой ежедневный бонус ')
		await ctx.send(embed= emb)

#@Bot.command()
#async def cash(ctx, member: discord.Member = None):	
#    if member == ctx.author or member == None:
#        with open('economy.json', 'r') as f:
#            money = json.load(f)
#        emb = discord.Embed(description=f'Баланс игрока **{ctx.author}** {money[str(ctx.author.id)]["Money"]} :diamonds: ')
#        await ctx.send(embed = emb)
#   else:
#        emb = discord.Embed(description=f'Вам не позволено видеть баланс других пользователей ')
#        await ctx.send(embed = emb)
#        pass


# ещё проверить на наличии кирки        
quars = []  
mine_ore = 1
@Bot.command()
async def mine(ctx):
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)  
	gkk1 = ctx.author.roles
	man = False
	vam = False
	for gk in gkk1:
		if str(gk) == "Human":
			man = True
		if str(gk) == "Vampire": 
			vam = True
	if captr2 or captr1:
			if vam:
				if stat["Per"] == 0 and captr1 or stat["Vt"] == 0 and captr2:	
					if "Miner" in inv[str(ctx.author.id)]["Other"]:
						if not str(ctx.author.id) in quars:
							emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы шахте вы смогли добыть:')
							emb.add_field(name = 'Ископаемое', value = '{} :gem: '.format(mine_ore))
							await ctx.send(embed= emb)
							users[str(ctx.author.id)]['ore'] += 1
							inv[str(ctx.author.id)]["Other"]["Miner"][1] -= 1
							if inv[str(ctx.author.id)]["Other"]["Miner"][1] == 0:
								emb = discord.Embed(title='Добыча ископаемых', description=f'Твоя кирка сломалась! :x: ')
								await ctx.send(embed= emb)
								del inv[str(ctx.author.id)]["Other"]["Miner"]
							quars.append(str(ctx.author.id))
							with open('informat.json', 'w') as f:
								json.dump(users, f)
							with open('inventory.json', 'w') as f:
								json.dump(inv, f)
							await asyncio.sleep(60*5)
							quars.remove(str(ctx.author.id))
						if str(ctx.author.id) in quars:
							emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы слишком устали, отдохните 5 минут. ')
							await ctx.send(embed= emb)
					elif "Good Miner" in inv[str(ctx.author.id)]["Other"]:
						if not str(ctx.author.id) in quars:
							emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы шахте вы смогли добыть:')
							emb.add_field(name = 'Ископаемое', value = '{} :gem: '.format(mine_ore))
							await ctx.send(embed= emb)
							users[str(ctx.author.id)]['ore'] += 1
							inv[str(ctx.author.id)]["Other"]["Good Miner"][1] -= 1
							if inv[str(ctx.author.id)]["Other"]["Good Miner"][1] == 0:
								emb = discord.Embed(title='Добыча ископаемых', description=f'Твоя кирка сломалась! :x: ')
								await ctx.send(embed= emb)
								del inv[str(ctx.author.id)]["Other"]["Good Miner"]
							quars.append(str(ctx.author.id))
							with open('informat.json', 'w') as f:
								json.dump(users, f)
							with open('inventory.json', 'w') as f:
								json.dump(inv, f)
							await asyncio.sleep(60*5)
							quars.remove(str(ctx.author.id))
						if str(ctx.author.id) in quars:
							emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы слишком устали, отдохните 5 минут. ')
							await ctx.send(embed= emb)
					else:
						emb = discord.Embed(title='Добыча ископаемых', description=f'У вас нет кирки! :x:')
						await ctx.send(embed= emb)
					
				else:
					emb = discord.Embed(title='Добыча ископаемых', description=f'Эта территория находится не под вашим контролем :x:')
					await ctx.send(embed= emb)
			if man:
					if stat["Per"] == 1 and captr1 or stat["Vt"] == 1 and captr2:		
						if "Miner" in inv[str(ctx.author.id)]["Other"]:
							if not str(ctx.author.id) in quars:
								emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы шахте вы смогли добыть:')
								emb.add_field(name = 'Ископаемое', value = '{} :gem: '.format(mine_ore))
								await ctx.send(embed= emb)
								users[str(ctx.author.id)]['ore'] += 1
								inv[str(ctx.author.id)]["Other"]["Miner"][1] -= 1
								if inv[str(ctx.author.id)]["Other"]["Miner"][1] == 0:
									emb = discord.Embed(title='Добыча ископаемых', description=f'Твоя кирка сломалась! :x: ')
									await ctx.send(embed= emb)
									del inv[str(ctx.author.id)]["Other"]["Miner"]
								quars.append(str(ctx.author.id))
								with open('informat.json', 'w') as f:
									json.dump(users, f)
								with open('inventory.json', 'w') as f:
									json.dump(inv, f)
								await asyncio.sleep(60*5)
								quars.remove(str(ctx.author.id))
							if str(ctx.author.id) in quars:
								emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы слишком устали, отдохните 5 минут. ')
								await ctx.send(embed= emb)
						elif "Good Miner" in inv[str(ctx.author.id)]["Other"]:
							if not str(ctx.author.id) in quars:
								emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы шахте вы смогли добыть:')
								emb.add_field(name = 'Ископаемое', value = '{} :gem: '.format(mine_ore))
								await ctx.send(embed= emb)
								users[str(ctx.author.id)]['ore'] += 1
								inv[str(ctx.author.id)]["Other"]["Good Miner"][1] -= 1
								if inv[str(ctx.author.id)]["Other"]["Good Miner"][1] == 0:
									emb = discord.Embed(title='Добыча ископаемых', description=f'Твоя кирка сломалась! :x: ')
									await ctx.send(embed= emb)
									del inv[str(ctx.author.id)]["Other"]["Good Miner"]
								quars.append(str(ctx.author.id))
								with open('informat.json', 'w') as f:
									json.dump(users, f)
								with open('inventory.json', 'w') as f:
									json.dump(inv, f)
								await asyncio.sleep(60*5)
								quars.remove(str(ctx.author.id))
							if str(ctx.author.id) in quars:
								emb = discord.Embed(title='Добыча ископаемых', description=f'**{ctx.author}** Вы слишком устали, отдохните 5 минут. ')
								await ctx.send(embed= emb)
						else:
							emb = discord.Embed(title='Добыча ископаемых', description=f'У вас нет кирки! :x:')
							await ctx.send(embed= emb)
					
					else:
						emb = discord.Embed(title='Добыча ископаемых', description=f'Эта территория находится не под вашим контролем :x:')
						await ctx.send(embed= emb)	
	else:
		emb = discord.Embed(title='Добыча ископаемых', description=f'Рядом с вами нет шахт. :x:')
		await ctx.send(embed= emb)


def random_zarab():
    rand = random.randint(1,5)
    return rand

meet_dostat = random_zarab()
quars = []  
@Bot.command()
async def hunt(ctx):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	if les1 == True:
		if "Onin" in inv[str(ctx.author.id)]['Weapon']:
			if "Strely" in inv[str(ctx.author.id)]['Other']:
				if inv[str(ctx.author.id)]['Other']["Strely"][1] > 0:
					if not str(ctx.author.id) in quars:
						emb = discord.Embed(title='Охота', description=f'**{ctx.author}** Во время охоты вы смогли добыть:')
						emb.add_field(name = 'Мясо', value = '{} :cut_of_meat: '.format(meet_dostat))
						await ctx.send(embed= emb)
						inv[str(ctx.author.id)]['Other']["Strely"][1] -= 1
						users[str(ctx.author.id)]['meet'] += meet_dostat
						quars.append(str(ctx.author.id))
						with open('informat.json', 'w') as f:
							json.dump(users, f)
						with open('inventory.json', 'w') as f:
							json.dump(inv, f)
						await asyncio.sleep(60*5)
						quars.remove(str(ctx.author.id))
					if str(ctx.author.id) in quars:
						emb = discord.Embed(title='Охота', description=f'**{ctx.author}** Вы слишком устали, отдохните 5 минут. ')
						await ctx.send(embed= emb)
					else:
						emb = discord.Embed(title='Охота', description=f'У вас нет стрел! :x:')
						await ctx.send(embed= emb)
			else:
				emb = discord.Embed(title='Охота', description=f'У вас нет стрел! :x:')
				await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Охота', description=f'У вас нет лука! :x:')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Охота', description=f'Вы не в лесу! :x:')
		await ctx.send(embed= emb)

@Bot.command()
async def cash_hunt(ctx):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)  
	meets_pol = users[str(ctx.author.id)]['meet']   
	if meets_pol >= 10:
		emb = discord.Embed(title='Мясная лавка', description=f'**{ctx.author}** Вы смогли обменять 10 кусков мяса на 15 :diamonds: ')
		await ctx.send(embed= emb)
		money[str(ctx.author.id)]['Money'] += 15
		users[str(ctx.author.id)]['meet'] -=10
		with open('informat.json', 'w') as f:
			json.dump(users, f)
		with open('economy.json', 'w') as f:
			json.dump(money, f)
	else:
		emb = discord.Embed(title='Мясная лавка', description=f'**{ctx.author}** У вас недостаточно :cut_of_meat: для обмена  ')
		await ctx.send(embed= emb)
@Bot.command()
async def cash_mine(ctx):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)  
	ore_pol = users[str(ctx.author.id)]['ore']   
	if ore_pol >= 5:
		emb = discord.Embed(title='Ювелирная лавка', description=f'**{ctx.author}** Вы смогли обменять 5 :gem: на 10 :diamonds:  ')
		await ctx.send(embed= emb)
		money[str(ctx.author.id)]['Money'] += 10
		users[str(ctx.author.id)]['ore'] -=5
		with open('informat.json', 'w') as f:
			json.dump(users, f)
		with open('economy.json', 'w') as f:
			json.dump(money, f)
	else:
		emb = discord.Embed(title='Ювелирная лавка', description=f'**{ctx.author}** У вас недостаточно :gem: для обмена')
		await ctx.send(embed= emb)

a = ['пизда','Пизда','вагина','Вагина','даун','Даун','долбаёб','Долбаёб','обмудок','Обмудок','дегенерат','Дегенерат','Пидор','пидор','пидорас','Пидорас','ёбнутый','Ёбнутый', 'Член', 'член', 'хуй', 'Хуй', 'Залупа', 'залупа','Ебать', 'ебать', 'Ахуенно', 'ахуенно', 'Пиздато', 'пиздато',  'заебато', 'Заебато', 'Блять', 'блять', 'Сука', 'сука', 'хуила', 'Хуила', 'Пидр', 'пидр','Пидарас', 'пидарас', ' Гомогей', 'гомогей', 'Соси', 'соси', 'Отсоси', 'отсоси', 'похуй', 'Похуй','Блядина','Пиздина','Ебало','Хуесос','Говноплюй','Пиздатый','Ахуенный']
@Bot.event
async def on_message(message):
	try:
		await Bot.change_presence(status=discord.Status.online,activity= discord.Game('Vampire RP'))
		if message.author == Bot.user:
			return
		else:
			content = message.content.split()
			for word in content:
				if word in a:
					await message.delete()
	except:
		pass

captr1 = 0
captr2 = 0
olo = 0
don = 0
les1 = 0
@Bot.listen()
async def on_message(message):
	channel = Bot.get_guild(809288477501292544)
	global captr1 
	global captr2 
	global olo
	global don
	global les1
	adolf = ["《🏰》╎кират","《🏯》╎вантерхольм"]
	captr11 = ["《⛏》╎шахты-кембарийской-горы"]
	captr22 = ["《⛏》╎месторождение-в-квантунских-лесах"]
	lar = ["《🏔》╎касова-гора"] 
	geybar = ["《🏕》╎квантунский-лес"]
	if str(message.channel) in geybar:
		les1 = True
	if str(message.channel) in adolf:
		olo = True
	else: 
		olo = False
	if str(message.channel) in captr11:
		captr1 = True
	else: 
		captr1 = False
	if str(message.channel) in captr22:
		captr2 = True
	else: 
		captr2 = False
	if str(message.channel) in lar:
		don = True
	else:
		don = False
	await Bot.process_commands(message)


@Bot.listen()
async def on_message(message):
	for member in message.guild.members:
		for kk in member.roles:
			if str(kk) == "Захват":
				ks1 = True
			else:
				ks1 = False
			if ks1 == True:
				if warzaxvat != 1:
					remove_role = discord.utils.get(member.guild.roles,id=829377070223196201)
					await member.remove_roles(remove_role)
				if warzaxvat == 1:
					t = member.status
					if t != discord.Status.online:
						remove_role = discord.utils.get(member.guild.roles,id=829377070223196201)
						await member.remove_roles(remove_role)

@Bot.listen()
async def on_message(message):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)

	async def update_data(users,user):
		if not user in users:
			users[user] = {}
			users[user]['rep'] = 0
			users[user]['lvl'] = 1

	await update_data(users,str(message.author.id))

	rep = users[str(message.author.id)]['rep']  
	lvl = users[str(message.author.id)]['lvl'] 

	if lvl == 50:
		if rep > 490 and rep <= 500:
			gkk1 = message.author.id.roles
			ks1 = False
			for gk in gkk1:
					if str(gk) == 'Vampire':
						ks1 = True
			if ks1:
				role = discord.utils.get(message.author.id.roles,id=826832703973490710)
				await message.author.id.add_roles(role)
				emb = discord.Embed(description=f'**{ctx.author}** Вы стали Лордом!')    
				await ctx.send(embed = emb)
				users[str(message.author.id)]['lovk'] = 7 
				users[str(message.author.id)]['sil'] = 4
				users[str(message.author.id)]['lvl'] += 1 
				users[str(message.author.id)]['rep']  = 0

	if rep >= (lvl*10):
		users[str(ctx.author.id)]['lvl'] += 1 
		users[str(ctx.author.id)]['rep']  = 0

	with open('economy.json', 'w') as f:
		json.dump(money, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)

@Bot.command()
async def account(ctx, member: discord.Member = None):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)  
	if member == ctx.author or member == None:
		emb = discord.Embed(description=f'Аккаунт:')
		emb.add_field(name = 'Имя:', value = '**{}**'.format(ctx.author), inline = False)
		emb.add_field(name = 'Мясо:', value = f'{users[str(ctx.author.id)]["meet"]} :cut_of_meat: ', inline = False)
		emb.add_field(name = 'Руда:', value = f'{users[str(ctx.author.id)]["ore"]} :gem:', inline = False)
		emb.add_field(name = 'Уровень:', value = f'{users[str(ctx.author.id)]["lvl"]} :star:', inline = False)
		emb.add_field(name = 'Здоровье:', value = f'{users[str(ctx.author.id)]["hp"]} :hearts:', inline = False)
		emb.add_field(name = 'Оружие:', value = f'{inv[str(ctx.author.id)]["Use"]["Weapon"][0]} :crossed_swords:', inline = False) 
		emb.add_field(name = 'Броня:', value = f'{inv[str(ctx.author.id)]["Use"]["Armor"][0]} :martial_arts_uniform:', inline = False)
		emb.add_field(name = 'Деньги:', value = f'{money[str(ctx.author.id)]["Money"]} :diamonds:', inline = False)
		await ctx.send(embed = emb)
	else:
		emb = discord.Embed(description=f'Вам не позволено видеть аккаунт других пользователей ')
		await ctx.send(embed = emb)
		pass   


@Bot.command()
async def reg_Vamp(ctx):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)  
	with open('inventory.json', 'r') as f:
		inv = json.load(f)  
	if not str(ctx.author.id) in money:
		inv[str(ctx.author.id)] = {}
		inv[str(ctx.author.id)]['Potion'] = {'Health potion': ['Зелье здоровья',1], 'Attack potion': ['Зелье Силы',0]}
		inv[str(ctx.author.id)]['Armor']= {'Cloak':['Мантия',0,3], 'Lien':['Льяная рубаха',0,1]}
		inv[str(ctx.author.id)]['Weapon'] = {'Dagger':['Кинжал',2,2]}
		inv[str(ctx.author.id)]['Other'] = {'Map': ['Карта',1]}
		inv[str(ctx.author.id)]['Leg'] = 4
		inv[str(ctx.author.id)]['Hand'] = 5
		inv[str(ctx.author.id)]['Tors'] = 7
		inv[str(ctx.author.id)]['Arm'] = 4
		inv[str(ctx.author.id)]['Use'] = {'Armor':inv[str(ctx.author.id)]['Armor']['Cloak'], 'Weapon': inv[str(ctx.author.id)]['Weapon']['Dagger']}
		money[str(ctx.author.id)] = {}
		money[str(ctx.author.id)]['Money'] = 100
		users[str(ctx.author.id)] = {}
		users[str(ctx.author.id)]['rep'] = 0
		users[str(ctx.author.id)]['lvl'] = 1
		users[str(ctx.author.id)]['meet'] = 0
		users[str(ctx.author.id)]['hp'] = 100
		users[str(ctx.author.id)]['ore'] = 0
		users[str(ctx.author.id)]['ore_mine'] = 0
		users[str(ctx.author.id)]['lovk'] = 5 
		users[str(ctx.author.id)]['sil'] = 3
		users[str(ctx.author.id)]['race'] = 1   
		role = discord.utils.get(ctx.guild.roles,id=809287144899215382)
		await ctx.author.add_roles(role)
		remove_role = discord.utils.get(ctx.guild.roles,id=812759375374319626)
		await ctx.author.remove_roles(remove_role)
		emb = discord.Embed(description=f'**{ctx.author}** Регистрация прошла успешно')    
		await ctx.send(embed = emb)
		with open('economy.json', 'w') as f:
			json.dump(money, f)
		with open('informat.json', 'w') as f:
			json.dump(users, f)
		with open('inventory.json', 'w') as f:
			json.dump(inv, f)
	else:
		emb = discord.Embed(description=f'**{ctx.author}** У вас уже есть аккаунт')    
		await ctx.send(embed = emb) 


@Bot.command()
async def reg_Hum(ctx):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)  
	with open('inventory.json', 'r') as f:
		inv = json.load(f)  
	if not str(ctx.author.id) in money:
		inv[str(ctx.author.id)] = {}
		inv[str(ctx.author.id)]['Potion'] = {'Health potion': ['Зелье здоровья',1], 'Attack potion': ['Зелье Силы',0]}
		inv[str(ctx.author.id)]['Armor']= {'Сhain armor':['Кольчуга',2,5], 'Lien':['Льяная рубаха',0,1]} #Имя, Штраф к увороту, защита
		inv[str(ctx.author.id)]['Weapon'] = {'Steel sword':['Стальной меч',5,4]}#Имя,урон, шанс промаха 
		inv[str(ctx.author.id)]['Use'] = {'Armor':inv[str(ctx.author.id)]['Armor']['Сhain armor'], 'Weapon': inv[str(ctx.author.id)]['Weapon']['Steel sword']}
		inv[str(ctx.author.id)]['Other'] = {'Map': ['Карта',1]}
		inv[str(ctx.author.id)]['Leg'] = 4
		inv[str(ctx.author.id)]['Hand'] = 5
		inv[str(ctx.author.id)]['Tors'] = 7
		inv[str(ctx.author.id)]['Arm'] = 4
		money[str(ctx.author.id)] = {}
		money[str(ctx.author.id)]['Money'] = 100
		users[str(ctx.author.id)] = {}
		users[str(ctx.author.id)]['rep'] = 0
		users[str(ctx.author.id)]['lvl'] = 1
		users[str(ctx.author.id)]['meet'] = 0
		users[str(ctx.author.id)]['hp'] = 100
		users[str(ctx.author.id)]['ore'] = 0
		users[str(ctx.author.id)]['lovk'] = 5 
		users[str(ctx.author.id)]['sil'] = 3
		users[str(ctx.author.id)]['race'] = 1  
		role = discord.utils.get(ctx.guild.roles,id=809287150116798466)
		await ctx.author.add_roles(role)
		remove_role = discord.utils.get(ctx.guild.roles,id=812759375374319626)
		await ctx.author.remove_roles(remove_role)
		emb = discord.Embed(description=f'**{ctx.author}** Регистрация прошла успешно')    
		await ctx.send(embed = emb)
		with open('economy.json', 'w') as f:
			json.dump(money, f)
		with open('informat.json', 'w') as f:
			json.dump(users, f)
		with open('inventory.json', 'w') as f:
			json.dump(inv, f)
	else:
		emb = discord.Embed(description=f'**{ctx.author}** У вас уже есть аккаунт')    
		await ctx.send(embed = emb) 

@Bot.command()
async def give(ctx,member:discord.Member,arg:int):
	with open('economy.json', 'r') as f:
		money = json.load(f) 
	if money[str(ctx.author.id)]['Money'] >= arg:
		emb = discord.Embed(description=f'{arg} :diamonds: передано {member}')
		money[str(ctx.author.id)]['Money'] -= arg
		money[str(member.id)]['Money']  += arg
		await ctx.send(embed= emb)
	else: 
		emb = discord.Embed(title='Передача средств:', description=f'**Недостаточно :diamonds:**')
		await ctx.send(embed= emb)
	with open('economy.json', 'w') as f:
			json.dump(money, f)


@Bot.command()
async def fight(ctx):
	g = ctx.author.roles
	jll = 0
	kka = 0
	cap = 0
	for gk in g:
		if str(gk) == 'Режим боя':
			jll = 1
		if str(gk) == 'В бою':
			kka = 1
		if str(gk) == 'Захват':
			cap = 1
	if jll == 0:
		emb = discord.Embed(title='Бой', description=f'**Вы вошли в режим боя**')
		await ctx.send(embed= emb)
		role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
		await ctx.author.add_roles(role)
	else:
		if kka == 1:
			emb = discord.Embed(title='Бой', description=f'**Вы не можете выйти из режима боя пока вы в бою :x:**')
			await ctx.send(embed= emb)
		elif cap == 1:
			emb = discord.Embed(title='Бой', description=f'**Вы не можете выйти из режима боя пока вы принимаете участие в захвате :x:**')
			await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Бой', description=f'**Вы вышли из режима боя**')
			await ctx.send(embed= emb)
			remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
			await ctx.author.remove_roles(remove_role)


#@Bot.command()
#async def snus(ctx,member:discord.Member):
#	g =  member.roles
#	if discord.Status.online:
#		print('Da')
#	print(member.status)
#	lsh = ''
#	lk = 0
#	a = []
#	for gk in g:
#		print(gk)
#	print(lsh)

promax = random_zarab()

fight1 = []
fight3 = []
@Bot.command()
async def attack(ctx,member:discord.Member,arg:str):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)  
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	promax = random.randint(1,3)
	attack_person = random.randint(1,9)
	if str(ctx.author.id) in fight3:
		emb = discord.Embed(title='Бой', description=f'**{ctx.author}** вы уже учавствовали в бою, подождите немного')
		await ctx.send(embed= emb)
	elif str(ctx.author.id) in fight1:
		emb = discord.Embed(title='Бой', description=f'**{ctx.author}** Вы устали, подождите несколько секунд')
		await ctx.send(embed= emb)
	else:
		try:
			gkk = member.roles
			ks = False
			for gk in gkk:
				if str(gk) == 'Режим боя':
					ks = True
				if ks == True:	
					pass
			gkk1 = ctx.author.roles
			ks1 = False
			for gk in gkk1:
				if str(gk) == 'Режим боя':
					ks1 = True
			if str(ctx.author.id) in fight1 and ks1 == False:
				exit()
			if ks == True and ks1 == True:
				role = discord.utils.get(member.guild.roles,id=813739982120026203)
				await member.add_roles(role)
				role = discord.utils.get(ctx.guild.roles,id=813739982120026203)
				await ctx.author.add_roles(role)
			else:
				emb = discord.Embed(title='Бой', description=f'У вас или вашего противника не включён режим боя')
				await ctx.send(embed= emb)
				exit()
			gkk = member.roles
			ks = False
			for gk in gkk:
				if str(gk) == 'В бою':
					ks = True
			if ks == True:	
				pass
			else:
				emb = discord.Embed(title='Бой', description=f' Игрок не на поле боя! :x: ')
				await ctx.send(embed= emb)
				exit()
			if str(member.id) == str(ctx.author.id):
				emb = discord.Embed(title='Бой', description=f'Вы не можете повредить себя :x: ')
				await ctx.send(embed= emb)
				exit()
			if "Лук" in inv[str(ctx.author.id)]["Use"]["Weapon"][0]: 
				if inv[str(ctx.author.id)]["Other"]["Strely"][1] <= 0:
					emb = discord.Embed(title='Бой', description=f'**У вас нет стрел!** :x: ')
					await ctx.send(embed= emb)
					exit()
				else:
					inv[str(ctx.author.id)]['Other']["Strely"][1] -= 1
			if arg == 'ноги':
				uvorot = promax + inv[str(member.id)]['Use']["Armor"][1] + inv[str(ctx.author.id)]['Use']["Weapon"][2] + users[str(member.id)]['lovk'] + inv[str(ctx.author.id)]['Leg'] * 2
			elif arg == 'руки':
				uvorot = promax + inv[str(member.id)]['Use']["Armor"][1] + inv[str(ctx.author.id)]['Use']["Weapon"][2] + users[str(member.id)]['lovk'] + inv[str(ctx.author.id)]['Arm'] * 2
			elif arg == 'торс':
				uvorot = promax + inv[str(member.id)]['Use']["Armor"][1] + inv[str(ctx.author.id)]['Use']["Weapon"][2] + users[str(member.id)]['lovk'] + inv[str(ctx.author.id)]['Tors'] 
			elif arg == 'голова':
				uvorot = promax + inv[str(member.id)]['Use']["Armor"][1] + inv[str(ctx.author.id)]['Use']["Weapon"][2] + users[str(member.id)]['lovk'] + inv[str(ctx.author.id)]['Hand'] * 2
			else:
				emb = discord.Embed(title='Бой', description=f'Неправильно введена часть тела :bone:')
				await ctx.send(embed= emb)
			if uvorot >=25:
				emb = discord.Embed(title='Бой', description=f'**{ctx.author}** промахнулся')
				await ctx.send(embed= emb)
				fight1.append(str(ctx.author.id))
			else:
				if arg == 'ноги':
					attack_pers = attack_person + users[str(ctx.author.id)]['sil'] + inv[str(ctx.author.id)]['Use']["Weapon"][1] - inv[str(member.id)]['Use']['Armor'][2] - inv[str(ctx.author.id)]['Leg'] + 20
					inv[str(ctx.author.id)]['Leg'] -= 2
					users[str(member.id)]['hp'] -= attack_pers
					emb = discord.Embed(title='Бой', description=f'**{ctx.author}** Нанёс **{member}** **{attack_pers}** :hearts: по ногам :leg: ')
					await ctx.send(embed= emb)
					fight1.append(str(ctx.author.id))
				elif arg == 'руки':
					attack_pers = attack_person + users[str(ctx.author.id)]['sil'] + inv[str(ctx.author.id)]['Use']["Weapon"][1] - inv[str(member.id)]['Use']['Armor'][2] - inv[str(ctx.author.id)]['Arm'] + 20
					inv[str(ctx.author.id)]['Arm'] -= 2
					users[str(member.id)]['hp'] -= attack_pers
					emb = discord.Embed(title='Бой', description=f'**{ctx.author}** Нанёс **{member}** **{attack_pers}** :hearts: по рукам :raised_hand:')
					await ctx.send(embed= emb)
					fight1.append(str(ctx.author.id))
				elif arg == 'торс':
					attack_pers = attack_person + users[str(ctx.author.id)]['sil'] + inv[str(ctx.author.id)]['Use']["Weapon"][1] - inv[str(member.id)]['Use']['Armor'][2] - inv[str(ctx.author.id)]['Tors'] + 20
					inv[str(ctx.author.id)]['Tors'] -= 1
					users[str(member.id)]['hp'] -= attack_pers
					emb = discord.Embed(title='Бой', description=f'**{ctx.author}** Нанёс **{member}** **{attack_pers}** :hearts: по торсу :shirt: ')
					await ctx.send(embed= emb)
					fight1.append(str(ctx.author.id))
				elif arg == 'голова':
					attack_pers = attack_person + users[str(ctx.author.id)]['sil'] + inv[str(ctx.author.id)]['Use']["Weapon"][1] - inv[str(member.id)]['Use']['Armor'][2] - inv[str(ctx.author.id)]['Hand'] + 20
					inv[str(ctx.author.id)]['Hand'] -= 1
					users[str(member.id)]['hp'] -= attack_pers
					emb = discord.Embed(title='Бой', description=f'**{ctx.author}** Нанёс **{member}** **{attack_pers}** :hearts: по голове :bust_in_silhouette:')
					await ctx.send(embed= emb)
					fight1.append(str(ctx.author.id))
		except:
			pass
		if users[str(member.id)]['hp'] <=0: 
			emb = discord.Embed(title='Бой', description=f'**{member}** Повержен! :skull_crossbones: ')
			await ctx.send(embed= emb)
			users[str(member.id)]['hp'] = 100
			users[str(ctx.author.id)]['hp'] = 100
			money[str(ctx.author.id)]['Money'] += 50
			inv[str(ctx.author.id)]['Leg'] = 4
			inv[str(ctx.author.id)]['Hand'] = 5
			inv[str(ctx.author.id)]['Tors'] = 7
			inv[str(ctx.author.id)]['Arm'] = 4
			users[str(ctx.author.id)]['rep'] += 5
			inv[str(member.id)]['Leg'] = 4
			inv[str(member.id)]['Hand'] = 5
			inv[str(member.id)]['Tors'] = 7
			inv[str(member.id)]['Arm'] = 4
			money[str(member.id)]['Money']  -= 50
			remove_role = discord.utils.get(ctx.guild.roles,id=813739982120026203)
			await ctx.author.remove_roles(remove_role)
			remove_role = discord.utils.get(member.guild.roles,id=813739982120026203)
			await member.remove_roles(remove_role)
			fight3.append(str(ctx.author.id))
			fight3.append(str(member.id))
			await asyncio.sleep(15*1)
			fight3.remove(str(ctx.author.id))
		with open('economy.json', 'w') as f:
			json.dump(money, f)
		with open('inventory.json', 'w') as f:
			json.dump(inv, f)
		with open('informat.json', 'w') as f:
			json.dump(users, f)
		await asyncio.sleep(15*1)
		fight1.remove(str(ctx.author.id))
		await asyncio.sleep(60*5)
		remove_role =	discord.utils.get(ctx.guild.roles,id=813739982120026203)
		await ctx.author.remove_roles(remove_role)
		remove_role = discord.utils.get(member.guild.roles,id=813739982120026203)
		await member.remove_roles(remove_role)
		
fight2 = []
@Bot.command()
async def use(ctx,*,arg:str): 
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	if arg =='Зелье здоровья':
		if inv[str(ctx.author.id)]['Potion']['Health potion'][1] >=1:
			users[str(ctx.author.id)]['hp']	+= 20
			inv[str(ctx.author.id)]['Potion']['Health potion'][1] -= 1
			emb = discord.Embed(title='Зелье', description=f'**{ctx.author}** использовал **{inv[str(ctx.author.id)]["Potion"]["Health potion"][0]}** :sake:')
			await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Зелье', description=f'**{ctx.author}** У вас нет зелий ')
			await ctx.send(embed= emb)
	elif arg == 'Мантия' or arg == 'Кожаная броня' or arg == 'Кольчуга' or arg == 'Латы' or arg == 'Зерцальный доспех' or arg == 'Кираса с тассетами' or arg == 'Льяная рубаха':
		ks = provrek_buy(arg)
		if ks[3]  in inv[str(ctx.author.id)]["Armor"]: 
			inv[str(ctx.author.id)]["Use"]["Armor"].clear()
			inv[str(ctx.author.id)]["Use"]["Armor"] = [arg,ks[2],ks[1]] 
			emb = discord.Embed(title='Предметы', description=f'Вы использовали предмет: {inv[str(ctx.author.id)]["Armor"][ks[3]][0]} :martial_arts_uniform: ')
			await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Предметы', description=f'**У вас нет этого предмета** :x:')
			await ctx.send(embed= emb)
	elif arg == "Стальной меч" or arg == 'Кинжал' or arg == 'Алебарда' or arg == 'Бёрдыш' or arg == 'Качественный палаш' or arg == 'Улучшенная рапира' or arg == 'Лук':
		ks = provrek_buy(arg)
		if ks[3]  in inv[str(ctx.author.id)]["Weapon"]: 
			inv[str(ctx.author.id)]["Use"]["Weapon"].clear()
			inv[str(ctx.author.id)]["Use"]["Weapon"] = [arg,ks[1],ks[2]]	 
			emb = discord.Embed(title='Предметы', description=f'Вы использовали предмет: {inv[str(ctx.author.id)]["Weapon"][ks[3]][0]} :crossed_swords: ')
			await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Предметы', description=f'**У вас нет этого предмета** :x:')
			await ctx.send(embed= emb)	
	elif arg == "Зелье Силы":
		if inv[str(ctx.author.id)]['Potion']['Attack potion'][1] >=1:
			fight2.append(str(ctx.author.id))
			us = users[str(ctx.author.id)]['sil']
			us1 = users[str(ctx.author.id)]['lovk']
			users[str(ctx.author.id)]['sil'] += 5
			users[str(ctx.author.id)]['lovk'] += 4
			inv[str(ctx.author.id)]['Potion']['Attack potion'][1] -= 1
			emb = discord.Embed(title='Зелье', description=f'**{ctx.author}** использовал **{inv[str(ctx.author.id)]["Potion"]["Attack potion"][0]}** :sake:')
			await ctx.send(embed= emb)
			await asyncio.sleep(60*1)
			fight2.remove(str(ctx.author.id))
			await asyncio.sleep(60*5)
			users[str(ctx.author.id)]['sil'] = us
			users[str(ctx.author.id)]['lovk'] = us1
		else:
			emb = discord.Embed(title='Зелье', description=f'**{ctx.author}** **У вас нет зелий!** :x: ')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Зелье', description=f'**Неизвестный предмет!** :x:')
		await ctx.send(embed= emb)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)


@Bot.command()
async def inventory(ctx):	
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)
	armor = ''
	kt = 0
	for value in inv[str(ctx.author.id)]['Armor'].values():
		armor += value[0]
		kt += 1
		ga = len(inv[str(ctx.author.id)]['Armor'].values())
		if ga == kt:
			armor += '.'
		else: armor += ', '
	weapon = ''
	sh = 0
	for value in inv[str(ctx.author.id)]['Weapon'].values():
		weapon += value[0]
		sh += 1
		gg = len(inv[str(ctx.author.id)]['Weapon'].values())
		if gg == sh:
			weapon += '.'
		else: weapon += ', '
	other = '' 
	kl = 0
	for value in inv[str(ctx.author.id)]['Other'].values():
		other += value[0]
		kl += 1
		if value[0] == 'Стрелы':
			other += ' = ' + str(inv[str(ctx.author.id)]['Other']["Strely"][1])

		go = len(inv[str(ctx.author.id)]['Other'].values())
		if go == kl:
			other += '.'
		else: other += ', '
	emb = discord.Embed(description=f'Инвентарь:')
	emb.add_field(name = ':school_satchel: ', value = '{}'.format(ctx.author), inline = False)
	emb.add_field(name = 'Зелья:', value = f'{inv[str(ctx.author.id)]["Potion"]["Health potion"][0]} = {inv[str(ctx.author.id)]["Potion"]["Health potion"][1]} :wine_glass: , {inv[str(ctx.author.id)]["Potion"]["Attack potion"][0]} = {inv[str(ctx.author.id)]["Potion"]["Attack potion"][1]} :tumbler_glass: ', inline = False)
	emb.add_field(name = 'Оружие:', value = f'{weapon} :crossed_swords:', inline = False) 
	emb.add_field(name = 'Броня:', value = f'{armor} :martial_arts_uniform:', inline = False)
	emb.add_field(name = 'Кристалы:', value = f'{money[str(ctx.author.id)]["Money"]} :diamonds:', inline = False)
	emb.add_field(name = 'Остальное:', value = f'{other} :tools:', inline = False)
	await ctx.send(embed = emb)


	with open('economy.json', 'w') as f:
		json.dump(money, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)

@Bot.command()
async def shop(ctx,arg:str):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)
	if olo == True:
		if arg == 'оружие':
			emb = discord.Embed(description=f'Оружие:')
			emb.add_field(name = ':crossed_swords:', value = f'🛒', inline = False)
			emb.add_field(name = 'Стальной меч:', value = f'Цена: 100, урон: 5', inline = False)
			emb.add_field(name = 'Кинжал:', value = f'Цена: 75, урон: 2', inline = False) 
			emb.add_field(name = 'Алебарда:', value = f'Цена: 350, урон: 7', inline = False)
			emb.add_field(name = 'Бёрдыш:', value = f'Цена:500 , урон: 10', inline = False)
			emb.add_field(name = 'Качественный палаш:', value = f'Цена: 1000, урон: 12', inline = False)
			emb.add_field(name = 'Улучшенная рапира:', value = f'Цена: 1200, урон: 15', inline = False)
			emb.add_field(name = 'Лук:', value = f'Цена: 800, урон: 7', inline = False)
			await ctx.send(embed = emb)
		elif arg == 'одежда':
			emb = discord.Embed(description=f'Одежда:')
			emb.add_field(name = ':martial_arts_uniform:', value = f'🛒', inline = False)
			emb.add_field(name = 'Мантия:', value = f'Цена: 80, защита: 3', inline = False)
			emb.add_field(name = 'Кожаная броня:', value = f'Цена: 110, защита: 4', inline = False)
			emb.add_field(name = 'Кольчуга:', value = f'Цена: 140, защита: 5', inline = False) 
			emb.add_field(name = 'Латы:', value = f'Цена: 600, защита: 10', inline = False)
			emb.add_field(name = 'Зерцальный доспех:', value = f'Цена: 1500, защита: 21', inline = False)
			emb.add_field(name = 'Кираса с тассетами:', value = f'Цена: 800, защита: 15', inline = False)
			await ctx.send(embed = emb)
		elif arg == 'остальное':
			emb = discord.Embed(description=f'Остальное:')
			emb.add_field(name = ':tools:', value = f'🛒', inline = False)
			emb.add_field(name = 'Зелье здоровья', value = f'Цена: 25, востанавливает: 20 hp', inline = False)
			emb.add_field(name = 'Зелье Силы:', value = f'Цена: 60, увеличивает силу и ловкость', inline = False) 
			emb.add_field(name = 'Кирка:', value = f'Цена: 50, с помощью неё можно добывать руду', inline = False)
			emb.add_field(name = 'Очень прочная кирка:', value = f'Цена: 100, прочней обычной кирки', inline = False)
			emb.add_field(name = 'Стрелы:', value = f'Цена:30, 15 штук.', inline = False)
			await ctx.send(embed = emb)
		else:
			emb = discord.Embed(title='Магазин', description=f'Неверная категория')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Магазин', description=f'Вы не в городе! :x:')
		await ctx.send(embed= emb)
	with open('economy.json', 'w') as f:
		json.dump(money, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)

@Bot.command()
async def buy(ctx,*,arg1:str):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)
	if olo == True:
		if arg1 == "Стальной меч" or arg1 == 'Кинжал' or arg1 == 'Алебарда' or arg1 == 'Бёрдыш' or arg1 == 'Качественный палаш' or arg1 == 'Улучшенная рапира' or arg1 == 'Лук':
			ks = provrek_buy(arg1)
			if money[str(ctx.author.id)]['Money'] >= ks[0]: 
				if ks[3] not in inv[str(ctx.author.id)]['Weapon']:
					money[str(ctx.author.id)]['Money'] -= ks[0]
					inv[str(ctx.author.id)]['Weapon'][ks[3]] = [arg1,ks[1],ks[2]]
					emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Weapon"][ks[3]][0]} :crossed_swords: ')
					await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Покупка:', description=f'У вас уже есть {inv[str(ctx.author.id)]["Weapon"][ks[3]][0]}  :x: ')
					await ctx.send(embed= emb)
			else:
				stou = ks[0] - money[str(ctx.author.id)]["Money"]
				emb = discord.Embed(title='Покупка:', description=f'Вам не хватает {stou} :diamonds:')
				await ctx.send(embed= emb)
		elif arg1 == 'Мантия' or arg1 == 'Кожаная броня' or arg1 == 'Кольчуга' or arg1 == 'Латы' or arg1 == 'Зерцальный доспех' or arg1 == 'Кираса с тассетами':
			ks = provrek_buy(arg1)
			if money[str(ctx.author.id)]['Money'] >= ks[0]: 
				if ks[3] not in inv[str(ctx.author.id)]['Armor']:
					money[str(ctx.author.id)]['Money'] -= ks[0]
					inv[str(ctx.author.id)]['Armor'][ks[3]] = [arg1,ks[2],ks[1]]
					emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Armor"][ks[3]][0]} :martial_arts_uniform: ')
					await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Покупка:', description=f'У вас уже есть {inv[str(ctx.author.id)]["Armor"][ks[3]][0]}  :x: ')
					await ctx.send(embed= emb)
			else:
				stou = ks[0] - money[str(ctx.author.id)]["Money"]
				emb = discord.Embed(title='Покупка:', description=f'Вам не хватает {stou} :diamonds:')	
		elif arg1 == "Зелье здоровья" or arg1 == "Зелье Силы":
			ks = provrek_buy(arg1)
			if money[str(ctx.author.id)]['Money'] >= ks[0]: 
				money[str(ctx.author.id)]['Money'] -= ks[0]
				inv[str(ctx.author.id)]['Potion'][ks[1]][1] += 1
				emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Potion"][ks[1]][0]} :sake: ')
				await ctx.send(embed= emb)
			else:
				stou = ks[0] - money[str(ctx.author.id)]["Money"]
				emb = discord.Embed(title='Покупка:', description=f'Вам не хватает {stou} :diamonds:')
		elif arg1 == 'Кирка' or arg1 == 'Очень прочная кирка' or arg1 == 'Стрелы':
			if arg1 == 'Стрелы':
				ks = provrek_buy(arg1)
				if money[str(ctx.author.id)]['Money'] >= ks[0]:  
					money[str(ctx.author.id)]['Money'] -= ks[0] 
					if ks[2] not in inv[str(ctx.author.id)]['Other']:
						inv[str(ctx.author.id)]['Other'][ks[2]] = [arg1,15]
						emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Other"][ks[2]][0]} :bow_and_arrow: ')
						await ctx.send(embed= emb)
					else:
						inv[str(ctx.author.id)]['Other'][ks[2]][1] += 15
						emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Other"][ks[2]][0]} :bow_and_arrow: ')
						await ctx.send(embed= emb)
				else:
					stou = ks[0] - money[str(ctx.author.id)]["Money"]
					emb = discord.Embed(title='Покупка:', description=f'Вам не хватает {stou} :diamonds:')
			elif arg1 == 'Кирка' or arg1 == 'Очень прочная кирка':
				ks = provrek_buy(arg1)
				if money[str(ctx.author.id)]['Money'] >= ks[0]:  
					money[str(ctx.author.id)]['Money'] -= ks[0] 
					if ks[2] not in inv[str(ctx.author.id)]['Other']:
						inv[str(ctx.author.id)]['Other'][ks[2]] = [arg1,ks[1]]
						emb = discord.Embed(title='Покупка:', description=f'Вы приобрели предмет: {inv[str(ctx.author.id)]["Other"][ks[2]][0]} :hammer_pick: ')
						await ctx.send(embed= emb)
					else:
						emb = discord.Embed(title='Покупка:', description=f'У вас уже есть {inv[str(ctx.author.id)]["Other"][ks[2]][0]}  :x: ')
						await ctx.send(embed= emb)	
				else:
					stou = ks[0] - money[str(ctx.author.id)]["Money"]
					emb = discord.Embed(title='Покупка:', description=f'Вам не хватает {stou} :diamonds:')
		else:
			emb = discord.Embed(title='Магазин', description=f'Неверный товар')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Магазин', description=f'Вы не в городе! :x:')
		await ctx.send(embed= emb)

	with open('economy.json', 'w') as f:
		json.dump(money, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)

@Bot.command()
async def sell(ctx,arg1:str):
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	with open('economy.json', 'r') as f:
		money = json.load(f)
	if olo == True:
		if arg1 == "Стальной меч" or arg1 == 'Кинжал' or arg1 == 'Алебарда' or arg1 == 'Бёрдыш' or arg1 == 'Качественный палаш' or arg1 == 'Улучшенная рапира' or arg1 == 'Лук':
			ks = provrek_buy(arg1)
			if ks[3]  in inv[str(ctx.author.id)]['Weapon']:
				del inv[str(ctx.author.id)]['Weapon'][ks[3]]
				money[str(ctx.author.id)]['Money'] += ks[0]
				emb = discord.Embed(title='Продажа:', description=f'Вы успешно продали предмет! :white_check_mark: ')
				await ctx.send(embed= emb)
				if ks[3] in inv[str(ctx.author.id)]['Use']['Weapon']:
					del inv[str(ctx.author.id)]['Use']['Weapon'][ks[3]]
			else:
				emb = discord.Embed(title='Продажа:', description=f'У вас нет этого предмета! :x: ')
				await ctx.send(embed= emb)

		elif arg1 == 'Мантия' or arg1 == 'Кожаная броня' or arg1 == 'Кольчуга' or arg1 == 'Латы' or arg1 == 'Зерцальный доспех' or arg1 == 'Кираса с тассетами':
			ks = provrek_buy(arg1)
			if ks[3]  in inv[str(ctx.author.id)]["Armor"]:
				del inv[str(ctx.author.id)]['Armor'][ks[3]]
				money[str(ctx.author.id)]['Money'] += ks[0]
				emb = discord.Embed(title='Продажа:', description=f'Вы успешно продали предмет! :white_check_mark:  ')
				await ctx.send(embed= emb)
				if ks[3] in inv[str(ctx.author.id)]['Use']['Armor']:
					print(inv[str(ctx.author.id)]['Use']['Armor'])
					del inv[str(ctx.author.id)]['Use']['Armor'][ks[3]]
					inv[str(ctx.author.id)]['Use']['Armor']['Lien'] = ['Льяная рубаха',0,1]
			else:
				emb = discord.Embed(title='Продажа:', description=f'У вас нет этого предмета! :x: ')
				await ctx.send(embed= emb)
		elif arg1 == "Зелье здоровья" or arg1 == "Зелье Силы":
			ks = provrek_buy(arg1)
			if inv[str(ctx.author.id)]['Potion'][ks[1]][1] > 0:
				inv[str(ctx.author.id)]['Potion'][ks[1]][1] -= 1
				money[str(ctx.author.id)]['Money'] += ks[0]
				emb = discord.Embed(title='Покупка:', description=f'Вы успешно продали предмет! :white_check_mark: ')
				await ctx.send(embed= emb)
			else:
				emb = discord.Embed(title='Продажа:', description=f'У вас нет этого предмета! :x: ')
				await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Магазин', description=f'Неверный предмет')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Магазин', description=f'Вы не в городе! :x:')
		await ctx.send(embed= emb)
	with open('economy.json', 'w') as f:
		json.dump(money, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)

@Bot.command()
async def stats(ctx):
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	if don == True:
		emb = discord.Embed(title='Монумент', description=f'На данный момент для строительства монумента есть {stat["Stat"]}/50000 :jigsaw:')
		await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Монумент', description=f'Вы находитесь не у монумента :x:')
		await ctx.send(embed= emb)
	with open('stat.json', 'w') as f:
		json.dump(stat, f)


@Bot.command()
async def donate(ctx,arg):
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	with open('informat.json', 'r') as f:
		users = json.load(f)
	if don == True:
		if users[str(ctx.author.id)]['ore_mine'] >= int(arg):
			if int(arg) > 0:
				users[str(ctx.author.id)]['ore_mine'] -= int(arg)
				users[str(ctx.author.id)]['rep'] += 1 * int(arg)
				stat["Stat"] += int(arg)
				emb = discord.Embed(title='Монумент', description=f'Вы пожертвовали {arg} руды :jigsaw:')
				await ctx.send(embed= emb)
			else:
				emb = discord.Embed(title='Монумент', description=f'Вы не можете пожертвовать {arg} :x:')
				await ctx.send(embed= emb)
		else:
			emb = discord.Embed(title='Монумент', description=f'У вас нет столько руды! :x:')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Монумент', description=f'Вы находитесь не у монумента :x:')
		await ctx.send(embed= emb)
	with open('stat.json', 'w') as f:
		json.dump(stat, f)
	with open('informat.json', 'w') as f:
		json.dump(users, f)

@Bot.event
async def on_command_error(ctx,error):
	pass


@Bot.command()
@commands.has_any_role('Модератор', 'Администратор', 'Старший Администратор', 'Куратор', 'Основатель')
async def clear(ctx,arg):
	try:
		delet = await ctx.message.channel.purge(limit=int(arg)+1)
	except:
		pass

@Bot.command()
@commands.has_any_role('Модератор', 'Администратор', 'Старший Администратор', 'Куратор', 'Основатель')
async def mute(ctx,member:discord.Member,time:int,reason):
	g =  member.roles
	man = False
	vam = False
	for gk in g:
		if str(gk) == "Human":
			man = True
		if str(gk) == "Vampire": 
			vam = True
	if man == True:
		remove_role = discord.utils.get(member.guild.roles,id=809287150116798466)
		await member.remove_roles(remove_role)
	if vam == True:
		remove_role = discord.utils.get(member.guild.roles,id=809287144899215382)
		await member.remove_roles(remove_role)
	role = discord.utils.get(member.guild.roles,id=852480932065968128)
	await member.add_roles(role)
	channel = Bot.get_channel(852481835698094110)
	emb = discord.Embed(title="Мут",color=0x2f3136)
	emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
	emb.add_field(name='Нарушитель',value=member.mention,inline=False)
	emb.add_field(name='Причина',value=reason,inline=False)
	emb.add_field(name="Время",value=time,inline=False)
	await channel.send(embed = emb)
	await asyncio.sleep(time*60 )
	emb = discord.Embed(title="Размут",color=0x2f3136)
	emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
	emb.add_field(name='Нарушитель',value=member.mention,inline=False)
	emb.add_field(name='Причина',value="Время мута вышло",inline=False)
	await channel.send(embed=emb)
	if man == True:
		role = discord.utils.get(member.guild.roles,id=809287150116798466)
		await member.add_roles(role)
	if vam == True:
		role = discord.utils.get(member.guild.roles,id=809287144899215382)
		await member.add_roles(role)
	remove_role = discord.utils.get(member.guild.roles,id=852480932065968128)
	await member.remove_roles(remove_role)
	
@Bot.command()
@commands.has_any_role('Модератор', 'Администратор', 'Старший Администратор', 'Куратор', 'Основатель')
async def unmute(ctx,member:discord.Member):
	channel = Bot.get_channel(852481835698094110)
	g =  member.roles
	man = False
	vam = False
	for gk in g:
		if str(gk) == "Human":
			man = True
		if str(gk) == "Vampire": 
			vam = True
	if man == True:
		role = discord.utils.get(member.guild.roles,id=809287150116798466)
		await member.add_roles(role)
	if vam == True:
		role = discord.utils.get(member.guild.roles,id=809287144899215382)
		await member.add_roles(role)
	muterole = discord.utils.get(ctx.guild.roles,id=ВашАйди)
	emb = discord.Embed(title="Размут",color=0xff0000)
	emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
	emb.add_field(name='Нарушитель',value=member.mention,inline=False)
	await channel.send(embed = emb)
	remove_role = discord.utils.get(member.guild.roles,id=852480932065968128)
	await member.remove_roles(remove_role)



@Bot.event
async def on_command_error(ctx, error):
	if isinstance(error,commands.MissingRequiredArgument):
		pass
	elif isinstance(error,commands.MissingPermissions):
		pass
	elif isinstance(error,commands.CommandNotFound ):
		pass


def provhhh():
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	stat["Per"] = 1
	with open('stat.json', 'w') as  f: 
		json.dump(stat, f)

def provhhhz():
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	stat["Per"] = 0
	with open('stat.json', 'w') as  f: 
		json.dump(stat, f)

def provhhhz1():
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	stat["Vt"] = 1
	with open('stat.json', 'w') as  f: 
		json.dump(stat, f)

def provhhhz2():
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	stat["Vt"] = 0
	with open('stat.json', 'w') as  f: 
		json.dump(stat, f)



warzaxvat = 0
capturyy = []
cd1 = []
add_p = 0
@Bot.command()
async def capture(ctx):
	with open('stat.json', 'r') as f:
		stat = json.load(f)
	with open('informat.json', 'r') as f:
		users = json.load(f)
	with open('inventory.json', 'r') as f:
		inv = json.load(f)
	global warzaxvat 
	global add_p
	cat = 0
	gkk1 = ctx.author.roles
	man = False
	vam = False
	for gk in gkk1:
		if str(gk) == "Human":
			man = True
		if str(gk) == "Vampire": 
			vam = True
	if captr1 == True: #!
		if man == True:
			if stat["Per"] == 1:
				emb = discord.Embed(title='Захват', description=f'Эта зона под вашим контролем! :x: ')
				await ctx.send(embed= emb)
			else: 
				if '1' not in capturyy:
					if '1' not in cd1:
						cd1.append('1')
						capturyy.append('1')
						warzaxvat = 1
						role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
						await ctx.author.add_roles(role)
						role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
						await ctx.author.add_roles(role)
						emb = discord.Embed(title='Захват', description=f'Начался захват! :white_check_mark:')
						await ctx.send(embed= emb)
						add_p = 1
						await asyncio.sleep(60*5) #изменить не забудь!!!!
						role1 = ctx.guild.get_role(829377070223196201)
						colv = len(role1.members)
						if colv == 0:
							emb = discord.Embed(title='Захват', description=f'Попытка захвата провалилась! :x: ')
							await ctx.send(embed= emb)
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
						else:
							emb = discord.Embed(title='Захват', description=f'Вы захватили эту зону :white_check_mark:')
							await ctx.send(embed= emb)	
							provhhh()
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
					else:
						emb = discord.Embed(title='Захват', description=f'Ещё не вышло время до следующего захвата! :x: ')
						await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Захват', description=f'Уже идёт захват! :x: ')
					await ctx.send(embed= emb)
		if vam == True:
			if stat["Per"] == 0:
				emb = discord.Embed(title='Захват', description=f'Эта зона под вашим контролем! :x: ')
				await ctx.send(embed= emb)
			else:
				if '1' not in capturyy:
					if '1' not in cd1:
						cd1.append('1')
						capturyy.append('1')
						warzaxvat = 1
						role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
						await ctx.author.add_roles(role)
						role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
						await ctx.author.add_roles(role)
						emb = discord.Embed(title='Захват', description=f'Начался захват! :white_check_mark:')
						await ctx.send(embed= emb)
						add_p = 2
						await asyncio.sleep(60*5) #изменить не забудь!!!!
						role1 = ctx.guild.get_role(829377070223196201)
						colv = len(role1.members)
						if colv == 0:
							emb = discord.Embed(title='Захват', description=f'Попытка захвата провалилась! :x: ')
							await ctx.send(embed= emb)
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
						else:
							emb = discord.Embed(title='Захват', description=f'Вы захватили эту зону :white_check_mark:')
							await ctx.send(embed= emb)	
							provhhhz()
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
					else:
						emb = discord.Embed(title='Захват', description=f'Ещё не вышло время до следующего захвата! :x: ')
						await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Захват', description=f'Уже идёт захват! :x: ')
					await ctx.send(embed= emb)
	elif captr2 == True:
		if man == True:
			if stat["Vt"] == 1:
				emb = discord.Embed(title='Захват', description=f'Эта зона под вашим контролем! :x: ')
				await ctx.send(embed= emb)
			else:
				if '1' not in capturyy:
					if '1' not in cd1:
						cd1.append('1')
						capturyy.append('1')
						warzaxvat = 1
						role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
						await ctx.author.add_roles(role)
						role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
						await ctx.author.add_roles(role)
						emb = discord.Embed(title='Захват', description=f'Начался захват! :white_check_mark:')
						await ctx.send(embed= emb)
						add_p = 1
						await asyncio.sleep(60*5) #изменить не забудь!!!!
						role1 = ctx.guild.get_role(829377070223196201)
						colv = len(role1.members)
						if colv == 0:
							emb = discord.Embed(title='Захват', description=f'Попытка захвата провалилась! :x: ')
							await ctx.send(embed= emb)
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
						else:
							emb = discord.Embed(title='Захват', description=f'Вы захватили эту зону :white_check_mark:')
							await ctx.send(embed= emb)	
							provhhhz1()
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')

					else:
						emb = discord.Embed(title='Захват', description=f'Ещё не вышло время до следующего захвата! :x: ')
						await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Захват', description=f'Уже идёт захват! :x: ')
					await ctx.send(embed= emb)
		if vam == True:
			if stat["Vt"] == 0:
				emb = discord.Embed(title='Захват', description=f'Эта зона под вашим контролем! :x: ')
				await ctx.send(embed= emb)
			else:
				if '1' not in capturyy:
					if '1' not in cd1:
						cd1.append('1')
						capturyy.append('1')
						warzaxvat = 1
						role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
						await ctx.author.add_roles(role)
						role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
						await ctx.author.add_roles(role)
						emb = discord.Embed(title='Захват', description=f'Начался захват! :white_check_mark:')
						await ctx.send(embed= emb)
						add_p = 2
						await asyncio.sleep(60*5) #изменить не забудь!!!!
						role1 = ctx.guild.get_role(829377070223196201)
						colv = len(role1.members)
						if colv == 0:
							emb = discord.Embed(title='Захват', description=f'Попытка захвата провалилась! :x: ')
							await ctx.send(embed= emb)
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
						else:
							emb = discord.Embed(title='Захват', description=f'Вы захватили эту зону :white_check_mark:')
							await ctx.send(embed= emb)	
							provhhhz2()
							remove_role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
							await ctx.author.remove_roles(remove_role)
							remove_role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
							await ctx.author.remove_roles(remove_role)
							capturyy.remove('1')
							await asyncio.sleep(15)
							warzaxvat = 0
							add_p = 0
							await asyncio.sleep(60*30-15) #изменить не забудь!!!!
							cd1.remove('1')
					else:
						emb = discord.Embed(title='Захват', description=f'Ещё не вышло время до следующего захвата! :x: ')
						await ctx.send(embed= emb)
				else:
					emb = discord.Embed(title='Захват', description=f'Уже идёт захват! :x: ')
					await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Захват', description=f'Вы не можете захватить эту зону! :x: ')
		await ctx.send(embed= emb)
	with open('informat.json', 'w') as f:
		json.dump(users, f)
	with open('inventory.json', 'w') as f:
		json.dump(inv, f)
	with open('stat.json', 'w') as f:
		json.dump(stat, f)





@Bot.command()
async def add(ctx): 
	if warzaxvat == 1:
		gkk1 = ctx.author.roles
		man = False
		vam = False
		for gk in gkk1:
			if str(gk) == "Human":
				man = True
			if str(gk) == "Vampire": 
				vam = True
		if vam == True and add_p == 2:
			emb = discord.Embed(title='Захват', description=f'**{ctx.author}** присоеденился к захвату точки! :white_check_mark: ')
			await ctx.send(embed= emb)
			role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
			await ctx.author.add_roles(role)
			role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
			await ctx.author.add_roles(role)
		elif man == True and add_p == 1:
			emb = discord.Embed(title='Захват', description=f'**{ctx.author}** присоеденился к захвату точки! :white_check_mark: ')
			await ctx.send(embed= emb)
			role = discord.utils.get(ctx.guild.roles,id=829377070223196201)
			await ctx.author.add_roles(role)
			role = discord.utils.get(ctx.guild.roles,id=844544206235238420)
			await ctx.author.add_roles(role)
		else:
			emb = discord.Embed(title='Захват', description=f'Ваша фракция не захватывает точку! :x ')
			await ctx.send(embed= emb)
	else:
		emb = discord.Embed(title='Захват', description=f'Cейчас не идёт захват территории! :x: ')
		await ctx.send(embed= emb)


#@Bot.event
#async def on_message(message):
#	global warzaxvat 
#	print(warzaxvat)
#	print('Mihey')
#	if warzaxvat == 1:
#		for member in message.guild.members:
#			for kk in member.roles:
#				if str(kk) == "Захват":
#					ks1 = True
#				else:
#					ks1 = False
#			if ks1 == True:
#				if warzaxvat != 1:
#					remove_role = discord.utils.get(member.guild.roles,id=829377070223196201)
#					await member.remove_roles(remove_role)
#			if warzaxvat == 1:
#				t = member.status
#				if t != discord.Status.online:
#					remove_role = discord.utils.get(member.guild.roles,id=829377070223196201)
#					await member.remove_roles(remove_role)
#	await Bot.process_commands(message)	

Bot.run('Nzg1NzQ3OTUzOTYwMjIyNzMz.X88Wzg.xu3V71i1riWtxXm_U4y7edyXyU8') 
