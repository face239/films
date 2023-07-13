#by @K1p1k#
#Downloaded from TG @KiTools#
#Leave this inscription#

from loader import dp, bot
from aiogram import types
from keybord_s import admin
from myFilters.admin import IsAdminM

#вызов admin меню#
@dp.message_handler(IsAdminM(), text='/admin')
async def cmd_admin(message: types.Message):
    await message.answer('*Админ меню*', reply_markup=admin.admin_menu_main, parse_mode=types.ParseMode.MARKDOWN_V2)

#Автор: @K1p1k#
#Загружено с TG @KiTools#
#Оставь эту надпись#