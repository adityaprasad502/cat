import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import catub
plugin_category = "utils"

# t.me/sandy1709
async def purge(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)

# t.me/Lal_Bakthan
@catub.cat_cmd(
    pattern="tc ([\s\S]*)",
    command=("tc", plugin_category),
    info={
        "header": "To search a phone number in Truecaller",
        "description": "Searches the given number in the truecaller and provides the details.",
        "usage": "{tr}tc <phone>",
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
            await catevent.edit("__Please unblock @RespawnRobot and try again.__")
            return
        await catevent.edit(details)
    await purge(event, chat, start_msg)

# t.me/realnub
