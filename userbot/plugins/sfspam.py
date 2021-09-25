# kanged by a noob directly from original spam plugin in catub, all credits goes to the respective devs.
# this plugin contains unwanted imports and unwanted lines of codes etc. that was neccessary for other commands in original plugin.
# If you ended up spamming groups, getting reported and/or floodwaits and/or account limitations/ban, left and right. DON'T BLAME US.
import asyncio

from telethon.utils import get_display_name

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "extra"


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery no-metrics
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#SFSPAM\n"
                        + f"Superfast Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} times with below message",
                    )
                else:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#SFSPAM\n"
                        + f"Superfast Spam was executed successfully in {get_display_name(await event.get_chat())}(`{event.chat_id}`) with {counter} times with below message",
                    )
            elif event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#DELAYSPAM\n"
                    + f"Delay spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} times with below message with delay {sleeptimet} seconds",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#DELAYSPAM\n"
                    + f"Delay spam was executed successfully in {get_display_name(await event.get_chat())}(`{event.chat_id}`) with {counter} times with below message with delay {sleeptimet} seconds",
                )

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await _catutils.unsavegif(event, sandy)
        return
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#SFSPAM\n"
                    + f"Superfast Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#SFSPAM\n"
                    + f"Superfast Spam was executed successfully in {get_display_name(await event.get_chat())}(`{event.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#DELAYSPAM\n"
                + f"Delay Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with delay {sleeptimet} seconds and with {counter} messages of \n"
                + f"`{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#DELAYSPAM\n"
                + f"Delay spam was executed successfully in {get_display_name(await event.get_chat())}(`{event.chat_id}`) chat with delay {sleeptimet} seconds and with {counter} messages of \n"
                + f"`{spam_message}`",
            )


@catub.cat_cmd(
    pattern="sfspam ([\s\S]*)",
    command=("sfspam", plugin_category),
    info={
        "header": "same as .spam with increased speed.",
        "description": "Sends the replied media/message <count> times in the chat",
        "usage": ["{tr}sfspam <count> <text>", "{tr}sfspam <count> reply to message"],
        "examples": "{tr}sfspam 10 hi",
    },
)
async def spammer(event):
    "Floods the text in the chat with superfast speed!!"
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    warn = "`Superfast spamming is very dangerous. Risks of floodwaits, account limitations and even account ban. Use at your own risk.\
 We are not responsible for any issues happens to your account like floodwaits and/or account limitations, ban etc..`\n\n"
    try:
        int(cat[0])
    except Exception:
        return await edit_delete(
            event, "**Use proper syntax to spam. For syntax refer** `.help sfspam`."
        )
    czy = await edit_or_reply(event, warn + "**Starting spam in 5 seconds**")
    await asyncio.sleep(3)
    await czy.edit(warn + "**Starting spam in 2 seconds**")
    await asyncio.sleep(2)
    await event.delete()
    await czy.delete()
    addgvar("spamwork", True)
    await spam_function(event, sandy, cat, 0.001, 0.001)


# @realnub
