import asyncio
from pyrogram import Client
from pyrogram.types import (
    ChatJoinRequest,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

API_ID = 36323488
API_HASH = "0fd9b7274110884086070dbf183a8e18"
BOT_TOKEN = "8631535910:AAFUTShjQ2p-EhO_wtvmLgitf37R9xqeTI4"

app = Client(
    "auto_accept_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_chat_join_request()
async def approve(client, request: ChatJoinRequest):

    user = request.from_user.first_name

    print(f"Request from {user}")

    # 1 minute wait
    await asyncio.sleep(60)

    # approve request
    await request.approve()

    print(f"{user} approved")

    # buttons
    buttons = InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🔥 13L GAME VIP 🔥",
                url="https://t.me/+yvZq5LOWQtQwMDE1"
            )
        ],

        [
            InlineKeyboardButton(
                "💰 VIP PREDICTION GAME 💰",
                url="https://t.me/+yvZq5LOWQtQwMDE1"
            )
        ],

        [
            InlineKeyboardButton(
                "✅ Join Channel",
                url="https://t.me/+yvZq5LOWQtQwMDE1"
            )
        ]

    ])

    # send welcome photo + message
    try:

        await client.send_photo(
            chat_id=request.from_user.id,

            photo="https://ibb.co/ZkvN99p",

            caption=f"""
🔥 Hello {user} 🔥

✅ Your join request has been approved!

🏏 13L GAME VIP
💰 VIP PREDICTION CHENAL
🎯 JAI CLUB VIP HACK
🔥 TASHAN WIN VIP HACK

👇 Join Channels Below 👇
""",

            reply_markup=buttons
        )

    except Exception as e:
        print(e)

print("Bot Running...")
app.run()