# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:22:00 2020

@author: eishe
"""
from nltk.util import ngrams

import preprocessor
from collections import Counter, defaultdict
from nltk import word_tokenize, sent_tokenize

class ContentAnalyzer:
    
    def __init__(self):
        self.nGramModel = defaultdict(lambda: defaultdict(lambda: 0))
     
    def generateParsetree():
        pass
    
    def topNWords(processedtext, n):
        wordDict = {}
        for word in processedtext:
            if word in wordDict:
                wordDict[word]=+1
            else:
                wordDict = 1
        sortedWords = sorted(wordDict, key = wordDict.get, reverse = True)
        return sortedWords[:n]
    
    def sentimentAnalysis():
        pass
    
    def averageWordLength():
        pass
    
    def ngram(self, n, text):
        sentList = sent_tokenize(text)
        for sent in sentList:
            wordsInSent = word_tokenize(sent)
            ngramList = ngrams(wordsInSent, n) #, pad_right=True, pad_left=True)
            for w in ngramList:
                #if w[0] is not None:
                self.nGramModel[w[:n-1]][w[n-1]] +=1
        
        for wKey in self.nGramModel:
            total = float(sum(self.nGramModel[wKey].values()))
            for value in self.nGramModel[wKey]:
                self.nGramModel[wKey][value] /= total
                
        
    #
    def wordCount(word, lis):
        count = 0
        for w in lis:
            if w is word:
                count+=1
                
    
    def categorize():
        pass
    def politicalBias():
        pass
    
