import asyncio

from userbot import catub

plugin_category = "utils"

# t.me/Lal_Bakthan
@catub.cat_cmd(
    pattern="countdown ([\s\S]*)",
    command=("countdown", plugin_category),
    info={
        "header": "countdown till 0 from given seconds.",
        "description": "countdown till 0 from given seconds.**",
        "usage": "{tr}countdown <seconds>\n\n**⚠️ Warning: Use this plugin at your own risk.",
    },
)
async def _(event):
    "countdown till 0 from given seconds."
    if event.fwd_from:
        return
    try:
        total = event.pattern_match.group(1)
        if not total:
            await edit_delete(
                event, "What I am supposed to do? Gime time in seconds.", 7
            )
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


# @realnub
