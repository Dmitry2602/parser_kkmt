from bs4 import BeautifulSoup as Bs  # pip install beautifulsoup4
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service  # pip install webdriver-manager
import time
import pandas as pd  # pip install pandas
from selenium.webdriver.common.by import By
from tkinter import *  # pip install Tkinter
from tkinter import ttk


# Функция графического интерфейса
def GUI():
    def click():  # Функция, которая передает переменным выбранные значения
        global group, sem, lesson
        group = take_group.get()
        sem = take_sem.get()
        lesson = take_subj.get()
        window.destroy()  # После завершения окно автоматически закрывается

    # Создаем интерфейс нашего меню
    window = Tk()

    window["bg"] = "#f7f7f7"
    window.title("Парсер сайта")
    window.geometry("500x500+400+90")
    window.resizable(width=False, height=False)

    canvas = Canvas(window, height=500, width=500)
    canvas.pack()

    frame = Frame(window, bg='#f7f7f7')
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

    # Списки, которые будут использоваться в выпадающих окнах
    lst = ["П1-20", "П2-20", "П3-20", "П1-19", "П2-19", "П3-19", "П1-18", "П2-18", "П1-17", "П2-17"]
    se = ["1", "2", "3", "4", "5", "6", "7", "8"]
    subject = ['Архитектура компьютерных систем', 'Астрономия', 'Безопасность жизнедеятельности',
               'Документирование и сертификация', 'Иностранный язык',
               'Инструментальные средства разработки программного обеспечения',
               'Инфокоммуникационные системы и сети', 'Информатика', 'Информационные технологии', 'История',
               'Литература',
               'Математика', 'Обществознание', 'Операционные системы', 'Основы безопасности жизнедеятельности',
               'Основы предпринимательства', 'Основы программирования', 'Основы философии', 'Основы экономики',
               'Правовое обеспечение профессиональной деятельности', 'Производственная практика', 'Психология общения',
               'Разработка и администрирование баз данных',
               'Разработка программных модулей программного обеспечения для компьютерных систем',
               'Русский язык', 'Системное программирование', 'Теория алгоритмов',
               'Теория вероятностей и математическая статистика',
               'Технические средства информатизации', 'Технология разработки и защиты баз данных',
               'УП.04.01 Учебная практика',
               'Участие в интеграции программных модулей', 'Учебная практика', 'Физика', 'Физическая культура',
               'Химия', 'Элементы высшей математики', 'Элементы математической логики',
               'Эффективное поведение на рынке труда']

    paint_group = Label(frame, text='Выберите группу:', bg='#f7f7f7', font='Calibri 11')  # Делаем спровождающую подпись
    paint_group.pack()

    take_group = ttk.Combobox(frame, value=lst)  # Создаем выпадающий список с группами
    take_group.pack()

    paint_group = Label(frame, text='Выберите семестр:', bg='#f7f7f7',font='Calibri 11')  # Делаем спровождающую подпись

    paint_group.pack()

    take_sem = ttk.Combobox(frame, value=se)  # Создаем выпадающий список с семестрами
    take_sem.pack()

    paint_group = Label(frame, text='Выберите предмет:', bg='#f7f7f7',font='Calibri 11')  # Делаем спровождающую подпись

    paint_group.pack()

    take_subj = ttk.Combobox(frame, width=50, value=subject)  # Создаем выпадающий список с предматами
    take_subj.pack()

    button = ttk.Button(frame, text="Click", command=click)  # Создаем кнопку для выполнения функции Click()
    button.pack()

    window.mainloop()


# Функция, которая создает ссылку по введенным данным
def take_url():
    global url_parse, subj_1, subj_2, subj_3, subj_4, subj_5, subj_6, subj_7  # subj_8

    # Перевод группы для корректной работы ссылки
    dict = {"П1-20": "%D0%9F1-20", "П2-20": "%D0%9F2-20", "П3-20": "%D0%9F3-20",
            "П1-19": "%D0%9F1-19", "П2-19": "%D0%9F2-19", "П3-19": "%D0%9F3-19",
            "П1-18": "%D0%9F1-18", "П2-18": "%D0%9F2-18", "П1-17": "%D0%9F1-17", "П2-17": "%D0%9F2-17"}

    # Предметы по семестрам и их код в портале
    subj_1 = {"Иностранный язык": "8190", "Информатика": "8192", "История": "8189", "Литература": "7948",
              "Математика": "8191", "Обществознание": "8299", "Основы безопасности жизнедеятельности": "7953",
              "Русский язык": "58", "Физика": "100", "Физическая культура": "8193", "Химия": "113"}

    subj_2 = {"Астрономия": "8754", "Иностранный язык": "8190", "Информатика": "8192", "История": "8189",
              "Литература": "7948", "Математика": "8191", "Обществознание": "8299",
              "Основы безопасности жизнедеятельности": "7953", "Русский язык": "58", "Физика": "100",
              "Физическая культура": "8193", "Химия": "113"}

    subj_3 = {"Иностранный язык": "56", "Информационные технологии": "379", "История": "6193",
              "Операционные системы": "179",
              "Основы программирования": "8038", "Психология общения": "571", "Физическая культура": "57",
              "Элементы высшей математики": "8031", "Элементы математической логики": "8032"}

    subj_4 = {"Архитектура компьютерных систем": "8035", "Иностранный язык": "56", "Информационные технологии": "379",
              "Основы программирования": "8038", "Правовое обеспечение профессиональной деятельности": "6674",
              "Технические средства информатизации": "8036", "УП.04.01 Учебная практика": "8764",
              "Физическая культура": "57", "Элементы высшей математики": "8031",
              'Эффективное поведение на рынке труда': "8685"}

    subj_5 = {"Безопасность жизнедеятельности": "33", "Иностранный язык": "56", "Основы предпринимательства": "6988",
              "Основы экономики": "8039", "Системное программирование": "8041", "Теория алгоритмов": "8195",
              "Теория вероятностей и математическая статистика": "267", "Учебная практика": "691",
              "Физическая культура": "57"}

    subj_6 = {"Иностранный язык": "56", "Инфокоммуникационные системы и сети": "6899",
              "Прикладное программирование": "8042", "Производственная практика": "5000",
              "Разработка программных модулей программного обеспечения для компьютерных систем": "8040",
              "Учебная практика": "691", "Физическая культура": "57"}

    subj_7 = {"Документирование и сертификация": "8052", "Иностранный язык": "56", "Основы философии": "7957",
              "Инструментальные средства разработки программного обеспечения": "8051",
              "Производственная практика": "5000",
              "Разработка и администрирование баз данных": "8044", "Технология разработки и защиты баз данных": "8046",
              "Технология разработки программного обеспечения": "8050",
              "Участие в интеграции программных модулей": "8049", "Учебная практика": "691",
              "Физическая культура": "57"}

    # subj_8 = {"": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": ""}

    # if sem == "8":
    # url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_8[lesson]}&sem={sem}"
    try:
        if sem == "7":  # Проверям какой у нас семестр и выводим соотвествующий ему словарь с предметами
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_7[lesson]}&sem={sem}"
        elif sem == "6":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_6[lesson]}&sem={sem}"
        elif sem == "5":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_5[lesson]}&sem={sem}"
        elif sem == "4":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_4[lesson]}&sem={sem}"
        elif sem == "3":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_3[lesson]}&sem={sem}"
        elif sem == "2":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_2[lesson]}&sem={sem}"
        elif sem == "1":
            url_parse = f"https://ies.unitech-mo.ru/journal?group={dict[group]}&subj={subj_1[lesson]}&sem={sem}"
    except KeyError:
        print("Вы указали неправильные данные :(")
        raise SystemExit


# Фукция для получения html-разметки и дальнейший ее парсинг
def parse_url():
    LOGIN = "bulyuchevda.20"  # логин от портала
    PASSW = "20042602DImad"  # пароль от портала

    try:
        # Webriver нужно поместить в одну директорию вместе с кодом. В Service указать абсолютный путь,
        # где лежит Webdriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=Service('C:\\Users\\dimab\\Study\\kkmt\\chromedriver.exe'), options=options)
        driver = webdriver.Chrome(service=Service("C:\\Users\\dimab\\Study\\kkmt\\chromedriver.exe"))
        driver.get("https://ies.unitech-mo.ru/")


        # Нажимаем на кнопку входа
        but = driver.find_element(By.CLASS_NAME, "user_session_data")
        but.click()

        # Переходим на поле с логином и вводим туда данные
        login = driver.find_element(By.NAME, "login")
        login.click()
        login.send_keys(LOGIN)
        time.sleep(1)

        # Переходим на поле с паролем и вводим туда данные
        password = driver.find_element(By.NAME, "pass")
        password.click()
        password.send_keys(PASSW)
        time.sleep(1)

        # Нажимаем и проходим авторизацию
        come_in = driver.find_element(By.ID, "main_login_link")
        come_in.click()
        time.sleep(2)

        driver.get(url_parse)  # Переходим по созданной ссылке
        html = driver.page_source  # Берем всю разметку со страницы

        time.sleep(2)

        driver.quit()  # Выходим из браузера
    except NameError:
        print("Вы указали неверные данные")
        raise SystemExit

    head = ["Список группы:"]  # Список для дат
    main = []  # Список для фамилий и оценок

    try:
        soup = Bs(html, "lxml")
        search_head = soup.find("table", class_="scorestable scorestable_clone_top").find("thead").findAll("th")
        search_main = soup.find("table", class_="fl_left scorestable").findAll("td")

        # С помощью цикла for, преобразуем текст из разметки и записываем его в список head, в котором будут хранится даты
        for i in search_head:
            s = i.text.strip()  # Убираем переносы и табулюцию
            head.append(s)

        # Убираем последний максимальный балл за пару
        head = [x[:-1] for x in head]

        # С помощью цикла for, преобразуем текст из разметки и записываем его в список main, в котором будут хранится оценки
        for i in search_main:
            q = i.text.strip()  # Убираем переносы и табулюцию
            main.append(q)

        # Убираем ссылки на личные сообщения
        main = [i.replace("\xa0лс", "") for i in main]

        full = head + main  # соединяем наши списки с оценками и датами
        finish = []  # Выделяем пустой список для переноса в Excel
        counter = 0  # Счетчик для перехода на другую строчку

        for i in range(len(head)):  # цикл for для экспорта нашей информации в список
            temp = []  # Промежуточный список для переноса в главный список - finish
            temp = full[slice(counter, len(full), len(head))]  # slice(start, stop, step)
            # Добавляем строку и на выходе получаем вложенный список, с которым можно в строку вывести в Excel
            finish.append(temp)
            counter += 1

        # Перевод нашей информации в Excel
        df = pd.DataFrame(data=finish)
        df = df.transpose()
        # Указываем абсолютный путь места, где будет сохраняться файл
        df.to_excel(f"C:\\Users\\dimab\\Study\\kkmt\\Excel\\{group}_{lesson}_{sem}.xlsx", index=False, header=False)
    except AttributeError or NameError:
        print("Тут какая-то ошибочка :(")
        raise SystemExit


# Главная функция, которая собирает все вместе
def parse_main():
    GUI()
    take_url()
    parse_url()


if __name__ == "__main__":  # Запускаем parse_main
    parse_main()
