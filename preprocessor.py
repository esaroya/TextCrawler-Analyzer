# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:51:27 2020

@author: eishe
"""
import io
import csv
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
"""
    Preprocess the data by:
"""

##to save, sentences, we need to store the word array as an 2d array of words and sentences
#potentially even paragraphs
#first break into sentences. 
#
#
#
#
class preprocessor:
    ## Mutliple model forms
    ## bag of words pre and post processed
    ## lines of sentences
    ##  
    
    def __init__(self, text):
        self.text = text
        self.word_sent_Tokens = []
        self.processedTokens = []
        self.sentences = []
        self.tokenize()
    
    def preprocess(self):
        self.tokenize()
        self.pos_tagger()
        
        
    def postprocess(self):
        stop = set(stopwords.words('english'))
        self.processedTokens = [word for word in self.word_sent_Tokens if word not in stop]
        porter = nltk.PorterStemmer()
        self.processedTokens = [porter.stem(t) for t in self.word_sent_Tokens]
        self.sentTokens = [self.deCapitalize(sent) for sent in self.sentTokens]
        
    def removeStopWords(self, text=''):  
        stop = set (stopwords.words('english'))
        returnText = ''
        if text == '':
            rawtokens = self.wordTokens
            self.wordTokens = [word for word in rawtokens if word not in stop]
            return None
        else:
            for word in text.split():
                if word not in stop:
                    returnText = returnText + word + ' '
            return returnText
        
    def pos_tagger(self):
            self.sentences = [self.pos_tag(sent) for sent in self.sentences] 

    
    def deCapitalize(self, text):
        newText = ''
        for word in text.split():
            newText = newText + word[0].lower() + word[1:] + ' '
            
            
    def tokenize(self, text=''):
        sentences=[]
        words = []
        
        if text=='':
            self.sentences = sent_tokenize(self.text)
            word_sent_Tokens = [word_tokenize(sent) for sent in self.sentences]
            return None
        else:
            sentences = sent_tokenize(text)
            words = [word_tokenize(sent) for sent in sentences]
            return words
        
  """
    def wordTokenize(self, text=''):
        wordTokens = []
        if text=='':
            wordTokens = word_tokenize(self.text)
        else:
            wordTokens = word_tokenize(text)
        
        return wordTokens
    
    def sentTokenize(self, text=''):
        sentTokens = []
        if text == '':
            sentTokens = sent_tokenize(self.text)
        else:
            sentTokens = sent_tokenize(text)
        
        return sentTokens
    
"""  

