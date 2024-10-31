def single_root_words(root_word, *other_words): #Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
    same_words = [] #Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    for i in other_words: #При помощи цикла for переберите предполагаемо подходящие слова.
        if root_word.upper() in i.upper() or i.upper() in root_word.upper():
            same_words.append(i)
    print(f'Однокоренными к слову "{root_word}" являются {same_words}')
    #return same_words

single_root_words('сад', 'садоВник', 'сАДик', 'Сады', 'судьБа', 'седой')
single_root_words('дыМ', 'Дымный', 'сараЙ', 'дымить', 'дЫмоК', 'еда')