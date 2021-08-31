import os, urllib

from ..helpers.functions import convert_tosticker, higlighted_text
from . import catub, deEmojify, edit_delete, reply_id

plugin_category = "fun"

@catub.cat_cmd(
    pattern="(|h)pay(?:\s|$)([\s\S]*)",
    command=("pay", plugin_category),
    info={
        "header": "Send money to anyone through paytm.",
        "flags": {
            "h": "To create paytm sticker with highlighted font.",
        },
        "usage": [
            "{tr}pay <text/reply to msg>",
            "{tr}hpay <text/reply to msg>",
        ],
        "examples": [
            "{tr}pay Czyneko",
            "{tr}hpay VinuXD",
        ],
    },
)
async def pay(event):
    "To create $1000 paytm payment sticker with the receiver name that you want."
    vinuxd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    czyneko = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await edit_delete(
            event, "__To whom do you want to send money? Gib his/her name!__"
        )
    await edit_delete(event, "__Wait, processing...__")
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    temp_name = "./temp/pay_temp.jpg"
    file_name = "./temp/pay.jpg"
    vinu = urllib.request.urlretrieve(
        "https://telegra.ph/file/847a028fbf453f1c83fc8.jpg", temp_name
    )
    text = deEmojify(text)
    font, wrap = (65, 1) if len(text) < 90 else (65, 1)
    bg, fg, alpha, ls = (
        ("black", "white", 255, "5") if vinuxd == "h" else ("white", "black", 0, "-40")
    )
    higlighted_text(
        temp_name,
        text,
        file_name,
        text_wrap=wrap,
        font_size=font,
        linespace=ls,
        position=(3, 580),
        align="left",
        background=bg,
        foreground=fg,
        transparency=alpha,
    )
    realnub = convert_tosticker(file_name)
    await event.client.send_file(
        event.chat_id, realnub, reply_to=czyneko, force_document=False
    )
    await event.delete()
    for files in (temp_name, file_name):
        if files and os.path.exists(files):
            os.remove(files)
