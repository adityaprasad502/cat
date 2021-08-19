import asyncio, calendar

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

plugin_category = "utils"

# t.me/Lal_Bakthan
@catub.cat_cmd(
    pattern="countdown ([\s\S]*)",
    command=("countdown", plugin_category),
    info={
        "header": "countdown",
        "description": "countdown till 0 from given seconds. use at your own risk.",
        "usage": "{tr}countdown <seconds>",
    },
)
async def _(event):
    "countdown till 0 from given seconds. use at your own risk."
    if event.fwd_from:
        return
    try:
     total = event.pattern_match.group(1)
     if not total:
         await edit_delete(event, "What I am supposed to do? Gime time in seconds.", 7)
         return
     t = int(total)
     pluto = await edit_or_reply(event, f"Counter Starting for {total} seconds.")
     while t >= 0:
         mins, secs = divmod(t, 60)
         timer = "{:02d}:{:02d}".format(mins, secs)
         await pluto.edit(str(timer))
         await asyncio.sleep(1)
         t -= 1
     await event.reply(f"Countdown for {total} seconds completed.")
    except Exception as e:
       await edit_delete(event, f"`{e}`", 7)

async def purge(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)

# t.me/Lal_Bakthan
@catub.cat_cmd(
    pattern="cid ([\s\S]*)",
    command=("cid", plugin_category),
    info={
        "header": "To search a phone number in Truecaller",
        "description": "Searches the given number in the truecaller and provides the details.",
        "usage": "{tr}cid <phone>",
    },
)
async def _(event):
    "To search a phone number in Truecaller"
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am supposed to check? Gime a number.")
        return
    catevent = await edit_or_reply(event, f"__Processing...__")
    chat = "@RespawnRobot"
    reply_id_ = await reply_id(event)
    async with event.client.conversation(chat) as conv:
        try:
            start_msg = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(args)
            await asyncio.sleep(2)
            check = await conv.get_response()
            details = check.text
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("__Please unblock (@RespawnRobot) and try again__")
            return
        await catevent.edit(details)
    await purge(event, chat, start_msg)


@catub.cat_cmd(
    pattern="ycal (.*)",
    command=("ycal", plugin_category),
    info={
        "header": "To get calendar of the given year.",
        "usage": "{tr}ycal year",
        "examples": "{tr}ycal 2021\n\nNote: please view this calendar from a pc",
    },
)
async def _(event):
    "To get the calendar of the given year."
    pluto = event.pattern_match.group(1)
    year = pluto
    try:
        cal = calendar.calendar(int(year))
        await edit_or_reply(event, f"`{cal}`")
    except Exception as e:
        await edit_delete(event, f"`{e}`", 7)

# @realnub
