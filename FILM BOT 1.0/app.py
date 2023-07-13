#by кот хакер 1234#
#Downloaded from TG @KiTools#
#Leave this inscription#

from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from loader import dp, bot, admin_id
from heandlers import dp
from keybord_s.ohter import ikb_close

#отмена любого состаяния#
@dp.callback_query_handler(text='cancellation_state', state='*')
async def cancellation_state(call: types.Message, state: FSMContext):
    await state.finish()
    await call.answer('Отмена❌')
    await call.message.delete()

#закрыть#
@dp.callback_query_handler(text='close_text')
async def cancellation_state(call: types.Message):
    await call.message.delete()

#уведомления о запуске#
async def satrt_nofication(self):
    try:
        me=await bot.get_me()
        await bot.send_message(chat_id=admin_id, text=f'Bot worked {me.mention}', reply_markup=ikb_close)
        print(f'Bot worked {me.mention}')
    except:
        print(f'Bot worked {me.mention}')
        print('Вы не нажали /start в сеом боте!')

executor.start_polling(dp, on_startup=satrt_nofication)

