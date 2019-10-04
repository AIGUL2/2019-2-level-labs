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

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict::
    spisok = {}
    if type(frequencies)== dict and type(stop_words)== tuple:
    for k,i in frequencies.items():
        if k not in stop_words:
            spisok[k] = i
    return spisok

def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies)
    return tuple(sortedFrequencies[i] for i in range(top_n))


text = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stop_words = ('lol','kek','cheburek','meet')
topwords = (get_top_n(dict,5))



  ''' 0.5 done work of 4 exercise'''
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