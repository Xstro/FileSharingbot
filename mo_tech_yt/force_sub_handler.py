# (c) @MRK_YT

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="**Sorry Sirπ**, **You are Banned to use me. Contact my** [πΈGroup](https://t.me/CinemaFlixz).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\n**Files ΰ΄΅ΰ΅ΰ΄£ΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΅½ ΰ΄ΰ΄€ΰ΅ΰ΄―ΰ΄ ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄³ΰ΅ΰ΄ΰ΅ Update Channelil ΰ΄ΰ΅ΰ΄―ΰ΄Ώΰ΅» ΰ΄ΰ΅ΰ΄―ΰ΅ΰ΄―ΰ΄£ΰ΄...!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("π ππ¨π’π§ ππ©πππ­π ππ‘ππ§π§ππ₯ π", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("π¦ α΄α΄α΄ α΄Κα΄α΄Κ", url="https://t.me/GxNeo")
                    ],
                    [
                        InlineKeyboardButton("π ππππ«ππ¬π‘ π", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [πΈGroup](https://t.me/CinemaFlixz).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
