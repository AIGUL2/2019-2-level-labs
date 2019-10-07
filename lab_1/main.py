def calculate_frequencies(text: str) -> dict:
    dict = {}
    word = ''
    if type(text) == str:
        for i in range(len(text)):
            letter = text[i].lower()
            if letter.isalpha():
                word = word + letter
            elif len(word) != 0:  # если же  очередой символ не является буквой, значит это конец слова
                if word in dict:
                    dict[word] += 1
                else:  # иначе добавляем слово в словарь и ставим встречаемость =1
                    dict[word] = 1
                word = ''
    return dict



def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    if stop_words is None or frequencies is None:
        return {}
    for key in stop_words:
        if key in frequencies:
            frequencies.pop(key)

    result_dict = {}
    for key, value in frequencies.items():
        if type(key) is str:
            result_dict[key] = value

    return result_dict


def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies) # тут проверка, меньше ли число слов, чем  длина словаря
    return tuple(sortedFrequencies[i] for i in range(top_n))

string = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stopWords = ('lol','kek','cheburek','meet')
dict = calculate_frequencies(string)
dictFiltred = filter_stop_words(dict,stopWords)
topwords = (get_top_n(dict,5))

