"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
def calculate_frequences(text):
    dict_f = {}
    word = ''
    text = text.lower()
    for i in text:
        if i.isalpha() or i == ' ':
              word += i
    word_new = word.split()
    for i in word_new:
        if i in dict_f:
            word_counter = word_new.count(i)
            dict_f[i] = word_counter
    return dict_f


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:

    """    Removes all stop words from the given frequencies dictionary

    """
    spisok = {}
    if type(frequencies)== dict and type(stop_words)== tuple:
    for k, i in frequencies.items():
        if k not in stop_words:
            spisok[k] = i
    return spisok

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular wordss
    """
    pass
"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""



text_=  '''Mary was quick to realize that she had won the prize that was a desired thing that everyone wanted'''
stop_words = ('i', 'am', 'a', 'human')
top_n = 2

def getWordsFrequence(line):
    dict = {} #словарь
    stopWords=['lol','kek','cheburek','of']
    word = ''
    for i in range(len(line)):
        letter = line[i].lower()
        if str.isalpha(letter):
            word = word+letter
        elif len(word) != 0:
            if word in dict:
                dict[word]+=1
            elif word not in stopWords:
                dict[word]=1
            word = ''

    sortedByFrequence = sorted(dict,key=dict.get,reverse=True)
    for i in sortedByFrequence:
        print (i,dict[i],sep=':')

    print('the most frequent word is: ',sortedByFrequence[0])
    return dict

line = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
getWordsFrequence(line)
