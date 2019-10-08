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
        if word in dict_f():
            value = dict_f[word]
            dict_f[word] = value + 1
        else:
            dict_f[word] = 1
    return dict_f




def filter_stop_words(freq_dict, stop_words: tuple) -> dict:
    dict_f_s = {}
    if freq_dict is not None and stop_words is not None:
        for key, value in freq_dict.items():
            if key == str(key):
                if key not in stop_words:
                    dict_f_s.update({key: value})
    return dict_f_s


def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies) 
    return tuple(sortedFrequencies[i] for i in range(top_n))

