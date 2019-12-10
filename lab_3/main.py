"""
Labour work #3
Building an own N-gram model
"""

import math

if __name__ == 'main':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:

    def __init__(self):
        self.i = 0
        self.storage = {}

    def put(self, word: str) -> int:
        if word in self.storage.keys():
            return self.storage[word]
        if word is not None and word != '' and str(word).isalpha():
            self.storage[word] = self.i
            self.i += 1
            return self.i - 1

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        for word, number in self.storage.items():
            if number == id:
                return word
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if corpus is not None and type(corpus) == tuple:
            for word in corpus:
                self.storage[word] = self.i
                self.i += 1


class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence is not None and type(sentence) == tuple:
            for ind in range(len(sentence) - self.size + 1):
                list_ind = []
                list_ind.append(sentence[ind])
                for i in range(self.size - 1):
                    k = ind + 1
                    list_ind.append(sentence[k])

                if tuple(list_ind) in self.gram_frequencies.keys():
                    self.gram_frequencies[tuple(list_ind)] += 1
                else:
                    self.gram_frequencies[tuple(list_ind)] = 1

    def calculate_log_probabilities(self):
        for gramm in self.gram_frequencies.keys():
            sum_gramm = 0
            for gramm2 in self.gram_frequencies.keys():
                if gramm[0] == gramm2[0]:
                    sum_gramm += self.gram_frequencies[gramm2]
            self.gram_log_probabilities[gramm] = math.log(self.gram_frequencies[gramm] / sum_gramm)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix is None or len(prefix) != 1 or type(prefix) != tuple:
            return []
        pred_sent = [prefix[0]]
        flag = True
        while flag:
            max_prob = -1000
            app_flag = False
            for gramm in self.gram_log_probabilities.keys():
                if gramm[0] == prefix[0]:
                    app_flag = True
                    if max_prob < self.gram_log_probabilities[gramm]:
                        max_prob = self.gram_log_probabilities[gramm]
                        ind = gramm[1]

            if app_flag == False:
                flag = False
            else:
                pred_sent.append(ind)
                prefix = [ind]
        return pred_sent


def encode(storage_instance, corpus) -> list:
    for sent in corpus:
        for word in sent:
            word = storage_instance[word]


def split_by_sentence(text: str) -> list:
    mat = []

    bad_chars = ["'", '$', '#', '&', '%', '^', '*', '(', ')', '@', ',']
    if text is not None:
        for ch in bad_chars:
            text = text.replace(ch, '')

    if text is None or text == '' or text.find('.') == -1:
        return mat
    text = text.replace('!', '.').replace('?', '.').split('\n')
    for ind in range(len(text)):
        sents = text[ind].split('.')
        for i in range(len(sents)):
            words = sents[i].split()
            if len(words) > 0:
                if words[0][0].islower():
                    sent_list = mat[-1]
                    for word in words:
                        sent_list.insert(-1, word.lower())
                else:
                    sent_list = ['<s>']
                    for word in words:
                        sent_list.append(word.lower())
                    sent_list.append('</s>')
                    mat.append(sent_list)
    return mat
