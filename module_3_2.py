def send_email(message, recipient,*, sender="university.help@gmail.com"):# Функция для работы 
     
     # Логика действия 
     if "@" not in sender or "@" not in recipient or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")) or not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")): #задаём условие при ктором будет выполнятся то или иное действие

        # действия
        print("Невозможно отправить письмо с адреса <" + sender + "> на адрес <" + recipient + ">.")
        return
     elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
     elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <" + sender + "> на адрес <" + recipient + ">.")
        return
     else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <" + sender + "> на адрес <" + recipient + ">.")
        return
     # Обработка функции

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


