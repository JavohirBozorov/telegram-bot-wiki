import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1940846951:AAEc-fYLX_tzekrnnAgqb6UTT_mWmr6TLcY11'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Wikipedia Botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Men sizga <b>Wikipedia</b>dagi malumotlarni olib beraman!\n\n     🔎   🔎   🔎   \n\nQidirayotgan malumotingizni menga yuboring", parse_mode='HTML')

@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
