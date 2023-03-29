"""Домашнее задание по уроку 2"""


class CssSelectors():
    test_stage_logo = '[id=main_logo]' #1.Логотип “Test Stage”
    button_quit = '[href = "/logout"]' #2.Кнопка “Выход”
    modals_window = '.menu-list :nth-child(7)' # 3.Ссылка в боковом меню “Модальные окна”
    surname = '[name="surname"]' # 4.Текстовое поле “Фамилия”
    radio_button = '#age2' # 5.Радиокнопка “Тестировщик автоматизатор”
    checkboks = '[id = "lang4"]' # 6.Чекбокс “Go” в блоке языки программирования
    confirm = '.button.is-block' # 7.Кнопка “Подтвердить”
    middle = '[id=lvl] :nth-child(3)' #Опция Middle в блоке “Уровень квалификации”
    confirm_three_buttons = '[onclick="confirm_func()"]' #кнопка Confirm
    last_button = '.box :nth-child(10)' #последняя кнопка Выбрать


class Xpaths:
    test_stage_logo = '//img'  # 1.Логотип “Test Stage”
    button_quit = '//a[@href="/logout"]'  # 2.Кнопка “Выход”
    modals_window = '//ul//a[@href="/three_buttons"]'  # 3.Ссылка в боковом меню “Модальные окна”
    surname = '//input[@name="surname"]'  # 4.Текстовое поле “Фамилия”
    radio_button = '//input[@value="auto"]'  # 5.Радиокнопка “Тестировщик автоматизатор”
    checkboks = '//input[@value="Go"]'  # 6.Чекбокс “Go” в блоке языки программирования
    confirm = '//button[contains(@class, "button")]'  # 7.Кнопка “Подтвердить”
    middle = '//option[text()="Middle"]'  # Опция Middle в блоке “Уровень квалификации”
    confirm_three_buttons = '//button[2]'  # кнопка Confirm
    last_button = '//button[4]'  # последняя кнопка Выбрать

