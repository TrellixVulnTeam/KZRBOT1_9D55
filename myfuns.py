
""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import ALIVE_NAME
from userbot import CMD_HELP
from userbot.utils import admin_cmd

# ================= CONSTANT =================
NOOBSTR = [
    "`പെമ്പിള്ളേരെ റോട്ടിക്കൂടെ നടക്കാൻ നീ സമ്മതിക്കില്ല , അല്ലേ.......ഡാ, നീയാണീ അലവലാതി ഷാജി അല്ലേ ?`",
    "`വർക്കിച്ചാ യെവൻ പുലിയാണ് കേട്ടാ പുലിയെന്ന് പറഞ്ഞാ വെറും പുലിയല്ല … ഒരു സിംഹം...😜😜 `",
    "`മാമ്മനും അനന്തരവനും കൂടി പണ്ട് ഈഴിര തോർത്തു വെച്ച് പരൽ മീനുകളെ പിടിച്ചു കളിച്ചിട്ടുണ്ടാകും ... പക്ഷെ ആ ഈഴിര വിരിച്ചാൽ സ്രാവിനെ കിട്ടുമെന്നു കരുതരുത് .. ഇത് കാർത്തികേയനാ ...😎😎😎 `",
    "`കഴിഞ്ഞ ഓണത്തിന് കൈപ്പുഴ കുഞ്ഞപ്പന്റെ കയ്യറുത്തപ്പോൾ കട്ടച്ചോരയാ മുഖത്തു തെറിച്ചത് അത്രക്കും വരില്ലല്ലോ ഒരു പീറ ആട്...🤭🤭🤭😜`",
    "`കളി ഹൈറേഞ്ചിലാണെങ്കിലും അങ്ങ് പാരീസിൽ ചെന്ന് ചോദിച്ചാലറിയാം ഈ സാത്താനെ...😎😎😡 `",
    "`എന്റെ ഹൈറേഞ്ചിൽ വന്നിട്ട് എന്റെ പിള്ളേരെ പേടിപ്പിക്കുന്നോടാ നാറികളേ...😡😡😜`",
    "`എവിടെയാടാ നീ അടിച്ചോണ്ട് പോയ എന്റെ നീലക്കുയിൽ 😡😡😜..`",
    "`കൃഷ്ണവിലാസം ഭഗീരഥൻ പിള്ള.. വലിയ വെടി നാല്.. ചെറിയ വെടി നാല്...😜😜🤭`", 
    "`ഇര തേടി വരുന്ന പുലി കെണി തേടി വരില്ല..... പുലിയെ അതിന്റെ മടയിൽ ചെന്ന് വേട്ടയാടി കൊല്ലണം.... അതാണ് കാട്ടിലെ നിയമം...😎😎😇`", 
    "`നീ പോ മോനെ ദിനേശാ...`", "`മരിപ്പിനുള്ള പരിപ്പുവടേം ചായേം ഞാൻ തരുന്നുണ്ട് ഇപ്പോഴല്ല പിന്നെ`", 
    "`സാർ മഹാരാജാസ് കോളേജിൽ പഴേ k.s.u കാരനായിരുന്നല്ലേ അവിടുത്തെ s. F. I പിള്ളേർടെ ഇടി അവസാനത്തേതാണെന്ന് കരുതരുത്...`",
    "`നീയൊക്കെ അര ട്രൗസറും ഇട്ടോണ്ട് അജന്തയിൽ ആദിപാപം കണ്ടോണ്ട് നടക്കണ ടൈമിൽ നമ്മളീ സീൻ വിട്ടതാ നിന്റെയൊക്കെ ഇക്കാനോട് ചോദിച്ചാൽ അറിയാം പോയി ചോദിക്ക് 😎😎😈 `", 
    "`വെല്ലുവിളികൾ ആവാം പക്ഷെ അത് നിന്നെക്കാൾ നാലഞ്ചോണം കൂടുതൽ ഉണ്ടവരോടാവരുത് `", "`ഇവിടെ കിടന്ന് എങ്ങാനും show ഇറക്കാൻ ആണ് പ്ലാൻ എങ്കിൽ പിടിച്ചു തെങ്ങിന്റെ മൂട്ടിലിട്ട് നല്ല വീക്ക് വീക്കും 😡😡😡`", 
    "`ഈ പൂട്ടിന്റെ മുകളിൽ നീ നിന്റെ പൂട്ടിട്ട് പൂട്ടിയാൽ നിന്നെ ഞാൻ പൂട്ടും .. ഒടുക്കത്തെ പൂട്ട് 😡`",
    "`തമ്പുരാൻന്ന് വിളിച്ച അതെ നാവോണ്ട് തന്നെ ചെ** എന്ന് വിളിച്ചതിൽ മനസ്താപണ്ട്..എടോ അപ്പനെന്നു പേരുള്ള തേർഡ് റേറ്റ് ചെ** താനാരാടോ നാട്ടുരാജാവോ 😡😡`", 
    "`ചന്തുവിനെ തോൽപ്പിക്കാൻ ആവില്ല മക്കളേ 😍😍🤗`", 
    "`കൊച്ചി പഴയ കൊച്ചിയെല്ലെന്നറിയാ.... പക്ഷെ ബിലാൽ പഴയ ബിലാൽ തന്നെയാ 😈😈`",
    "`നെട്ടൂരാനോടാണോടാ നിന്റെ കളി 😜😜`", "`ഗോ എവേ സ്റ്റുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂ വിൽ നാട്ട് സീ എനി മിനിറ്റ് ഓഫ് ദി റ്റുഡേ.. എറങ്ങിപ്പോടാ 😜🤭🤣`",
    "`ആണ്ടവൻ ഇത് നിന്റെ കോയമ്പത്തൂരിലെ മായാണ്ടിക്കൊപ്പമല്ല കൊച്ചിയാ വിശ്വനാഥന്റെ കൊച്ചി 😎😎`", 
    "`ഇതെന്റെ പുത്തൻ റെയ്ബാൻ ഗ്ലാസ്സാ ഇത് ചവിട്ടിപൊട്ടിച്ചാ നിന്റെ കാല് ഞാൻ വെട്ടും 😡😡😜`",
]

RAPE_STRINGS = [
    "`വേലക്കാരി ആയിരുന്താലും നീ എൻ മോഹവല്ലി....🥰`", 
    "`ഭവാനി ഒന്നു മനസ്സ് വെച്ചാൽ ഈ കലവറ നമുക്ക് മണിയറ ആക്കാം.....🥰🥰`", 
    "`ഒരു മുത്തം തരാൻ പാടില്ല എന്നൊന്നും അന്റെ ഉപ്പാപ്പ പറഞ്ഞിട്ടുണ്ടാവില്ലല്ല....🥰😜`", 
    "`ശോഭേ ഞാനൊരു വികാര ജീവിയാണ് 😜😜🥰😂 `",
    "`നിനക്കെന്നെ പ്രേമിച്ചൂടെ കൊച്ചേ 😜😜`",
    "`എങ്കിലേ എന്നോട് പറ ഐ ലവ് യൂന്ന് 🥰🥰🥰 `",
    "`പോരുന്നോ എന്റെ കൂടെ 🥰🥰 `",
    "`എനിക്ക് നിന്റെ പുറകിൽ നടക്കാനല്ല, ഒപ്പം നടക്കാനാണ് ഇഷ്ടം 🥰😍`", 
    "`ഓളാ തട്ടമിട്ടു കഴിഞ്ഞാലെന്റെ സാറേ, പിന്നെ ചുറ്റുമുള്ളതൊന്നും കാണാൻ പറ്റൂല്ലാ 😍🥰`",
] 
THANOS_STRINGS = [
   "`തെറി കേട്ടിട്ട് ഇവളുടെ വീട് കൊടുങ്ങല്ലൂർ ഭാഗത്താണെന്ന് തോന്നുന്നു...😜😜`",
   "`പുന്നാര മോളേ😜😜🤭 `", 
   "`ചങ്ക് പറിച്ചു തരുന്ന ചങ്കത്തി കൂടെയുള്ളപ്പോൾ പിന്നെന്തിനാ ലവർ 🥰😜 `",
   "`ഇവൾ നമ്മളേക്കാൾ തറയാടാ...😂😂🤭`",
   "`അഹങ്കാരത്തിന് കയ്യും കാലും വെയ്ക്കാ... എന്നിട്ട് പെണ്ണെന്നു പേരും...🤣🤣😜`",
   "`ആനി മോനെ സ്നേഹിക്കുന്ന പോലെ , മാഗ്ഗിക്ക് എന്നെ സ്നേഹിക്കാമോ...🥰🥰😘`", 
   "`അല്ല ഇതാരാ ! വാര്യംപള്ളിയിലെ മീനാക്ഷിയല്ലയോ ? എന്താ മോളേ സ്കൂട്ടർല്...😜😜🤣`",     
]
ABUSEHARD_STRING = [
     "`നിന്റെ പേരെന്താന്നാ പറഞ്ഞെ -പൈലി ഡ്രാഗൺപൈലി ഡ്യൂഡ് സാറെന്ന്യല്ലേ പേരിട്ടത്.. എന്തൂള പേരാടാത് അയ്യേ...😛😛😜`", 
     "`ദാമോദരൻ ഉണ്ണി മകൻ ദിൽമൻ ഇടക്കൊച്ചി, പീപ്പിൾ കാൾ മീ ഡ്യൂഡ് 😎😎🤨 `", 
     "`മധ്യതിരുവിതാംകൂർ ഭരിച്ച രാജാവാ പേര് ശശി.. 😛😂🤣 `", 
     "`തീരുമ്പോ തീരുമ്പോ പണി തരാൻ ഞാനെന്താ കുപ്പീന്ന് വന്ന ഭൂതോ... 😇😇🙄`",
     "`ഒന്ന് മിണ്ടാതിരിക്കുവോ.. എന്റെ കോൺസെൻട്രേഷൻ പോണ്.. ദേ ആയുധം വെച്ചുള്ള കളിയാ 😝😝😂`", 
     "`സൂക്ഷിച്ചു നോക്കണ്ടടാ ഉണ്ണീ ഇത് ഞാനല്ല...😇🤣🤣`", 
     "`ഈ യന്ത്രങ്ങളുടെ പ്രവർത്തനമൊന്നും താനെന്നെ പഠിപ്പിക്കേണ്ട ഞാനേ പോളിടെക്‌നിക് പഠിച്ചതാ 😎😎😝 `",
     "`ഡിങ്കോൾഫി അല്ലേ ഇത്രക്ക് ചീപ്പാണോ അര്ടിസ്റ്റ് ബേബി😉😉😜 `",
     "`ആദ്യമായി പ്രേമിച്ച പെണ്ണും ആദ്യമായി അടിച്ച ബ്രാൻഡും ഒരാളും ഒരു കാലത്തും മറക്കില്ല്യ😜😜😎`", 
     "`ഡാ മോനേ അത് ലോക്കാ ഇങ്ങ് പോര്.. ഇങ്ങ് പോര്..😇😇🤭`", 
     "`അടിച്ചതാരാടാ നിന്നെ ആണ്ടവനോ സേഡ്‌ജിയോ അടിച്ചതല്ല ചവിട്ടിയതാ ഷൂസിട്ട കാലുകൊണ്ട് 🤭🤭🤭`",
     "`വസൂ... ദേ തോറ്റു തുന്നം പാടി വന്നിരിക്കുന്നു നിന്റെ മോൻ...🤭🤭😜`", 
     "`വോ ലമ്പേ.... വോ ബാത്തേ.... കോഴീ ന ജാനേ.... ങേ കോഴിയോ 🐓🐓🐓`",
     "`എന്താ? പെൺകുട്ടികൾക്കിങ്ങനെ സിമ്പിൾ ഡ്രെസ് ധരിക്കുന്ന പുരുഷന്മാരെ ഇഷ്ടമല്ലേ ? ഡോണ്ട് ദെ ലൈക് ?😎😜`", 
     "`ലേലു അല്ലു ലേലു അല്ലു ലേലു അല്ലു അഴിച്ചു വിട് 🤣🤣`", 
     "`ഇതെന്താ , എനിക്കുമാത്രം പ്രാന്തായതാണോ അതോ നാട്ടുകാർക്ക് മൊത്തത്തിൽ പ്രാന്തായോ ?😇😇🤣`",
     "`അങ്ങനെ പവനായി ശവമായി.. എന്തൊക്കെ ബഹളമായിരുന്നു.. മലപ്പുറം കത്തി, മെഷീൻഗണ്ണു, ബോംബ്, ഒലക്കേടെ മൂട്...🤭🤣🤣`", 
]

PRO_STRINGS = [
     "`ഡാ മങ്കി മാങ്ങാതലയാ 😜`", 
     "`വല്യ മലരനാണല്ലോടാ നീ`", 
     "`പോയി ചാവടാ കള്ള പന്നീ`", 
     "`പോയി തൊലയെടാ തവളാച്ചി മോറാ😜 `", 
     "`മാറിപ്പോടാ മരം കൊത്തി മോറാ😜`",
     "`പുന്നാര മോനേ പോയി ചത്തൂടെ നിനക്ക് 😜`",
     "`നീ പോടാ കാട്ടുകോഴീ😜`", 
     "`കോപ്പേ വല്യ ബഹളം വേണ്ട😜`", 
     "`പുന്നാര മോനേ 😜`", 
     "`പ്ഫാ ഇറങ്ങി പോടാ മാക്രി 😜`",
     "`നിന്റെ പെട്ടീം കെടക്കേം എടുത്ത് ഇപ്പോ ഇറങ്ങിക്കോണം ഇവിടുന്ന് `",
     "`ഇനി നീ വാ തുറന്നാൽ മണ്ണ് വാരി ഇടും 😜`",
     "`അടിച്ചു നിന്റെ മണ്ട പൊളിക്കും കേട്ടോടാ മരപ്പട്ടീ... 😡😜`",
     "`മത്തങ്ങാ തലയാ 😜`", 
     "`മാങ്ങാണ്ടി മോറാ 😜`",
]

SLAP_TEMPLATES = [
    "{user1} {victim} ന്റെ തലക്ക് ഒലക്ക കൊണ്ട് അഞ്ചാറു അടി കൊടുത്തു 😪😪 .", 
    "{user1} ചാണകം വാരി {victim} ന്റെ മോന്തക്ക് എറിഞ്ഞു 🤢🤮 .",
    "️{user1} ഓടി വന്ന് {victim} ന്റെ തലയിൽ ചീമുട്ടയെറിഞ്ഞു 🤭🤭😜.",
    "{user1} ️{victim} നെ കാലേ വാരി നിലത്തടിച്ചു 🤓☹️",
    "️{user1} വലിയ പാറക്കല്ലെടുത്തു {victim} ന്റെ തലക്കെറിഞ്ഞു 😱😱🤭 .",
    "{user1} {victim} നെ വിളിച്ചോണ്ട് പോയി പൊട്ടകിണറ്റിൽ തള്ളിയിട്ടു 🤗🤗😝 .", 
    "️{user1} കാക്കയെ വിളിച്ചു വരുത്തി {victim} ന്റെ തലയിൽ അപ്പിയിടീച്ചു 😝🤣 .",
    "{user1} ഓടി വന്ന് ചൂരൽ കൊണ്ട് {victim} ന്റെ ചന്തിക്കിട്ട് അഞ്ചാറു അടി കൊടുത്ത് 😂😜 .",
    "{user1} {victim} നെ കൊതുകിനെ കൊല്ലുന്ന പോലെ അടിച്ചു കൊന്നു 🤭😜.", 
    "️{user1} കോഴിക്കാഷ്ടം എടുത്ത് {victim} ന്റെ മുഖത്തു തേച്ചു 🤭🤣.",
    "{user1} {victim} നെ എടുത്തോണ്ട് പോയി ചാണകക്കുഴിയിലിട്ടു 🤣🤣😛.",
    "️{user1} പട്ടിയെ അഴിച്ചു വിട്ട് {victim} ന്റെ ചന്തിയിൽ കടിപ്പിച്ചു 😂😂😛.",
    "{user1} കട്ടുറുറുമ്പിനെകൊണ്ട് {victim} ന്റെ കുണ്ടിക്ക് കടിപ്പിച്ചു 🤭🤭😜", 
    "{user1} {victim} നെ കോഴിയാണെന്ന് കരുതി കൂട്ടിലടച്ചു 🤭🤭😜", 
]


# ===========================================

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Sur_vivor"

@borg.on(admin_cmd(pattern="mslap ?(.*)"))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.edit(caption)

    except:
        await event.edit("`Can't slap this nibba !!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap strangers !!`")
            return None

    return replied_user

async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)		  

    caption = temp.format(user1=DEFAULTUSER, victim=slapped)

    return caption

@borg.on(admin_cmd(outgoing=True, pattern="mrape"))
async def raping (raped):
        index = random.randint(0, len(RAPE_STRINGS) - 1)
        reply_text = RAPE_STRINGS[index]
        await raped.edit(reply_text)

@borg.on(admin_cmd(outgoing=True, pattern="mshe"))
async def thanos (thanos):
        index = random.randint(0, len(THANOS_STRINGS) - 1)
        reply_text = THANOS_STRINGS[index]
        await thanos.edit(reply_text)

@borg.on(admin_cmd(outgoing=True, pattern="mabuse"))
async def fuckedd (abusehard):
        index = random.randint(0, len(ABUSEHARD_STRING) - 1)
        reply_text = ABUSEHARD_STRING[index]
        await abusehard.edit(reply_text)

@borg.on(admin_cmd(outgoing=True, pattern="mruns"))
async def metoo(hahayes):
        await hahayes.edit(random.choice(NOOBSTR))
        
@borg.on(admin_cmd(outgoing=True, pattern="minsult$"))
async def proo (pros):
        index = random.randint(0, len(PRO_STRINGS) - 1)
        reply_text = PRO_STRINGS[index]
        await pros.edit(reply_text)        
