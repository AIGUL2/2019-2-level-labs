def calculate_frequencies(text: str) -> dict:
    dict_f = {}
    if text == "" or text is None:
        return dict_f
    text = str(text)
    text_lower = text.lower()
    for a in text_lower:
        if not a.isalpha():
            text_lower = text_lower.replace(a, ' ')
    split = text_lower.split()
    for word in split:
        word = word.lower()
        if word  in dict_f():
            value = dict_f[word]
            dict_f[word] = value + 1
        else:
            dict_f[word] = 1
    return dict_f




def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    if stop_words is None or frequencies is None:
        return {}
    for word in stop_words:
        if word in frequencies:
            frequencies.pop(word)
    result_dict = {}
    for word, value in frequencies.items():
        if type(word) is str:
            result_dict[word] = value

    return result_dict


def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies) # тут проверка, меньше ли число слов, чем  длина словаря
    return tuple(sortedFrequencies[i] for i in range(top_n))

