import random
import re
import time
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

plugin_category = "utils"


@catub.cat_cmd(
    pattern="alivu$",
    command=("alivu", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alivu",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "✮ MY BOT IS RUNNING SUCCESSFULLY ✮"
    CAT_IMG = gvarstatus("ALIVE_PIC")
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        PIC = random.choice(CAT)
        cat_caption = f"┏━━━━━━━━━━━━━━┓\n"
        cat_caption += f"┃**私は生きています**\n"
        cat_caption += f"┃**{EMOJI} Sama : {mention}**\n"
        cat_caption += f"┃**{EMOJI} telethon._version_:** `{version.__version__}\n`"
        cat_caption += f"┃**{EMOJI} catub -v :** `{catversion}`\n"
        cat_caption += f"┃**{EMOJI} python3 -V :** `{python_version()}\n`"
        cat_caption += f"┗━━━━━━━━━━━━━━┛"
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            f"**{ALIVE_TEXT}**\n"
            f"**{EMOJI} Master : {mention}**\n"
            f"**Please put an image/video as alive pic\n",
        )
