@echo off
chcp 65001
title Установка PC Control Bot

echo ========================================
echo    УСТАНОВКА PC CONTROL BOT
echo ========================================
echo.

echo 🔍 Проверяем Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python не найден!
    echo 📥 Скачайте Python с python.org
    echo 🚀 После установки запустите этот файл снова
    pause
    exit
)

echo ✅ Python обнаружен

echo 📦 Устанавливаем зависимости...
echo Установка aiogram...
pip install aiogram
echo Установка pillow...
pip install pillow
echo Установка pyautogui...
pip install pyautogui
echo Установка beautifulsoup4...
pip install beautifulsoup4
echo Установка requests...
pip install requests
echo Установка feedparser...
pip install feedparser
echo Установка aiohttp...
pip install aiohttp

echo.
echo 🔑 НАСТРОЙКА КОНФИГУРАЦИИ
echo.
set /p bot_token="Введите токен вашего бота: "

echo 🔄 Создаем config.py...
echo TOKEN = "%bot_token%" > config.py

echo 🔄 Создаем start_bot.bat...
echo @echo off > "start_bot.bat"
echo chcp 65001 >> "start_bot.bat"
echo cd /d "%%~dp0" >> "start_bot.bat"
echo python main.py >> "start_bot.bat"
echo pause >> "start_bot.bat"

echo 🔄 Добавляем в автозагрузку...
set "startup=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%startup%\PC_Control_Bot.lnk'); $Shortcut.TargetPath = '%~dp0start_bot.bat'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.Save()"

echo.
echo ========================================
echo          ✅ УСТАНОВКА ЗАВЕРШЕНА!
echo ========================================
echo.
echo 📝 Что было сделано:
echo ├── Установлены все зависимости
echo ├── Создан config.py с вашим токеном
echo ├── Создан start_bot.bat для запуска
echo └── Добавлен в автозагрузку Windows
echo.
echo 🚀 Дальнейшие действия:
echo 1. Бот добавлен в автозагрузку
echo 2. При перезагрузке ПК бот запустится автоматически
echo 3. Напишите /start вашему боту в Telegram
echo.
echo 💡 Токен сохранен: %bot_token:~0,10%...
echo.
pause