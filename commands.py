import os
import types

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from keyboards import start_button
router = Router()
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    img = FSInputFile(os.path.join(os.path.dirname(__file__), 'images', 'photo_2025-03-13_10-09-21.jpg'))
    text = "доброго времени суток это бот про учебную компания PDP Junior"
    await message.answer_photo(photo=img, caption=text, reply_markup=start_button)
