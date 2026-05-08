import asyncio
from pyrogram import Client
from pyrogram.types import (
    ChatJoinRequest,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# API DETAILS
API_ID = 36323488
API_HASH = "0fd9b7274110884086070dbf183a8e18"
BOT_TOKEN = "8631535910:AAFUTShjQ2p-EhO_wtvmLgitf37R9xqeTI4"

# BOT CLIENT
app = Client(
    "auto_accept_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# AUTO APPROVE JOIN REQUEST
@app.on_chat_join_request()
async def approve(client, request: ChatJoinRequest):

    user = request.from_user.first_name

    print(f"Request from {user}")

    # 10 SECOND WAIT
    await asyncio.sleep(10)

    # APPROVE REQUEST
    await request.approve()

    print(f"{user} approved")

    # BUTTONS
    buttons = InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🔥 13𝙇 𝙂𝘼𝙈𝙀 𝙑𝙄𝙋 𝙃𝘼𝘾𝙆 🔥",
                url="https://t.me/+f_hZH2paA9s0NTQ9"
            )
        ],

        [
            InlineKeyboardButton(
                "💰𝙑𝙄𝙋 𝙋𝙍𝙀𝘿𝙄𝘾𝙏𝙄𝙊𝙉 𝘾𝙃𝘼𝙉𝙉𝙀𝙇💰",
                url="https://t.me/+JS8v50YuJvVjM2E1"
            )
        ],

        [
            InlineKeyboardButton(
                "✅ JOIN CHANNEL",
                url="https://t.me/+yvZq5LOWQtQwMDE1"
            )
        ]

    ])

    # SEND PHOTO + MESSAGE
    try:

        await client.send_photo(
            chat_id=request.from_user.id,

            # DIRECT IMAGE URL
            photo="https://ibb.co/xd3vsYK",

            caption=f"""
🔥 Hello {user} 🔥

✅ Your join request has been approved!

🏏 13𝙇 𝙂𝘼𝙈𝙀 𝙑𝙄𝙋 𝙃𝘼𝘾𝙆
💰 𝙑𝙄𝙋 𝙋𝙍𝙀𝘿𝙄𝘾𝙏𝙄𝙊𝙉 𝘾𝙃𝘼𝙉𝙉𝙀𝙇
🎯 𝙅𝘼𝙄 𝘾𝙇𝙐𝘽 𝙑𝙄𝙋 𝙃𝘼𝘾𝙆
🔥 𝙏𝘼𝙎𝙃𝘼𝙉 𝙒𝙄𝙉 𝙑𝙄𝙋 𝙃𝘼𝘾𝙆

👇 Join Channels Below 👇
""",

            reply_markup=buttons
        )

    except Exception as e:
        print(e)

# START BOT
if __name__ == "__main__":
    print("Bot Running...")
    app.run()
