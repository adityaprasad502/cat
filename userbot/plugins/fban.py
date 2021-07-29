import os

from telethon.tl.functions.users import GetFullUserRequest
from ..utils import admin_cmd , sudo_cmd

nospam = -1001178182087
plugin_category = "tools"

@bot.on(admin_cmd("fban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
	    reason = event.pattern_match.group(1)
    else:
        reason = "Spam Bot!"
    if event.reply_to_msg_id:
        spam_message = await event.get_reply_message()
        spammer = await event.client(
            GetFullUserRequest(spam_message.sender_id)
        )
        userid = str(spammer.user.id)
        async with event.client.conversation(nospam) as conv:
            try:
                await conv.send_message("/fban " + userid + " " +  reason)
                await conv.get_response()
                await event.delete()
            except YouBlockedUserError:
                await event.edit("`An Error occurred!`")
    else:
        async with event.client.conversation(nospam) as conv:
            try:
                await conv.send_message("/fban " +  reason)
                await conv.get_response()
                await event.delete()
            except YouBlockedUserError:
                await event.edit("`An Error occurred!`")


@bot.on(admin_cmd("unfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
	    reason = event.pattern_match.group(1)
    else:
        reason = "Spam Bot!"
    if event.reply_to_msg_id:
        spam_message = await event.get_reply_message()
        spammer = await event.client(
            GetFullUserRequest(spam_message.sender_id)
        )
        userid = str(spammer.user.id)
        async with event.client.conversation(nospam) as conv:
            try:
                await conv.send_message("/unfban " + userid + " " + reason)
                await conv.get_response()
                await event.delete()
            except YouBlockedUserError:
                await event.edit("`An Error occurred!`")
    else:
        async with event.client.conversation(nospam) as conv:
            try:
                await conv.send_message("/unfban " + reason)
                await conv.get_response()
                await event.delete()
            except YouBlockedUserError:
                await event.edit("`An Error occurred!`")
