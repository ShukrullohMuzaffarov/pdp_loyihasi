from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_company = KeyboardButton(text="Информация про компанию")
mentorlar = KeyboardButton(text="Наши преподы🎓")
kurslar = KeyboardButton(text="Наши курсы")
contact = KeyboardButton(text="Контакт/Местоположение")
languige = KeyboardButton(text="Рус/Еng Язык")
start_button = ReplyKeyboardMarkup(
    keyboard=[
        [about_company, mentorlar],
        [kurslar],
        [contact, languige]
    ], resize_keyboard=True
)


python_junior = KeyboardButton(text="Пайтон Джуниор")
fronted_junior = KeyboardButton(text="Фронтед Джуниор")
robototexnika = KeyboardButton(text="Робототехника")
scratch = KeyboardButton(text="Скретч")
back =KeyboardButton(text="🔙Назад")

kurslarimiz = ReplyKeyboardMarkup(
    keyboard=[
        [python_junior, fronted_junior],
        [robototexnika, scratch],
        [back]
    ], resize_keyboard=True
)


about_company1 = KeyboardButton(text="Company Information")
mentorlar1 = KeyboardButton(text="Our Teachers")
kurslar1 = KeyboardButton(text="Our Courses")
contact1 = KeyboardButton(text="Contact/Location")
languige1 = KeyboardButton(text="Rus/Eng languige")
start_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [about_company1, mentorlar1],
        [kurslar1],
        [contact1, languige1]
    ], resize_keyboard=True
)

rus_btn = KeyboardButton(text="Rus")
eng_btn  = KeyboardButton(text="Eng")
language = ReplyKeyboardMarkup(
    keyboard=[
        [rus_btn, eng_btn],
    ], resize_keyboard=True
)


python_junior1 = KeyboardButton(text="Python Junior")
fronted_junior1 = KeyboardButton(text="Fronted Junior")
robototexnika1 = KeyboardButton(text="Robotics")
scratch1 = KeyboardButton(text="Scratch")
back =KeyboardButton(text="Back")

kurslarimiz1 = ReplyKeyboardMarkup(
    keyboard=[
        [python_junior1, fronted_junior1],
        [robototexnika1, scratch1],
        [back]
    ],resize_keyboard=True
)
