from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

import keyboard.Replykeyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    keyboard = await kb.create_pc_control_menu()
    await bot.send_animation(
        chat_id=message.chat.id,
        animation="https://i.pinimg.com/originals/08/e4/1c/08e41c2059323fad9b46ea6a18d1b8ef.gif",
        caption="Панель управления ПК",
        reply_markup=keyboard
    )