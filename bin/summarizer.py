# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:13:42 2020

@author: rahul
"""


import yaml
import numpy as np

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config = yaml.load(fl)
        
    def loadDocs(self,filePath):
        with open(filePath,'r') as fl:
            text = fl.read()
        return text
    
    def splitSentences(self,text):
        """
        Split paragraph into an array of sentences
        -------------
        Input:
            text: string
        Output:
            sentences: a list of string
        -------------
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent
    
    def findsentlen(self,text):
        return text.split()
    
    def findsentlenarray(self,sentences):
        return[self.findsentlen(sent) for sent in sentences ]
    
    def findtopsentence(self,sentlents,sentences,n):
        sortedidx =np.argsort(sentlents)
        top3idx = sortedidx[-n:]
        top3sentences =[sentences[i] for i in top3idx]
        return top3sentences
    
    def findsumm(self):
        filePath = self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        sentences = self.splitSentences(text)
        firstSent,restOfSent =self.groupSentences(sentences)
        sentLent =self.findsentlenarray(restOfSent)
        topsentence = self.findtopsentence(sentLent,restOfSent,self.config['sentence_num'])
        allsentences =[firstSent] + topsentence
        summary = ' '.join(allsentences)
        return summary
        

summarizeObj = SummarizeDoc()
summarizeObj.loadConfig()