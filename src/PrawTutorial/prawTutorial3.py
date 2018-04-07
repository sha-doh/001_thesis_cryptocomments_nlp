# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:32:50 2018

@author: Guus
"""

import praw

reddit = praw.Reddit(client_id = 'JLb3NDSQF7bu1Q',
	client_secret = 'S2iMASU9ePl6LxOhhs9D5pxBs2Y',
	username = 'GuusStaaf38',
	password = 'guus515838',
	user_agent = 'prawtutorialv1')

subreddit = reddit.subreddit('cryptocurrency')

hot_python = subreddit.hot(limit=3)

for comments in subreddit.stream.comments():
    try:
        print(comments.body)
        
#        parent_id = str(comment.parent())
#        
#        original = reddit.comment(parent_id)
#        print('Parent:')
#        print(original.body)
#        print('Reply:')
#        print(comment.body)
        
    except Exception as e:
        print(str(e))