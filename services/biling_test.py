

import random

class BilingTest:
    eng_questions: list[str] = [
        "What is the name of our planet?",
        "What is the name of the star around which the Earth revolves?",
        "What is the name of the Earth's satellite?",
        "What shines in the sky during the day?",
        "What shines in the sky at night?",
        "What falls from the sky when it rains?",
        "What falls from the sky in winter?",
        "Where do fish live?",
        "Where do birds live?",
        "Where do people live?",
        "What color is the snow?",
        "What color is the grass?",
        "What color is the sky during the day?",
        "What color is a banana?",
        "What color is the orange?",
        "What color is a tomato?",
        "What color is coal?",
        "What color is the milk?",
        "What animal gives milk?",
        "What animal lays eggs?",
        "What animal says meow?",
        "What animal says woof?",
        "Which animal says mu?",
        "What animal says oink?",
        "What is used for cutting?",
        "What is used for writing?",
        "What do you use to wash your hands?",
        "What is used to clean teeth?",
        "What do you use for sleep?",
        "What do you use to eat soup?",
        "What is used for drinking water?",
        "What is used to measure time?",
        "What is used to measure length?",
        "What is used to measure temperature?",
        "What is used to measure weight?",
        "What does it take to breathe?",
        "What does it take to see?",
        "What does it take to hear?",
        "What does it take to walk?",
        "What do they turn on to make it light?",
        "What do you turn on to keep it warm?"
    ]

    rus_questions: list[str] = [
        "Как называется наша планета?",
        "Как называется звезда, вокруг которой вращается Земля?",
        "Как называется спутник Земли?",
        "Что светит днём на небе?",
        "Что светит ночью на небе?",
        "Что падает с неба во время дождя?",
        "Что падает с неба зимой?",
        "Где живут рыбы?",
        "Где живут птицы?",
        "Где живут люди?",
        "Какого цвета снег?",
        "Какого цвета трава?",
        "Какого цвета небо днём?",
        "Какого цвета банан?",
        "Какого цвета апельсин?",
        "Какого цвета помидор?",
        "Какого цвета уголь?",
        "Какого цвета молоко?",
        "Какое животное даёт молоко?",
        "Какое животное несёт яйца?",
        "Какое животное говорит мяу?",
        "Какое животное говорит гав?",
        "Какое животное говорит му?",
        "Какое животное говорит хрю?",
        "Что используют для резки?",
        "Что используют для письма?",
        "Что используют для мытья рук?",
        "Что используют для чистки зубов?",
        "Что используют для сна?",
        "Что используют для еды супа?",
        "Что используют для питья воды?",
        "Что используют для измерения времени?",
        "Что используют для измерения длины?",
        "Что используют для измерения температуры?",
        "Что используют для измерения веса?",
        "Что нужно, чтобы дышать?",
        "Что нужно, чтобы видеть?",
        "Что нужно, чтобы слышать?",
        "Что нужно, чтобы ходить?",
        "Что включают, чтобы было светло?",
        "Что включают, чтобы было тепло?"
    ]

    ka_questions: list[str] = [
        "რა ჰქვია ჩვენს პლანეტას?",
        "რა ჰქვია ვარსკვლავს, რომლის გარშემოც დედამიწა ბრუნავს?",
        "რა ჰქვია დედამიწის თანამგზავრს?",
        "რა ანათებს ცაში დღის განმავლობაში?",
        "რა ანათებს ცაში ღამით?",
        "რა მოდის ციდან წვიმის დროს?",
        "რა მოდის ციდან ზამთარში?",
        "სად ცხოვრობს თევზი?",
        "სად ცხოვრობენ ფრინველები?",
        "სად ცხოვრობს ხალხი?",
        "რა ფერისაა თოვლი?",
        "რა ფერის არის ბალახი?",
        "რა ფერია ცა დღის განმავლობაში?",
        "რა ფერის არის ბანანი?",
        "რა ფერია ფორთოხალი?",
        "რა ფერია პომიდორი?",
        "რა ფერია ნახშირი?",
        "რა ფერია რძე?",
        "რომელი ცხოველი აძლევს რძეს?",
        "რომელი ცხოველი დებს კვერცხებს?",
        "რომელი ცხოველი ამბობს მეაუს?",
        "რომელი ცხოველი ამბობს ფუფს?",
        "რომელი ცხოველი ამბობს mu?",
        "რომელი ცხოველი ამბობს ოინკს?",
        "რა გამოიყენება ჭრისთვის?",
        "რა გამოიყენება დასაწერად?",
        "რას იყენებთ ხელების დასაბანად?",
        "რა გამოიყენება კბილების გასაწმენდად?",
        "რას იყენებთ ძილისთვის?",
        "რას იყენებთ სუპის საჭმელად?",
        "რა გამოიყენება სასმელ წყალში?",
        "რა გამოიყენება დროის გასაზომად?",
        "რა გამოიყენება სიგრძის გასაზომად?",
        "რა გამოიყენება ტემპერატურის გასაზომად?",
        "რა გამოიყენება წონის გასაზომად?",
        "რა არის საჭირო სუნთქვა?",
        "რა არის საჭირო სანახავად?",
        "რა არის საჭირო მოსასმენად?"
        "რა არის საჭირო სიარული?",
        "რას რთავენ, რომ სინათლე იყოს?",
        "რას ჩართავთ მის შესანარჩუნებლად?",
    ]

    az_questions: list[str] = [
        "Planetimizin adı nədir?",
        "Yerin ətrafında fırlanan ulduzun adı nədir?",
        "Yerin peykinin adı nədir?",
        "Gün ərzində səmada nə işıq saçır?",
        "Gecələr səmada nə parlayır?",
        "Yağış yağanda göydən nə düşür?",
        "Qışda göydən nə yağır?",
        "Balıqlar harada yaşayır?",
        "Quşlar harada yaşayır?",
        "İnsanlar harada yaşayır?",
        "Qar hansı rəngdədir?",
        "Otun rəngi nədir?",
        "Gün ərzində səma hansı rəngdədir?",
        "Banan hansı rəngdədir?",
        "Narıncı hansı rəngdədir?",
        "Pomidor hansı rəngdədir?",
        "Kömür hansı rəngdədir?",
        "Süd hansı rəngdədir?",
        "Hansı heyvan süd verir?",
        "Hansı heyvan yumurta qoyur?",
        "Hansı heyvan miyavlayır?",
        "Hansı heyvan vay deyir?",
        "Hansı heyvan mu deyir?",
        "Hansı heyvan oink deyir?",
        "Kəsmə üçün nə istifadə olunur?",
        "Yazı üçün nə istifadə olunur?",
        "Əllərinizi yumaq üçün nə istifadə edirsiniz?",
        "Dişləri təmizləmək üçün nə istifadə olunur?",
        "Yuxu üçün nə istifadə edirsiniz?",
        "Şorba yemək üçün nə istifadə edirsiniz?",
        "İçməli su üçün nə istifadə olunur?",
        "Vaxtı ölçmək üçün nə istifadə olunur?",
        "Uzunluğu ölçmək üçün nə istifadə olunur?",
        "Temperaturu ölçmək üçün nə istifadə olunur?",
        "Çəki ölçmək üçün nə istifadə olunur?",
        "Nəfəs almaq üçün nə lazımdır?",
        "Görmək üçün nə lazımdır?",
        "Eşitmək üçün nə lazımdır?",
        "Gəzmək üçün nə lazımdır?",
        "İşıqlandırmaq üçün nəyi yandırırlar?",
        "Onu isti saxlamaq üçün nə yandırırsınız?",
    ]

    tt_questions: list[str] = [
        "Планетабызның исеме ничек?",
        "Aroundир әйләнә торган йолдызның исеме ничек?",
        "Satelliteир иярчененең исеме ничек?",
        "Көндез күктә нәрсә балкый?",
        "Төнлә күктә нәрсә балкый?",
        "Яңгыр яуганда күктән нәрсә төшә?",
        "Кыш көне күктән нәрсә төшә?",
        "Балык кайда яши?",
        "Кошлар кайда яши?",
        "Кешеләр кайда яши?",
        "Кар нинди төс?",
        "Grassлән нинди төс?",
        "Көндез күк нинди төс?",
        "Банан нинди төс?",
        "Алсу нинди төс?",
        "Помидор нинди төс?",
        "Көмер нинди төс?",
        "Сөт нинди төс?",
        "Нинди хайван сөт бирә?",
        "Нинди хайван йомырка сала?",
        "Нинди хайван мио ди?",
        "Нинди хайван йон ди?",
        "Кайсы хайван му ди?",
        "Нинди хайван оинк ди?",
        "Кисү өчен нәрсә кулланыла?",
        "Язу өчен нәрсә кулланыла?",
        "Кулларыгызны юар өчен нәрсә кулланасыз?",
        "Тешләрне чистарту өчен нәрсә кулланыла?",
        "Йокы өчен нәрсә кулланасыз?",
        "Шорпа ашар өчен нәрсә кулланасыз?",
        "Эчәрлек су өчен нәрсә кулланыла?",
        "Вакытны үлчәү өчен нәрсә кулланыла?",
        "Озынлыкны үлчәү өчен нәрсә кулланыла?",
        "Температураны үлчәү өчен нәрсә кулланыла?",
        "Авырлыкны үлчәү өчен нәрсә кулланыла?",
        "Сулыш алу өчен нәрсә кирәк?",
        "Күрер өчен нәрсә кирәк?",
        "Нәрсә ишетергә кирәк?",
        "Walkәяү нәрсә кирәк?",
        "Аны яктырту өчен нәрсә кабызалар?",
        "Warmылы булсын өчен сез нәрсә кабызасыз?",
    ]

    eng_answers: list[str] = [
        "Earth",
        "Sun",
        "Moon",
        "Sun",
        "Moon",
        "Rain",
        "Snow",
        "In the water",
        "In the air",
        "On land",
        "White",
        "Green",
        "Blue",
        "Yellow",
        "Orange",
        "Red",
        "Black",
        "White",
        "Cow",
        "Chicken",
        "Cat",
        "Dog",
        "Cow",
        "Pig",
        "Knife",
        "Pen",
        "Soap",
        "Toothbrush",
        "Bed",
        "Spoon",
        "Cup",
        "Watch",
        "Ruler",
        "Thermometer",
        "Scales",
        "Air",
        "Eyes",
        "Ears",
        "Legs",
        "Lamp",
        "Heater"
    ]

    rus_answers: list[str] = [
        "Земля",
        "Солнце",
        "Луна",
        "Солнце",
        "Луна",
        "Дождь",
        "Снег",
        "В воде",
        "В воздухе",
        "На земле",
        "Белый",
        "Зеленый",
        "Голубой",
        "Желтый",
        "Оранжевый",
        "Красный",
        "Черный",
        "Белый",
        "Корова",
        "Курица",
        "Кошка",
        "Собака",
        "Корова",
        "Свинья",
        "Нож",
        "Ручка",
        "Мыло",
        "Зубная щетка",
        "Кровать",
        "Ложка",
        "Чашка",
        "Часы",
        "Линейка",
        "Термометр",
        "Весы",
        "Воздух",
        "Глаза",
        "Уши",
        "Ноги",
        "Лампу",
        "Обогреватель"
    ]

    ka_answers: list[str] = [
        "დედამიწა",
        "მზე",
        "მთვარე",
        "მზე",
        "მთვარე",
        "წვიმა",
        "თოვლი",
        "წყალში",
        "ჰაერში",
        "ხმელეთზე",
        "თეთრი",
        "მწვანე",
        "ლურჯი",
        "ყვითელი",
        "ნარინჯისფერი",
        "წითელი",
        "შავი",
        "თეთრი",
        "ძროხა",
        "ქათამი",
        "კატა",
        "ძაღლი",
        "ძროხა",
        "ღორი",
        "დანა",
        "კალამი",
        "საპონი",
        "კბილის ჯაგრისი",
        "საწოლი",
        "კოვზი",
        "თასი",
        "უყურე",
        "მმართველი",
        "თერმომეტრი",
        "სასწორები",
        "ჰაერი",
        "თვალები",
        "ყურები",
        "ფეხები",
        "ნათურა",
        "გამათბობელი"
    ]

    az_answers: list[str] = [
        "Yer",
        "Günəş",
        "Ay",
        "Günəş",
        "Ay",
        "Yağış",
        "qar",
        "Suda",
        "Havada",
        "Quruda",
        "Ağ",
        "Yaşıl",
        "Mavi",
        "Sarı",
        "Narıncı",
        "Qırmızı",
        "Qara",
        "Ağ",
        "İnək",
        "toyuq",
        "pişik",
        "it",
        "İnək",
        "Donuz",
        "Bıçaq",
        "Qələm",
        "Sabun",
        "Diş fırçası",
        "Yataq",
        "Qaşıq",
        "kubok",
        "Bax",
        "Hökmdar",
        "Termometr",
        "Tərəzilər",
        "Hava",
        "Gözlər",
        "Qulaqlar",
        "Ayaqlar",
        "Lampa",
        "Qızdırıcı"
    ]

    tt_answers: list[str] = [
        "Ир",
        "Кояш",
        "Ай",
        "Кояш",
        "Ай",
        "Яңгыр",
        "Кар",
        "Суда",
        "Airавада",
        "Landирдә",
        "Белый",
        "Яшел",
        "Зәңгәр",
        "Сары",
        "Алсу",
        "Кызыл",
        "Кара",
        "Белый",
        "Сыер",
        "Тавык",
        "Мәче",
        "Эт",
        "Сыер",
        "Дуңгыз",
        "Пычак",
        "Каләм",
        "Сабын",
        "Теш щеткасы",
        "Карават",
        "Кашык",
        "Кубок",
        "Карагыз",
        "Хаким",
        "Термометр",
        "Тараза",
        "Airава",
        "Күзләр",
        "Колаклар",
        "Аяклар",
        "Лампа",
        "Aterылыткыч"
    ]

    set_questions = []
    set_answers = []

    def get_questions(language: str) -> tuple[list[str], list[str]]:

        if len(BilingTest.set_questions) > 0 and len(BilingTest.set_answers) > 0:
            BilingTest.set_questions.clear()
            BilingTest.set_answers.clear()

        if language == 'eng-rus':
            while len(BilingTest.set_questions) < 3:
                while len(BilingTest.set_questions) < 3:    
                    choice = random.choice(['eng', 'rus'])
                    if choice == 'eng':
                        
                        q = random.choice(BilingTest.eng_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.eng_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.rus_answers[BilingTest.eng_questions.index(q)])
                    else:

                        q = random.choice(BilingTest.rus_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.rus_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.eng_answers[BilingTest.rus_questions.index(q)])
        elif language == 'rus-ka':
            while len(BilingTest.set_questions) < 3:
                while len(BilingTest.set_questions) < 3:
                    choice = random.choice(['ka', 'rus'])
                    if choice == 'ka':
                        
                        q = random.choice(BilingTest.ka_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.ka_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.rus_answers[BilingTest.ka_questions.index(q)])
                    else:

                        q = random.choice(BilingTest.rus_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.rus_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.ka_answers[BilingTest.rus_questions.index(q)])      
        elif language == 'rus-tt':
             while len(BilingTest.set_questions) < 3:
                while len(BilingTest.set_questions) < 3:
                    choice = random.choice(['tt', 'rus'])
                    if choice == 'tt':
                        
                        q = random.choice(BilingTest.tt_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.tt_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.rus_answers[BilingTest.tt_questions.index(q)])
                    else:

                        q = random.choice(BilingTest.rus_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.rus_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.tt_answers[BilingTest.rus_questions.index(q)])  
        elif language == 'rus-az':
            while len(BilingTest.set_questions) < 3:
                while len(BilingTest.set_questions) < 3:
                    choice = random.choice(['az', 'rus'])
                    if choice == 'az':

                        q = random.choice(BilingTest.az_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.az_questions)
                            
                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.rus_answers[BilingTest.az_questions.index(q)])
                    else:
                        
                        q = random.choice(BilingTest.rus_questions)
                        while q in BilingTest.set_questions:
                            q = random.choice(BilingTest.rus_questions)

                        BilingTest.set_questions.append(q)
                        BilingTest.set_answers.append(BilingTest.az_answers[BilingTest.rus_questions.index(q)])  

        return BilingTest.set_questions, BilingTest.set_answers
        
    def get_random_answer(correct_answer) -> list[str]:
        random_answers = []
        while len(random_answers) < 2:
            if correct_answer in BilingTest.eng_answers:
                a = random.choice(BilingTest.eng_answers)
            elif correct_answer in BilingTest.ka_answers:
                a = random.choice(BilingTest.ka_answers)
            elif correct_answer in BilingTest.rus_answers:
                a = random.choice(BilingTest.rus_answers)
            elif correct_answer in BilingTest.tt_answers:
                a = random.choice(BilingTest.tt_answers)
            elif correct_answer in BilingTest.az_answers:
                a = random.choice(BilingTest.az_answers)

            if a not in random_answers and a not in BilingTest.set_questions:
                random_answers.append(a)
        return random_answers
    
