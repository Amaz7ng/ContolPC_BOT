from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_pc_control_menu():
    builder = InlineKeyboardBuilder()
    
    button1 = InlineKeyboardButton(text="🖥️ Секрет", callback_data="shutdown_pc")
    button2 = InlineKeyboardButton(text="🎥 YouTube", callback_data="youtube")
    button3 = InlineKeyboardButton(text="🔉 News", callback_data="news")
    button4 = InlineKeyboardButton(text="🔉 Telegram", callback_data="telegram")
    button5 = InlineKeyboardButton(text="📸 Screenshot", callback_data="screenshot")
    
    builder.row(button1)
    builder.row(button2, button3, button4)
    builder.row(button5)
    
    return builder.as_markup()
  

async def create_back_to_menu_button():
    """Создает кнопку для возврата в главное меню"""
    builder = InlineKeyboardBuilder()
    button = InlineKeyboardButton(text="🏠 Menu", callback_data="menu")
    builder.row(button)
    return builder.as_markup()

async def create_shutdown_confirmation():
    """Клавиатура для подтверждения выключения ПК"""
    builder = InlineKeyboardBuilder()
    
    button_yes = InlineKeyboardButton(text="✅ Уверен?", callback_data="confirm_shutdown")
    button_no = InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_shutdown")
    
    builder.row(button_yes, button_no)
    return builder.as_markup()
