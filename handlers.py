import os

from aiogram import types, Router, F
from aiogram.types import FSInputFile

from keyboards import mentorlar, kurslarimiz, start_button, language, kurslarimiz1, start_button1

router = Router()


@router.message(F.text == "Информация про компанию")
async def gef_about_company(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), 'images', 'инфа_про_компанию.jpg'))

    text = "8 лет опыта, более 2000 учеников и опытных наставников!"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Наши преподы🎓")
async def gef_mentorlar(msg: types.Message):
    img1 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    img2 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    img3 = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    mentorlar = [
        [img1, "Хабибулла Нуридинов"],
        [img2, "Шохрух Абдурахманов"],
        [img3, "Аброржон Абдусаидов"]
    ]
    for mentor in mentorlar:
        await msg.answer_photo(photo=mentor[0], caption=mentor[1])


@router.message(F.text == "Наши курсы")
async def gef_kurslarimiz(msg: types.Message):
    await msg.answer(text="Наши курсы", reply_markup=kurslarimiz)


@router.message(F.text == "Пайтон Джуниор")
async def gef_python(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images","пайтон_джуниор.jpg"))
    text = "Python - Основы боевого фиксинга и программирования"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Фронтед Джуниор")
async def gef_frontend(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "js.jpg"))
    text = "Это интерпретируемый язык программирования, который используют для написания frontend- и backend-частей сайтов, а также мобильных приложений"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Робототехника")
async def gef_robototexnika(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "роботяга.jpg"))
    text = "Робототехника опирается на такие дисциплины, как электроника, механика, кибернетика, телемеханика, мехатроника[4], информатика, а также радиотехника и электротехника"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Скретч")
async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "кашак.jpg"))
    text = "Он создан как продолжение идей языка Лого и конструктора Лего."
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Контакт/Местоположение")
async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "gps.jpg"))
    text = "+998 78 777-74-77"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "🔙Назад")
async def gef_back(msg: types.Message):
    await msg.answer(text="back", reply_markup=start_button)


@router.message(F.text == "Рус/Еng Язык")
async def gef_eng(msg: types.Message):
    await msg.answer("Выберитье один из языков", reply_markup=language)


@router.message(F.text == "Rus")
async def select_language(msg: types.Message):
    await msg.answer(text="Ваш выбор остановился на русском языке", reply_markup=start_button)


@router.message(F.text == "Eng")
async def select_language(msg: types.Message):
    await msg.answer(text="Your choice has stopped at English", reply_markup=start_button1)


@router.message(F.text == "Company Information")
async def gef_about_company(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "инфа_про_компанию.jpg"))
    text = "8 years of experience, more than 2000 students and experienced mentors!"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Our Courses")
async def gef_kurslarimiz(msg: types.Message):
    await msg.answer(text="Our Courses", reply_markup=kurslarimiz1)


@router.message(F.text == "Python Junior")
async def gef_python(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "пайтон_джуниор.jpg"))
    text = "Python - Basics of Combat Fixing and Programming"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Fronted Junior")
async def gef_frontend(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "js.jpg"))
    text = "It is an interpreted programming language that is used to write frontend and backend parts of websites, as well as mobile applications."
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Robotics")
async def gef_robototexnika(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "роботяга.jpg"))
    text = "Robotics is based on such disciplines as electronics, mechanics, cybernetics, telemechanics, mechatronics[4], computer science, as well as radio engineering and electrical engineering"
    await msg.answer_photo(photo=company_image, caption=text)


@router.message(F.text == "Scratch")
async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "кашак.jpg"))
    text = "It was created as a continuation of the ideas of the Logo language and the Lego constructor."
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


@router.message(F.text == "Rus/Eng languige")
async def gef_eng(msg: types.Message):
    await msg.answer("Choose one of languages", reply_markup=language)


@router.message(F.text == "Contact/Location")
async def gef_scratch(msg: types.Message):
    company_image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "gps.jpg"))
    text = "+998 78 777-74-77"
    await msg.answer_photo(photo=company_image, caption=text)