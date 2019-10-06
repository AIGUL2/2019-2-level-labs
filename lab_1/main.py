def calculate_frequences(text):
    dict_f = {}
    word = ''
    text = text.lower()
    for i in text:
        if i.isalpha() or i == ' ':
              word += i
        else:
            word = ''
    word_new = word.split()
    for i in word_new:
        if i in dict_f:
            word_counter = word_new.count(i)
            dict_f[i] = word_counter
    return dict_f

def filter_stop_words(frequencies, stop_words):
    spisok = {}
    if type(frequencies)== dict and type(stop_words)== tuple:
        for k, i in frequencies.items():
            if k not in stop_words:
                spisok[k] = i
        return spisok


def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=for_sort, reverse=True)
    ad_element = []
    if len(sortedFrequencies)>top_n:
        top_n = top_n
    else:
        len(sortedFrequencies)
    for i in range(top_n):
        word = sortedFrequencies[i]
        ad_element.append(word)
    return tuple(ad_element)

def for_sort(n):
    return n[1]
print(get_top_n({'cat': 2, 'dog':3, 'swan':6}, 2))


text = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stop_words = ('lol','kek','cheburek','meet')

