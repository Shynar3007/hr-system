import os
import json
import requests
from datetime import datetime

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

# Список сотрудников — добавляйте сюда
employees = [
    {"name": "Айгерим Бекова", "position": "HR-менеджер", "birthday": "1989-03-15"},
    {"name": "Нурлан Сейткали", "position": "Разработчик", "birthday": "1992-01-10"},
    {"name": "Дина Жумабекова", "position": "Бухгалтер", "birthday": "1998-11-01"},
    {"name": "Асет Нурмагамбетов", "position": "Менеджер продаж", "birthday": "1988-07-20"},
]

JUBILEES = [30, 35, 40, 45, 50, 55, 60]

today = datetime.today()

for emp in employees:
    bday = datetime.strptime(emp['birthday'], '%Y-%m-%d')
    if bday.month == today.month and bday.day == today.day:
        age = today.year - bday.year
        is_jubilee = age in JUBILEES
        if is_jubilee:
            msg = (f"🎊🎉 ЮБИЛЕЙ! 🎉🎊\n\n"
                   f"👤 {emp['name']}\n"
                   f"💼 {emp['position']}\n"
                   f"🎂 Исполняется {age} лет!\n\n"
                   f"Не забудьте поздравить! 🌟")
        else:
            msg = (f"🎂 День рождения!\n\n"
                   f"👤 {emp['name']}\n"
                   f"💼 {emp['position']}\n"
                   f"🎂 Исполняется {age} лет\n\n"
                   f"Не забудьте поздравить! 🎉")

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
        )
