def send_email(message, recipient, sender="university.help@gmail.com"):# Функция для работы 
     
     # Логика действия 
     if not (("@" in sender) and (("@" in recipient) or (recipient.endswith(".com", ".ru", ".net")))): #задаём условие при ктором будет выполнятся то или иное действие

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

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')


