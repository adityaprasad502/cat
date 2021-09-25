# plugin edited by @Infinity20998
# added -p flag and customized more by t.me/realnub
import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import catub, hmention, mention

plugin_category = "tools"


@catub.cat_cmd(
    pattern="(p|ping)( -a| -p| -x|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {
            "-a": "For average ping.",
            "-p": "For theme 2.",
            "-x": "For theme 3.",
        },
        "usage": ["{tr}ping", "{tr}ping -a", "{tr}ping -p", "{tr}ping -x"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(2)
    start = datetime.now()
    if flag == " -a":
        catevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await catevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await catevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await catevent.edit(
            f"┏━━━━━━━━━━━━━━┓\n┃ ⁭⁫⁭<b><i>〣 Average Pong!</b></i>\n┃⁭⁫⁭<b><i> ⁭⁫⁭⁭〣 {ms}</b></i>\n┃⁭⁫⁭<b><i> ⁭〣 {hmention}</b></i>\n┗━━━━━━━━━━━━━━┛",
            parse_mode="html",
        )
    elif flag == " -p":
        catevent = await edit_or_reply(event, "__**Pong!..**__")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(
            f"<b><i>〣 Ping: {ms} ms\n〣 Owner: {hmention}</b></i>", parse_mode="html"
        )
    elif flag == " -x":
        catevent = await edit_or_reply(event, "__**Pong!..**__")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(f"Pong!\n`{ms} ms`")
    else:
        catevent = await edit_or_reply(event, "__**Pong!..**__")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(
            f"┏━━━━━━━━━━━━━━┓\n┃ ⁭⁫〣 `{ms}`\n┃ ⁭⁫〣 {mention}\n┗━━━━━━━━━━━━━━┛"
        )
