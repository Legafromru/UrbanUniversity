calls = 0
def count_calls(): #Функция count_calls подсчитывающая вызовы остальных функций
    global calls
    calls += 1
def string_info(string): #Функция string_info принимает аргумент - строку и возвращает кортеж из: длины
    # этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    print (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):  #Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    count_calls()
    print(string.upper() in [s.upper() for s in list_to_search])
string_info('жАра')
string_info('Fuse')
string_info('what about my money?')
is_contains('string', ['RinG', 'WING', 'strong'])
is_contains('abCDe', ['ABcdE', 'AbCdE', 'qwerty'])
print('Количество вызовов функций ', calls)