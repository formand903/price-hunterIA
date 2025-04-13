# Price Hunter Bot

ИИ-агент Telegram для поиска товаров с лучшим соотношением цена/качество на Wildberries и Ozon.

## Как запустить

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Создайте `.env` файл и вставьте ваш токен бота:

```
BOT_TOKEN=ваш_токен_от_BotFather
```

3. Запустите бота:

```bash
python bot.py
```

## Деплой на Render

- Загрузите файлы проекта в репозиторий.
- В Render создайте Web Service (Python).
- Укажите команду запуска: `python bot.py`
- В Environment добавьте переменную `BOT_TOKEN`.

