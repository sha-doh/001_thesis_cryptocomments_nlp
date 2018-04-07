# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:51:50 2018

@author: Guus
"""

import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

CryptoComments = {'Title':[],
                  'PostScore':[],
                  'PostTime':[],
                  'Flair':[],
                  'ParentID':[],
                  'CommentID':[],
                  'CommentTime':[],
                  'CommentScore':[],
                  'CommentText':[]
                  }

CryptoComments = {}

CryptoComments['Tilte'] = "Test2"

df = pd.DataFrame(web_stats)

print(df)


