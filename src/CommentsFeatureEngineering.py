# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:29:00 2018

@author: Guus
"""

import spacy
import pandas as pd

CryptoComm = pd.read_csv('cryptocurrency_Top_020118.csv', encoding='utf-8')

nlp = spacy.load('en_core_web_sm')

CryptoComm['Parsed'] = CryptoComm['CommentText'].apply(nlp)

