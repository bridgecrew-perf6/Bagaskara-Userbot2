# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# recode by @ybgskr

import asyncio
import os

import heroku3
from requests import get
from telethon.errors import FloodWaitError

from userbot import BLACKLIST_GCAST
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME
from userbot.utils import edit_delete, edit_or_reply, cilik_cmd


while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/grey423/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001273141346,  # Remix Support Vegeta
    -1001795125065,  # Bagaskara Support
    -1001687155877,  # Grey Cilik Support
    -1001692751821,  # Ram Support
    -1001699144606,  # Kasta Support
    -1001716001073,  # Skyla Support
    -1001554560763,  # Vegeta Support
    -1001578091827,  # Prime Support
    -1001380293847,  # Nasty Support
    -1001683749664,  # Xa Support
    -1001664518224,  # Joni Support
    -1001489233533,  # Rumah Kitaro
    -1001538752127,  # Abing Support
    -1001347414136,  # Musikku Support
]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""


@cilik_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@cilik_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{er}` **chat**"
    )


@cilik_cmd(pattern="blchat$")
async def sudo(event):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            event,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `.addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_delete(event, "🔮 **Blacklist GCAST:** `Disabled`")


@cilik_cmd(pattern="addblacklist(?:\\s|$)([\\s\\S]*)")
async def add(event):
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "BLACKLIST_GCAST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{gc}` **ke daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = blacklistgrup


@cilik_cmd(pattern="delblacklist(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xxx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await edit_delete(
            xxx, "**Grup ini tidak ada dalam daftar blacklist gcast.**", 45
        )


CMD_HELP.update(
    {
        "gcast": f"**➢ Plugin : **`gcast`\
        \n\n ┌✪ **Syntax :** `{cmd}gcast` <text/reply media>\
        \n └✪ **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n ┌✪ **Syntax :** `{cmd}blchat`\
        \n └✪ **Function : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n ┌✪ **Syntax :** `{cmd}addblacklist`\
        \n └✪ **Function : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n ┌✪ **Syntax :** `{cmd}delblacklist`\
        \n └✪ **Function : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n ➠ **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n ┌✪ **Syntax :** `{cmd}gucast` <text/reply media>\
        \n └✪ **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
