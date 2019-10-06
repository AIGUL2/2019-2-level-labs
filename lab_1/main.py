def calculate_frequences(str):
    dict = {} #словарь
    word = ''
    for i in range(len(str)):
        letter = str[i].lower()
        if letter.isalpha():
            word = word+letter
        elif len(word) != 0:
            if word in dict:
                dict[word]+=1
            else:
                dict[word]=1
            word = ''
    return dict

def filter_stop_words(frequencies,stop_words):
    if type(frequencies) == dict and type(stop_words) == tuple:
        dictcopy = frequencies.copy()
        for word in stop_words:
            if word in dictcopy:
                del dictcopy[word]
        return dictcopy



def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies)
    return tuple(sortedFrequencies[i] for i in range(top_n))

string = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stopWords = ('lol','kek','cheburek','meet')

dict = calculate_frequences(string)
dictFiltred = filter_stop_words(dict,stopWords)
topwords = (get_top_n(dict,5))