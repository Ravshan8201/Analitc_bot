TOKEN = '2031680092:AAF-zb_Y-NoTXIPeYIn_7x8CypDQNrOxkgs'
dct = {1:['''Здраствуйте, {}! Вас приветствует официальный телеграм бот Аналитического центра  ''',#0
             'Пожалуйта, введите ваше имя:',#1
             '{}, вы уже есть в нашей базе, нам не хватает вашего номера(\nСкиньте ваш контакт ',#2
              'нажмите на кнопку далее...',#3
              'Поделиться контактом☎',#4
              '''Подилитесь контактом☎: ''', #5
              'Добавлено✅', #6
              '🛒Корзина', #7
              '🏬Город', #8
              '📞Номер телефона', #9
              'Язык🇷🇺🇺🇿', #10
              'ГОТОВО✅', #11
              'Подтвердить✅', #12
              '➕🛒Добавить в корзину', #13
              '⬅️Назад', #14
              'Выберите', #15
              '🏠Главное меню',#16
              '🛍Заказать',#17
              '🚫Очистить корзину'
             ],

       2:[
           '''Assalomu alaykum, {}! Siz Tahliliy va ilmiy axborot xizmatlari markazining rasmiy telegram bot kanaliga tashrif buyurdingiz!!!''', #0
           'Iltimos, ismingizni kiriting:', #1
           '{}, siz bizning malumotlar bazamizda mavjudsiz, bizga sizning telefon raqamingiz kerak (\nKontaktingizni ulashing ', #2
           '', #3
           'Kontaktni ulashish☎️', #4
           '''Kontaktingizni ulashishing☎️: ''', #5
           '''Qo'shildi✅''', #6
           '🛒Korzina', #7
           '🏬Shahar', #8
           'Telefon nomer☎️', #9
           'Til🇺🇿🇷🇺', #10
           'TAYYOR✅', #11
           'Tasdiqlash✅', #12
           '''➕🛒Korzinaga qo'shish''',  # 13
           '⬅️Orqaga', #14
           'Tanlang', #15
           '🏠Asosiy menyu',  # 16
           '🛍Buyurtma berish',#17
           '🚫 Korzinani tozalash'

       ]

}
maindct = {

    1:[
        '📊📑Услуги Центра',
        '🗃Мои заказы',
        '📨Оставить отзыв',
        '⚙️🛠Настройки',
        '',
        '',
        '',

    ],

    2:[
        '📊📑Markaz xizmatlari',
        '🗃Meening buyurtmalarim',
        '📨Fikr bildirish',
        '⚙️🛠Sozmalar',
        '',
        '',
        '',
    ]

}

uslugadct = {
    1:[
        'Справочно-информационное обслуживание',#0
        'Консультационные услуги',#1
        'Определение показателей научного рейтинга',#2
        'Организация информационного обучения',#3
        # 1
        'Составление библиографического списка литературы по теме запроса',#4
        'Полнотекстовые ресурсы', #5
        'Составление списка научных журналов для публикации', #6
        'Регулярное (ежемесячное) информирование клиентов о новых изданиях и поступлениях', #7
        'Разовое информирование о новых изданиях', #8
        # 2
        '''Консультации по поиску и использованию инструментария научных информационных ресурсов''',  # 9
        '''Консультации по написанию научных статей''',  # 10
        '''Консультации по подготовке и написанию диссертаций''',  # 11
        '''Консультации по поиску и выбору научных журналов для публикации''',  # 12
        # 3
        '''Оказание помощи в создании и управлении профилем ученого''',  # 13
        '''Оказание помощи в создании и управлении профилем организации''',  # 14
        '''Анализ публикационной активности авторов''',  # 15
        '''Анализ публикационной активности организации''',  # 16
        '''Присвоение DOI научным публикациям''',  # 17
        '''Услуги проверки на Антиплагиат''',  # 18
        # 4
        '''Проведение семинаров/вебинаров''',  # 19
        '''Проведение тренингов/мастер-классов''',  # 20


    ],

    2:[
        '''Ma^lumot va axborot xizmati''',  # 0
        '''Maslahat xizmatlari''',  # 1
        '''Ilmiy reyting ko^rsatkichlarini aniqlash''',  # 2
        '''Axborot ta^limni tashkil etish''',  # 3
        # 1
        '''So^rov mavzusi bo^yicha adabiyotlarning bibliografik ro^yxatini tuzish''',  # 4
        '''To^liq matnli manbalar''',  # 5
        '''Maqolani nashr qilish uchun ilmiy jurnallar ro^yxatini tuzish''',  # 6
        '''Mijozlarni yangi nashrlar va tushumlar haqida muntazam xabardor qilish''',  # 7
        '''Yangi nashrlar haqida bir martalik xabar''',  # 8
        # 2
        '''Ilmiy axborot resurslari vositalarini izlash va ulardan foydalanish bo^yicha   maslahatlar berish''',  # 9
        '''Ilmiy maqolalar yozish bo^yicha maslahat berish''',  # 10
        '''Dissertatsiyalarni tayyorlash va yozish bo^yicha maslahatlar''',  # 11
        '''Maqolani nashr qilish uchun ilmiy jurnallarni izlash va tanlash bo^yicha maslahatlar berish''',  # 12
        # 3
        '''Ijtimoiy tarmoqlarda profil yaratish va boshqarishda yordam berish''',  # 13
        '''Tashkilot profilini yaratish va boshqarishda yordam berish''',  # 14
        '''Mualliflarning nashriyot faoliyatini tahlil qilish''',  # 15
        '''Tashkilotning nashriyot faoliyatini tahlil qilish''',  # 16
        '''Ilmiy nashrlarga DOI ni belgilash''',  # 17
        '''Plagiatga tekshirish xizmati''',  # 18
        # 4
        '''Seminarlar/vebinarlar o^tkazish''',  # 19
        '''Treninglar/mahorat-darslarni o^tkazish''',  # 20


    ]


}



obldct = {
    1:[
        'Ташкентская область',#0
        'Город Ташкент',#1
        'Андижанская область',#2
        'Бухарская область',#3
        'Джизакская область',#4
        'Кашкадарьинская область', #5
        'Наманганская область', #6
        'Навоийская область', #7
        'Самаркандская область', #8
        'Сурхандарьинская область', #9
        'Сырдарьинская область', #10
        'Ферганская область',  # 11
        'Хорезмская область',  # 12
        'Республика Каракалпакстан',  # 13
        '',  # 14
        '',  # 15
    ],

    2:[
        '''Toshkent viloyati''',  # 0
        'Toshkent',  # 1
        '''	Andijon viloyati''',  # 2
        'Buxoro viloyati',  # 3
        'Jizzah viloyati',  # 4
        'Qashqadaryo viloyati',  # 5
        'Namangan viloyati',  # 6
        'Navoiy viloyati', # 7
        'Samarqand viloyati',  # 8
        'Surxondaryo viloyati',  # 9
        'Sirdaryo viloyati',  # 10
        'Farg’ona viloyati	',  # 11
        'Xorazm viloyati',  # 12
        'Qoraqalpog’iston Respublikasi',  # 13
        '',  # 14
        '',  # 15
        '',  # 16

    ]


}

uslugadct2 = {
    1:[

        'Составление библиографического списка литературы по теме запроса',#4
        'Полнотекстовые ресурсы', #5
        'Составление списка научных журналов для публикации', #6
        'Регулярное (ежемесячное) информирование клиентов о новых изданиях и поступлениях', #7
        'Разовое информирование о новых изданиях', #8
        # 2
        '''Консультации по поиску и использованию инструментария научных информационных ресурсов''',  # 9
        '''Консультации по написанию научных статей''',  # 10
        '''Консультации по подготовке и написанию диссертаций''',  # 11
        '''Консультации по поиску и выбору научных журналов для публикации''',  # 12
        # 3
        '''Оказание помощи в создании и управлении профилем ученого''',  # 13
        '''Оказание помощи в создании и управлении профилем организации''',  # 14
        '''Анализ публикационной активности авторов''',  # 15
        '''Анализ публикационной активности организации''',  # 16
        '''Присвоение DOI научным публикациям''',  # 17
        '''Услуги проверки на Антиплагиат''',  # 18
        # 4
        '''Проведение семинаров/вебинаров''',  # 19
        '''Проведение тренингов/мастер-классов''',  # 20

    ],

    2:[

        '''So'rov mavzusi bo'yicha adabiyotlarning bibliografik ro'yxatini tuzish''',  # 4
        '''To'liq matnli manbalar''',  # 5
        '''Maqolani nashr qilish uchun ilmiy jurnallar ro'yxatini tuzish''',  # 6
        '''Mijozlarni yangi nashrlar va tushumlar haqida muntazam xabardor qilish ''',  # 7
        '''Yangi nashrlar haqida bir martalik xabar''',  # 8
        # 2
        '''Ilmiy axborot resurslari vositalarini izlash va ulardan foydalanish boʻyicha   maslahatlar berish''',  # 9
        '''Ilmiy maqolalar yozish bo'yicha maslahat berish''',  # 10
        '''Dissertatsiyalarni tayyorlash va yozish bo'yicha maslahatlar''',  # 11
        '''Maqolani nashr qilish uchun ilmiy jurnallarni izlash va tanlash bo'yicha maslahatlar berish''',  # 12
        # 3
        '''Ijt^moiy tarmoqlarda profil yaratish va boshqarishda yordam berish''',  # 13
        '''Tashkilot profilini yaratish va boshqarishda yordam berish''',  # 14
        '''Mualliflarning nashriyot faoliyatini tahlil qilish''',  # 15
        '''Tashkilotning nashriyot faoliyatini tahlil qilish''',  # 16
        '''Ilmiy nashrlarga DOI ni belgilash''',  # 17
        '''Plagiatga tekshirish xizmati''',  # 18
        # 4
        '''Seminarlar/vebinarlar o'tkazish''',  # 19
        '''Treninglar/mahorat-darslarni o'tkazish''',  # 20


    ]


}



cost_dct = {

    1:{
        'Составление библиографического списка литературы по теме запроса':'1 источник/6000 сум',
        'Полнотекстовые ресурсы':'Книга/ монография/30000 сум;  Учебное пособие/ диссертация/25000 сум',
        'Составление списка научных журналов для публикации': '1 журнал/30000 сум',
        'Регулярное (ежемесячное) информирование клиентов о новых изданиях и поступлениях': 'Годовая/72000 сум;  Полугодовая/48000 сум;  Квартальная/ 30000 сум',
        'Разовое информирование о новых изданиях': '1 месяц/20000 сум',
        'Консультации по поиску и использованию инструментария научных информационных ресурсов': 'Поиск по 1 базе/35000 сум',
        'Консультации по написанию научных статей': 'цена договорная',
        'Консультации по подготовке и написанию диссертаций': 'цена договорная',
        'Консультации по поиску и выбору научных журналов для публикации': '30000 сум',
        'Оказание помощи в создании и управлении профилем ученого': '1 профиль/1 система/ 35000 сум',
        'Оказание помощи в создании и управлении профилем организации': '1 профиль/1 система/ 45000 сум',
        'Анализ публикационной активности авторов': '1 справка/ 30000 сум',
        'Анализ публикационной активности организации': '1 справка/ 40000 сум',
        'Присвоение DOI научным публикациям': '50000 сум',
        'Услуги проверки на Антиплагиат': '1 диссертация/50000 сум',
        'Проведение семинаров/вебинаров': '2 часа (не менее 10 чел.)/ цена договорная',
        'Проведение тренингов/мастер-классов': '1,5 часа (не менее 10 чел.)/ цена договорная',



    },
    2:{

        '''So^rov mavzusi bo^yicha adabiyotlarning bibliografik ro^yxatini tuzish''': '''1 manba/6000 so^m''',
        '''To^liq matnli manbalar''': '''Ilmiy jurnal / konferentsiya to^plami maqolasi/20 000 so^m;  Kitob / monografiya/30000 s^'m;  O^quv qo^llanma / dissertatsiya/25000 so^m''',
        '''Maqolani nashr qilish uchun ilmiy jurnallar ro^yxatini tuzish''': '''1 jurnal/30000 so^m''',
        '''Mijozlarni yangi nashrlar va tushumlar haqida muntazam xabardor qilish''': '''Yillik/ 72000 so^m;  Yarim yillik/ 48000 so^m;  Har chorakda/ 30000 so^m''',
        '''Yangi nashrlar haqida bir martalik xabar''': '''1 oy uchun/20000 so^m''',
        '''Ilmiy axborot resurslari vositalarini izlash va ulardan foydalanish bo^yicha   maslahatlar berish''': '''Поиск по 1 базе/35000 сум''',
        '''Ilmiy maqolalar yozish bo^yicha maslahat berish''': '''narxi kelishilgan holda''',
        '''Dissertatsiyalarni tayyorlash va yozish bo^yicha maslahatlar''': '''narxi kelishilgan holda''',
        '''Maqolani nashr qilish uchun ilmiy jurnallarni izlash va tanlash bo^yicha maslahatlar berish''': '''30000 so^m''',
        '''Ijtimoiy tarmoqlarda profil yaratish va boshqarishda yordam berish''': '''1 profil/1 tizim/ 35000 so^m''',
        '''Tashkilot profilini yaratish va boshqarishda yordam berish''': '''1 profil/1 tizim/ 45000 so^m''',
        '''Mualliflarning nashriyot faoliyatini tahlil qilish''': '''1 ma^lumotnoma/ 30000 so^m''',
        '''Tashkilotning nashriyot faoliyatini tahlil qilish''': '''1 ma^lumotnoma/ 40000 s^'m''',
        '''Ilmiy nashrlarga DOI ni belgilash''': '''50000 so^m''',
        '''Plagiatga tekshirish xizmati''': '''1 dissertatsiya/50000 so^m''',
        '''Seminarlar/vebinarlar o^tkazish''': '''2 soat (kamida 10 kishi) / narxi kelishilgan holda''',
        '''Treninglar/mahorat-darslarni o^tkazish''': '''1,5 soat (kamida 10 kishi) / narxi kelishilgan holda''',


    }

}

otzivdct = {

    1:[
        '😊Все понравилось ⭐️⭐️⭐️⭐️⭐️',
        '☺️Нормально, на 4 ⭐️⭐️⭐️⭐️',
        '😐Удовлетворительно на 3 ⭐️⭐️⭐️',
        '☹️Не понравилось, на 2 ⭐️⭐️',
        '😤Хочу пожаловаться 👎🏻',
        'Спасибо за Ваш отзыв. Мы рады сотрудничеству!'
    ],

    2:[
        '😊Hammasi yoqdi ⭐️⭐️⭐️⭐️⭐️',
        '☺️Yaxshi ⭐️⭐️⭐️⭐️',
        '😐Yoqmadi ⭐️⭐️⭐️',
        '☹️Yomon ⭐️⭐️',
        '😤Juda yomon 👎🏻',
        'Bildirgan fikringiz uchun rahmat. Biz hamkorlik qilishdan xursandmiz!'

    ]

}