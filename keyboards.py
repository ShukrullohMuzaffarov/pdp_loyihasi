from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_company = KeyboardButton(text="информация про компанию")
mentorlar = KeyboardButton(text="наши преподы")
kurslar = KeyboardButton(text="наши курсы")
contact = KeyboardButton(text="контакт/местоположение")
languige = KeyboardButton(text="рус/eng ЯЗ")
start_button = ReplyKeyboardMarkup(
    keyboard=[
        [about_company, mentorlar],
        [kurslar],
        [contact, languige]
    ], resize_keyboard=True
)


python_junior = KeyboardButton(text="пайтон джуниор")
fronted_junior = KeyboardButton(text="фронтед джуниор")
robototexnika = KeyboardButton(text="робототехника")
scratch = KeyboardButton(text="скретч")
back =KeyboardButton(text="🔙назад")

kurslarimiz = ReplyKeyboardMarkup(
    keyboard=[
        [python_junior, fronted_junior],
        [robototexnika, scratch],
        [back]
    ]
)


about_company1 = KeyboardButton(text="Company Information")
mentorlar1 = KeyboardButton(text="Our Teachers")
kurslar1 = KeyboardButton(text="Our Courses")
contact1 = KeyboardButton(text="Contact/Location")
languige1 = KeyboardButton(text="rus/eng anguige")
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


python_junior1 = KeyboardButton(text="python Junior")
fronted_junior1 = KeyboardButton(text="fronted Junior")
robototexnika1 = KeyboardButton(text="robotics")
scratch1 = KeyboardButton(text="scratch")
back =KeyboardButton(text="Back")

kurslarimiz1 = ReplyKeyboardMarkup(
    keyboard=[
        [python_junior1, fronted_junior1],
        [robototexnika1, scratch1],
        [back]
    ],resize_keyboard=True
)
