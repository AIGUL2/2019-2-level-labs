def calculate_frequences(str):
    dict = {} #словарь
    word = '' #переменная для очередного слова
    for i in range(len(str)): #проходим по всем буквам/символам
        letter = str[i].lower() #переводим в нижний регистр
        if letter.isalpha(): #если это буква, а не символ или че то другое
            word = word+letter #добавляем букву в слово
        elif len(word) != 0: #если же  очередой символ не является буквой, значит это конец слова
            if word in dict:
                dict[word]+=1 #то увеличиваем "встречаемость"
            else: # иначе добавляем слово в словарь и ставим встречаемость =1
                dict[word]=1
            word = '' # обнуляем переменную под очередное слово
    return dict



def filter_stop_words(frequencies,stop_words):
    dictcopy = frequencies.copy()
    for word in stop_words:
        if word in dictcopy:
            del dictcopy[word]
    return dictcopy


def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies) # тут проверка, меньше ли число слов, которое мы хотим получить, чем вообще длина словаря, если да, то ничего не делаем, иначе - возвращаем весь словарь
    return tuple(sortedFrequencies[i] for i in range(top_n)) # создаем tuple из словаря (внутри находится "генератор", прочитай в инетике чо ето такое)


string = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stopWords = ('lol','kek','cheburek','meet')
dict = calculate_frequences(string)
dictFiltred = filter_stop_words(dict,stopWords)
topwords = (get_top_n(dict,5))

