from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

inline_kb_1 = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Hasceum enq", callback_data="hasceum")],
    [InlineKeyboardButton(text="Avart", callback_data="avart")]
])

inline_kb_2 = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Avart", callback_data="avart")]
])

inline_problems = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="kabel", callback_data="pr_kabel"), InlineKeyboardButton(text="wifi", callback_data="pr_wifi"), InlineKeyboardButton(text="onu", callback_data="pr_onu")],
    [InlineKeyboardButton(text="ont", callback_data="pr_ont"), InlineKeyboardButton(text="gin", callback_data="pr_gin"), InlineKeyboardButton(text="TvBox", callback_data="pr_tvbox")],
    [InlineKeyboardButton(text="mag", callback_data="pr_mag"), InlineKeyboardButton(text="kapuyt-ONU", callback_data="pr_kapuyt-ONU"), InlineKeyboardButton(text="No problem", callback_data="pr_no_problem")]
])

kb_geo_1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_for_geo = KeyboardButton(text="/location", request_location=True)
kb_geo_1.add(button_for_geo)
