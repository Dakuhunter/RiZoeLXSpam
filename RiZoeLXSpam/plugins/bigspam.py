async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20
from RiZoeLXSpam.config import SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@Riz.on(events.NewMessage(pattern=".bigspam"))
@Riz2.on(events.NewMessage(pattern=".bigspam"))
@Riz3.on(events.NewMessage(pattern=".bigspam"))
@Riz4.on(events.NewMessage(pattern=".bigspam"))
@Riz5.on(events.NewMessage(pattern=".bigspam"))
@Riz6.on(events.NewMessage(pattern=".bigspam"))
@Riz7.on(events.NewMessage(pattern=".bigspam"))
@Riz8.on(events.NewMessage(pattern=".bigspam"))
@Riz9.on(events.NewMessage(pattern=".bigspam"))
@Riz10.on(events.NewMessage(pattern=".bigspam"))
@Riz11.on(events.NewMessage(pattern=".bigspam"))
@Riz12.on(events.NewMessage(pattern=".bigspam"))
@Riz13.on(events.NewMessage(pattern=".bigspam"))
@Riz14.on(events.NewMessage(pattern=".bigspam"))
@Riz15.on(events.NewMessage(pattern=".bigspam"))
@Riz16.on(events.NewMessage(pattern=".bigspam"))
@Riz17.on(events.NewMessage(pattern=".bigspam"))
@Riz18.on(events.NewMessage(pattern=".bigspam"))
@Riz19.on(events.NewMessage(pattern=".bigspam"))
@Riz20.on(events.NewMessage(pattern=".bigspam"))
async def spam(e):
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            counter = int(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
