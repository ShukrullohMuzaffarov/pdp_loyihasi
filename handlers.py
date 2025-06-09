import os

from aiogram import types
from aiogram.dispatcher import router
from aiogram.types import FSInputFile

from keyboards import language


async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "кашак.jpg"))
    text = "It's just a mess"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Back")
async def gef_back(msg: types.Message):
    await msg.answer(text="Back", reply_markup=start_button1)


@router.message(F.text == "Our Teachers")
async def gef_teachers(msg: types.Message):
    img4 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    img5 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    img6 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    teachers = [
        [img4, "Habibulla Nuridinov"],
        [img5, "Shokhrukh Abdurakhmanov"],
        [img6, "Abrorjon Abdusaidov"]]
    for teacher in teachers:
        await msg.answer_photo(photo=teacher[0], caption=teacher[1])


@router.message(F.text == "rus/eng anguige")
async def gef_eng(msg: types.Message):
    await msg.answer("Choose one of languages", reply_markup=language)


@router.message(F.text == "Contact/Location")
async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "контакт.jpg"))
    text = "+998 78 777-74-77"
    await msg.answer_photo(photo=company_image, caption=text)


