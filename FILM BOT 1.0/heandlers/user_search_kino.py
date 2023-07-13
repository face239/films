#by @K1p1k#
#Downloaded from TG @KiTools#
#Leave this inscription#
from loader import bot, dp
from aiogram import types
from keybord_s.user import kb_films, sub_list
from misc.chek_chennel import check as sub_check
from bs4 import BeautifulSoup
import requests

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer('Фильм можно найти раз в 30 секунд😪')

async def spisok_number_to60():
    counter_number=int()
    spisok=str()
    while counter_number != 60:
        counter_number+=1
        spisok+=f'{str(counter_number)} '
    spisok=spisok.split()
    return spisok

@dp.message_handler()
@dp.throttled(anti_flood, rate=30)
async def search_kino_parser(message: types.Message):

    if await sub_check(user_id=message.from_user.id):
        await bot.send_message(chat_id=message.from_user.id, text='Вы не подписаны на канал(ы)❌\nПосле подписки повторите попытку👌', reply_markup=await sub_list())
        return

    try:
        url='https://kino.mail.ru/search/?q='+message.text
        request=requests.get(url)
        soup=BeautifulSoup(request.text, "html.parser")
        a=soup.find('div', class_='margin_top_20')

        url='https://kino.mail.ru'+a.find('a')['href']
        request=requests.get(url)
        soup=BeautifulSoup(request.text, "html.parser")

        type_kino=soup.find('div', class_='p-truncate p-truncate_background-gray p-truncate_multiline p-truncate_multiline-3 p-truncate_multiline-podrobnee js-module js-toggle__truncate margin_bottom_20 reset-inner-fonts')
        type_kino=type_kino.find('h2', class_='text text_inline text_bold_normal text_fixed text_letter-spacing text-mode_uppercase valign_baseline').text
        type_kino=type_kino[type_kino.find(' '):type_kino.find(':')][1:-1].title()

        film_data=soup.find('div', class_='block block_bg_gray padding_vertical_x8')
        more=soup.find_all('div', class_='margin_bottom_20')

        for i in more:
            zhanar=i.find_all('span', class_='nowrap')
            if zhanar != []:
                break
        for i in zhanar:
            zhanar_one=i.find('a', class_='badge badge_gray badge_gray_rgba badge_border_off badge_link')
            if zhanar_one != None:
                break

        photo=film_data.find('picture', class_='picture p-framer__picture').find('img')['src']
        director=film_data.find('div', class_='p-truncate p-truncate_ellipsis js-module js-toggle__truncate js-toggle__truncate js-toggle__truncate-first').text
        text_autor=film_data.find('div', class_='table__cell padding_right_10').text
        name_film=soup.find('div', class_='p-movie-intro__content-inner').find('h1',class_='text text_light_promo color_white').text
        #try:
        film_data2=soup.find_all('div', class_='margin_bottom_20')
    
        for i in film_data2:
            dlina=i.find('span', class_='margin_left_40 nowrap')
            try:
                if dlina != None and dlina.text[0] in await spisok_number_to60():
                    break
            except:
                pass
        if dlina == None:
            dlina='Неизвестно'
        else:
            dlina=dlina.text
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=f'🎥{type_kino}: {name_film}\n\n👁Основной жанр: {zhanar_one.text}\n\n👥{text_autor}: {director}\n\n🔗Длительность: {dlina}', reply_markup=await kb_films(name_films=name_film))
    except:
        pass
 
#Автор: @K1p1k#
#Загружено с TG @KiTools#
#Оставь эту надпись#
