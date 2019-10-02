"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""

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


line =  'Mary was quick to realize that she had won the prize that was a desired thing that everyone wanted'
getWordsFrequence(line)


"""проверка github"""
