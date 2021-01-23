import numpy as np
from math import log
from collections import Counter


class bm25(object):

    def __init__(self, index):
        self.index = index
        self.doc_len = []
        self.tokens = []
        self.freq = []
        self.idf = {}

        for doc in self.index:
            tokens = self.standard_tokenizer(doc)
            self.doc_len.append(len(tokens))
            self.tokens += tokens
            self.freq.append(Counter(tokens))
        self.tokens = list(dict.fromkeys(self.tokens))

        for token in self.tokens:
            doc_count = 0
            for doc in self.freq:
                if doc[token] > 0:
                    doc_count += 1
            
            self.idf[token] = log(1 + (len(self.doc_len) - doc_count + 0.5) / (doc_count + 0.5))


    def standard_tokenizer(self, doc):
        return doc.split(" ")


    def get_scores(self, query):
        k = 2.0
        b = 0.75
        scores = []
        for i in range(0, len(self.index)):
            tf = self.freq[i][query]
            idf = self.idf[query]
            scores.append(idf*(tf * (k + 1) / ((tf + k) * (1 - b + b * (self.doc_len[i]/np.mean(self.doc_len))))))

        return scores


    def search(self, query):
        result = {}
        try:
            scores = self.get_scores(query)
        except:
            return result
        for n, s in enumerate(scores):
            result[n] = s
        result = sorted(result.items(), key=lambda x : x[1], reverse=True)

        return result






