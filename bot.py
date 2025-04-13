from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import logging
import os
from db import init_db, save_search, get_user_history
from parser import search_products
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("Привет! Я ИИ-агент для поиска выгодных цен на Wildberries и Ozon. Введи название товара, и я покажу лучшие предложения.")

@dp.message_handler(commands=["история"])
async def history_command(message: Message):
    history = get_user_history(message.from_user.id)
    if not history:
        await message.answer("История пуста.")
    else:
        reply = "Вот твоя история запросов:
" + "\n".join(f"- {item}" for item in history)
        await message.answer(reply)

@dp.message_handler()
async def handle_search(message: Message):
    query = message.text.strip()
    save_search(message.from_user.id, query)
    await message.answer(f"Ищу: {query}...")
    results = search_products(query)
    if not results:
        await message.answer("Ничего не найдено.")
    else:
        for item in results:
            await message.answer(item)

if __name__ == "__main__":
    init_db()
    executor.start_polling(dp, skip_updates=True)
