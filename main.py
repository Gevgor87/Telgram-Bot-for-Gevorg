from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove
from config import TOKEN
from buttons import inline_kb_1, inline_kb_2, kb_geo_1, inline_problems
import logging
import asyncio
from datetime import datetime


logging.basicConfig(level=logging.INFO) #Basic Loging
bot = Bot(token=TOKEN) # You must past your Token here
dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot Start")


@dp.message_handler(commands=["start"])
async def start_command(message:types.Message):
    await message.answer(text=f"Hello {message.from_user.first_name}")
    print(message)


@dp.message_handler(commands=["miac"])
async def miac_command(message:types.Message):
    await message.answer(text=f"Message_1 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", reply_markup=inline_kb_1)


@dp.message_handler(content_types=["location"])
async def mess_com(message:types.Message):
    global lat
    global long
    lat = message.location.latitude
    long = message.location.longitude
    await bot.send_message(chat_id=message.from_user.id, text="Thank You!", reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text = "hasceum")
async def location_command(callback:types.CallbackQuery):
    await callback.answer(text="Please Share your location")
    await bot.send_message(chat_id=callback.from_user.id, text="Share Location. Press the button below 👇", reply_markup=kb_geo_1)
    await asyncio.sleep(15)
    try:
        # await bot.send_location(chat_id=callback.message.chat.id, latitude=lat, longitude=long)
        await callback.message.edit_text(text=f"Message_2 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\nlatitude {lat}\nlongitude {long}", reply_markup=inline_kb_2)
    except:
        await bot.send_message(chat_id=callback.message.chat.id, text="ERROR, Please try again")


@dp.callback_query_handler(text = "avart")
async def end_command(callback:types.CallbackQuery):
    await callback.answer(text="Very Good 👍")
    await callback.message.edit_text(text=f"Message_3 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    await bot.send_message(chat_id=callback.message.chat.id, text="Do you have some problems?", reply_markup=inline_problems)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("pr"))
async def problem_command(callback:types.CallbackQuery):
    if callback.data == "pr_no_problem":
        await callback.answer(text="It is nice")
        await callback.message.delete()
    else:
        await callback.answer(text="Houston we have problem")
        await bot.send_message(chat_id=callback.message.chat.id, text=f"have problem with {callback.data[3:].upper()}")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)