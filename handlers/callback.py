from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, BufferedInputFile
import keyboard.Replykeyboard as kb
import platform
import subprocess
import pyautogui
import io
from datetime import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import asyncio

router = Router()

# ================== MENU BUTTON ==================
@router.callback_query(F.data == "menu")
async def menu_handler(callback: CallbackQuery, bot: Bot):
    """Return menu"""
    await callback.answer("Back menu")
    
    # Удаляем старое сообщение и отправляем новое с гифкой
    await callback.message.delete()
    
    keyboard = await kb.create_pc_control_menu()
    await bot.send_animation(
        chat_id=callback.message.chat.id,
        animation="https://i.pinimg.com/originals/08/e4/1c/08e41c2059323fad9b46ea6a18d1b8ef.gif",
        caption="Панель управления ПК",
        reply_markup=keyboard
    )

# ================== OFF BUTTON ====================
@router.callback_query(F.data == "shutdown_pc")
async def shutdown_handler(callback: CallbackQuery):
    """Обработчик кнопки выключения ПК"""
    await callback.answer()
    
    confirmation_keyboard = await kb.create_shutdown_confirmation()
    
    # Универсальное редактирование
    if callback.message.caption is not None:
        await callback.message.edit_caption(
            caption="⚠️ Вы уверены, что хотите выключить ПК?",
            reply_markup=confirmation_keyboard
        )
    else:
        await callback.message.edit_text(
            "⚠️ Вы уверены, что хотите выключить ПК?",
            reply_markup=confirmation_keyboard
        )

@router.callback_query(F.data == "confirm_shutdown")
async def confirm_shutdown_handler(callback: CallbackQuery):
    """Confirm off ПК"""
    await callback.answer("🖥️ Выключаю ПК...")

    menu_button = await kb.create_back_to_menu_button()
    
    # Универсальное редактирование
    if callback.message.caption is not None:
        await callback.message.edit_caption(
            caption="🖥️ ПК выключается...",
            reply_markup=menu_button
        )
    else:
        await callback.message.edit_text(
            "🖥️ ПК выключается...",
            reply_markup=menu_button
        )
    
    await execute_shutdown()

@router.callback_query(F.data == "cancel_shutdown")
async def cancel_shutdown_handler(callback: CallbackQuery):
    """Отмена выключения ПК"""
    await callback.answer("❌ Выключение отменено")
    
    keyboard = await kb.create_pc_control_menu()
    
    # Универсальное редактирование
    if callback.message.caption is not None:
        await callback.message.edit_caption(
            caption="Панель управления ПК",
            reply_markup=keyboard
        )
    else:
        await callback.message.edit_text(
            "Панель управления ПК",
            reply_markup=keyboard
        )
    
async def execute_shutdown():
    """Off PC"""
    system = platform.system().lower()
 
    try:
        if system == "windows":
            subprocess.run(["shutdown", "/s", "/t", "10"], check=True)
        elif system == "linux" or system == "darwin":
            subprocess.run(["sudo", "shutdown", "-h", "+1"], check=True)
        else:
            print(f"Unkown ОС: {system}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выключении: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
        
# ================== SCREENSHOT ======================
@router.callback_query(F.data == "screenshot")
async def screenshot_handler(callback: CallbackQuery, bot: Bot):
    await callback.answer("📸 Делаю скриншоТ...")
    
    try:        
        screenshot = pyautogui.screenshot()
        
        img_byte_arr = io.BytesIO()
        screenshot.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        photo_file = BufferedInputFile(
            img_byte_arr.getvalue(), 
            filename="screenshot.png"
        )
        
        await bot.send_photo(
            chat_id=callback.message.chat.id,
            photo=photo_file,
            caption=f"📸 Скриншот от {datetime.now().strftime('%H:%M:%S')}"
        )
        
        menu_button = await kb.create_back_to_menu_button()
        await callback.message.answer(
            "📸 Скриншот отправлен!",
            reply_markup=menu_button
        )
    except Exception as e:
        print(f"Ошибка при создании скриншота: {e}")
        await callback.answer("Ошибка при создании скриншота")
        menu_button = await kb.create_back_to_menu_button()
        await callback.message.answer(
            " Не удалось сделать скриншот",
            reply_markup=menu_button
        )

#=========================== YOUTUBE =====================================
@router.callback_query(F.data == "youtube")
async def youtube_handler(callback: CallbackQuery):
    """Кнопка Ютуб"""
    await callback.answer("Открываю...")
    
    try:
        
        webbrowser.open("https://www.youtube.com")
        
        menu_button = await kb.create_back_to_menu_button()
        
        if callback.message.caption is not None:
            await callback.message.edit_caption(
				caption="Youtube opened",
				reply_markup=menu_button
			)
        else:
            await callback.message.edit_text(
				"YouTube openede",
				reply_markup=menu_button
			)
    except Exception as e:
        print(f"Ошибка при открытии YouTube: {e}")
        await callback.answer(" Ошибка при открытии YouTube")
        
        menu_button = await kb.create_back_to_menu_button()
        if callback.message.caption is not None:
            await callback.message.edit_caption(
                caption="Не удалось открыть YouTube",
                reply_markup=menu_button
            )
        else:
            await callback.message.edit_text(
                "Не удалось открыть YouTube",
                reply_markup=menu_button
            )
            
#==================== Telegram ==================           
@router.callback_query(F.data == "telegram")
async def youtube_handler(callback: CallbackQuery):
    """Кнопка Телеграм"""
    await callback.answer("Открываю...")
    
    try:
        
        webbrowser.open("https://web.telegram.org/a/")	
        
        menu_button = await kb.create_back_to_menu_button()
        
        if callback.message.caption is not None:
            await callback.message.edit_caption(
				caption="Telegram opened",
				reply_markup=menu_button
			)
        else:
            await callback.message.edit_text(
				"Telegram openede",
				reply_markup=menu_button
			)
    except Exception as e:
        print(f"Ошибка при открытии Telegram: {e}")
        await callback.answer(" Ошибка при открытии Telegram")
        
        menu_button = await kb.create_back_to_menu_button()
        if callback.message.caption is not None:
            await callback.message.edit_caption(
                caption="Не удалось открыть Telegram",
                reply_markup=menu_button
            )
        else:
            await callback.message.edit_text(
                "Не удалось открыть Telegram",
                reply_markup=menu_button
            )
        
        
#==============================================================

# ================== NEWS BUTTON ==================
@router.callback_query(F.data == "news")
async def news_handler(callback: CallbackQuery):
    """Обработчик кнопки Новости"""
    await callback.answer("📰 Получаю свежие новости...")
    
    try:
        news_data = await get_news_any_source()
        
        menu_button = await kb.create_back_to_menu_button()
        
        await callback.message.answer(
            news_data,
            reply_markup=menu_button,
            disable_web_page_preview=False
        )
        
    except Exception as e:
        print(f"Ошибка при получении новостей: {e}")
        await callback.answer("❌ Ошибка при получении новостей")
        
        menu_button = await kb.create_back_to_menu_button()
        await callback.message.answer(
            "❌ Не удалось получить новости",
            reply_markup=menu_button
        )

async def get_news_any_source():
    """Пробует получить новости из разных источников"""
    
    sources = [
        get_meduza_news,      # Meduza - простой RSS
        get_lenta_news,       # Lenta.ru
        get_rt_news,          # RT News
    ]
    
    for source in sources:
        try:
            news = await source()
            if news and "❌" not in news:
                return news
        except:
            continue
    
    return "❌ Не удалось получить новости ни из одного источника"

# ================== MEDUZA (самый надежный) ==================
async def get_meduza_news():
    """Новости с Meduza через RSS"""
    try:
        import feedparser
        
        rss_url = "https://meduza.io/rss/all"
        feed = feedparser.parse(rss_url)
        
        if feed.entries:
            latest_news = feed.entries[0]
            title = latest_news.title
            link = latest_news.link
            
            return f"📰 **Meduza - Последняя новость:**\n\n{title}\n\n🔗 {link}"
        else:
            return "❌ Не удалось получить новости с Meduza"
            
    except Exception as e:
        return f"❌ Ошибка Meduza: {str(e)}"

# ================== LENTA.RU ==================
async def get_lenta_news():
    """Новости с Lenta.ru"""
    try:
        url = "https://lenta.ru"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'lxml')
        
        
        main_news = soup.find('a', class_='card-mini__title')
        if not main_news:
            main_news = soup.find('h3', class_='card-big__title')
        if not main_news:
            main_news = soup.find('a', class_='_title')
            
        if main_news:
            title = main_news.get_text(strip=True)
            link = main_news.get('href')
            
            if link and link.startswith('/'):
                link = "https://lenta.ru" + link
            
            return f"📰 **Lenta.ru - Последняя новость:**\n\n{title}\n\n🔗 {link}"
        else:
            return "❌ Не удалось найти новости на Lenta.ru"
            
    except Exception as e:
        return f"❌ Ошибка Lenta.ru: {str(e)}"

# ================== RT NEWS ==================
async def get_rt_news():
    """Новости с RT"""
    try:
        url = "https://russian.rt.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'lxml')
        
        main_news = soup.find('a', class_='link')
        if not main_news:
            main_news = soup.find('div', class_='card__heading')
        if not main_news:
            main_news = soup.find('h2')
            
        if main_news:
            title = main_news.get_text(strip=True)
            link = main_news.get('href')
            
            if link and link.startswith('/'):
                link = "https://russian.rt.com" + link
            elif link and link.startswith('//'):
                link = "https:" + link
            
            return f"📰 **RT - Последняя новость:**\n\n{title}\n\n🔗 {link}"
        else:
            return "❌ Не удалось найти новости на RT"
            
    except Exception as e:
        return f"❌ Ошибка RT: {str(e)}"

# ================== TASS (простая структура) ==================
async def get_tass_news():
    """Новости с ТАСС"""
    try:
        url = "https://tass.ru"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        main_news = soup.find('a', class_='news-line__item')
        if not main_news:
            main_news = soup.find('span', class_='news-line__text')
            
        if main_news:
            title = main_news.get_text(strip=True)
            link = main_news.get('href')
            
            if link and link.startswith('/'):
                link = "https://tass.ru" + link
            
            return f"📰 **ТАСС - Последняя новость:**\n\n{title}\n\n🔗 {link}"
        else:
            return "❌ Не удалось найти новости на ТАСС"
            
    except Exception as e:
        return f"❌ Ошибка ТАСС: {str(e)}"