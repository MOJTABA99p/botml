from rubika_lib.lib import Bot
from json import load, dump
from requests import get

def hasAds(msg):
	links = ["join","rubika.ir/post","@","joinc"]
	for i in links:
		if i in msg.lower():
			return True
def hasInsult(msg):
	try:
		punctuations = '''۱۲۳۴۵۶ ۷۸۹۰+×÷=/_€£¥﷼!@#$٪^&*()-'":؛،؟`~|<>{}[]°•○●□■♤♡◇♧☆☆ـ¤《》¡¿1234567890qqw⇧⇩⇨⚤︎シ︎ertyuiopasdfghjklzxccvbbnmm.'''
		no_punct = ""
		for char in msg:
			if char not in punctuations:
				no_punct = no_punct + char
		swData = [False,None]
		msg = no_punct
		for i in open("dontReadMe.txt").read().split("\n"):
			if i in msg:
				swData = [True, i]
				break
			else: continue
		return swData
	except: pass

auth = Bot("dinqrknnrzodjjuagoyailyeybhdchit")
guid = "g0B1HKt0342e19945a09836c396b4fd7"
answered , sleeped = [] , False

while True:
	try:
		admins = [i["member_guid"] for i in auth.reciveGroupAdmins(guid)["data"]["in_chat_members"]]
		try:
			with open("yadgiri.json","r",encoding="utf-8") as learn:
				data = load(learn)
		except: pass
		min_id = auth.reciveGroupInfo(guid)["data"]["chat"]["last_message_id"]
		messages = auth.reciveMessages(guid,min_id)

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins:
						try:
							auth.clearMessages(guid, [msg.get("message_id")])
						except:
							try:
								auth.clearMessages(guid, [msg.get("message_id")])
							except: pass

					elif hasInsult(msg.get("text"))[0]:
						try:
							auth.clearMessages(guid, [msg.get("message_id")])
						except:
							try:
								auth.clearMessages(guid, [msg.get("message_id")])
							except: pass
		
					elif "forwarded_from" in msg.keys() and auth.reciveMessagesInfo(guid, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						try:
							auth.clearMessages(guid, [str(msg.get("message_id"))])
						except:
							print('err delete forwared')
					

					for i in data.keys():
						if i == msg.get("text"):
							try:
								auth.sendMessage(guid, str(data[i]), message_id=msg.get("message_id"))
							except: pass

					answered.append(msg.get("message_id"))

	except: pass