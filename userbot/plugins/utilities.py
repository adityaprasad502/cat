import asyncio
import calendar

import bs4
import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

plugin_category = "utils"

BOT = "@HowGayBot"
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
    catevent = await edit_or_reply(event, "__Processing...__")
    chat = "@RespawnRobot"
    await reply_id(event)
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


@catub.cat_cmd(
    pattern="gey ([\s\S]*)",
    command=("gey", plugin_category),
    info={
        "header": "try yourself.",
        "description": "try yourself.",
        "usage": "{tr}gey <name>.",
    },
)
async def app_search(event):
    "try yourself"
    name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "`Calculating!..`")
    id = await reply_id(event)
    try:
        score = await event.client.inline_query(BOT, name)
        await score[0].click(event.chat_id, reply_to=id, hide_via=True)
        await event.delete()
    except Exception as err:
        await event.edit(str(err))


@catub.cat_cmd(
    pattern="iapp ([\s\S]*)",
    command=("iapp", plugin_category),
    info={
        "header": "To search any app in playstore via inline.",
        "description": "Searches the app in the playstore and provides the link to the app in playstore and fetches app details via inline.",
        "usage": "{tr}iapp <name>",
    },
)
async def app_search(event):
    "To search any app in playstore via inline."
    app_name = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    event = await edit_or_reply(event, "`Searching!..`")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )

        app_details = "**App Name:** " + app_name + "\n**Developer:** "
        app_details += f"[{app_dev}]({app_dev_link})" + "\n**Rating:**"
        app_details += (
            app_rating.replace("Rated ", " ")
            .replace(" out of ", "/")
            .replace(" stars", "", 1)
            .replace(" stars", " ⭐ ")
            .replace("five", "5")
        )
        catinput = "Inline buttons " + app_details
        catinput += f" [DOWNLOAD]<buttonurl:{app_link}>"
        results = await event.client.inline_query(Config.TG_BOT_USERNAME, catinput)
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()

    except IndexError:
        await event.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))


# t.me/realnub
