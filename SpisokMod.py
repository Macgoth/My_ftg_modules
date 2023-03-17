from .. import loader, utils
import asyncio
from telethon.tl.types import MessageEntityTextUrl
import json as JSON

class SpisokMod(loader.Module):
	"Делает юзернеймы из списков ириса"
	strings={"name": "SpisokMod"}
	
	async def spisokcmd(self, message):
		".spisok [arg] [arg] [arg]....\nВ качестве аргументов используй числа. или первые символы строки."
		reply = await message.get_reply_message()
		a = reply.text
		sms = ''
		count_st = 0
		count_hf = 0
		if not reply:
			await message.edit('Нет реплая.')
			return
		args = utils.get_args_raw(message)
		list_args=[]
		if not args:
			await message.edit('Нет аргументов')
			return
		await message.delete()
		for i in args.split(' '):
			if '-' in i:
				ot_do = i.split('-')
				try:
					for x in range(int(ot_do[0]),int(ot_do[1])+1):
						list_args.append(str(x))
				except:
					await message.respond('Используй правильно функцию "от-до"')
					return
			else:
				list_args.append(i)
		lis = []
		for i in a.splitlines():
			lis.append(i)
		for start in list_args:
			for x in lis:
				if x.lower().startswith(str(start.lower())):
					count_st = 1
					if 'href="' in x:
						count_hf = 1
						b=x.find('href="')+6
						c=x.find('">')
						link = x[b:c]
						if link.startswith('tg'):
							list = []
							for i in link.split('='):
								list.append(i)
							sms+=f'@{list[1]}\n'
							break
						elif link.startswith('https://t.me'):
							a ='@' + str(link.split('/')[3])
							sms+=f'{a}\n'
							break
						else:
							sms+='что за хуета?'
							break
#			await asyncio.sleep(3)
		await message.respond(sms)
				
		if not count_st:
			await message.edit('Не найдено ни одного совпадения в начале строк с аргументами.')
			
		elif not count_hf:
			await message.edit('Не найдено ни одной ссылки.')
			
		elif len(list_args) >= 3:
			await message.respond('<b>Извлечения юзеров успешно завершены.</b>')
