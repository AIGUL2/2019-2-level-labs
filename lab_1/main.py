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
    dictcopy = frequencies.copy()
    for word in stop_words:
        if word in dictcopy:
            del dictcopy[word]
    return dictcopy

def get_top_n(frequencies, top_n):
    sortedFrequencies = sorted(frequencies, key=frequencies.get, reverse=True)
    top_n = top_n if len(sortedFrequencies)>top_n else len(sortedFrequencies)
    return tuple(sortedFrequencies[i] for i in range(top_n))

def read_from_file(path_to_file, lines_limit):
    with open(path_to_file,"r") as myfile:
        str = ''
        for i in range (lines_limit):
            str = str + myfile.readline()
    return str

def write_to_file(path_to_file, content):
    with open(path_to_file,"w") as myfile:
            myfile.writelines(map(lambda word: word+'\n',content))
    return True

string = "Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael."
stopWords = ('lol','kek','cheburek','meet')

dict = calculate_frequences(string)
dictFiltred = filter_stop_words(dict,stopWords)
topwords = (get_top_n(dict,5))
fromFile = get_top_n(calculate_frequences(read_from_file("data.txt",5)),3)
write_to_file("report.txt",fromFile)