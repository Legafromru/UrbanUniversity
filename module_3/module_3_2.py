def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender):
    #Если строки  и  не содержит  или не оканчивается на ".com" / ".ru" / ".net", то  вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender: #Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com": #Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('hello','university.help@gmail')
send_email('hello','university.help@gmail.com')
send_email('hello','university@mail.com')
send_email('hello','university@mail.com', sender='vasiliy@mail.ru')