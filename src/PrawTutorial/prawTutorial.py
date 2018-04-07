import praw

reddit = praw.Reddit(client_id = 'JLb3NDSQF7bu1Q',
	client_secret = 'S2iMASU9ePl6LxOhhs9D5pxBs2Y',
	username = 'GuusStaaf38',
	password = 'guus515838',
	user_agent = 'prawtutorialv1')

subreddit = reddit.subreddit('cryptocurrency')

hot_cryptocurrency = subreddit.submissions(1516797995, 1516970795)#.hot(limit=1)
#top_cryptocurrency = subreddit.top('year')

for submission in hot_cryptocurrency:
#    if not submission.stickied:
    print(submission.title)
    print(submission.score)
    print(submission.num_comments)
    print(submission.created_utc)
    print(submission.link_flair_text)
    
    submission.comments.replace_more(limit=0) #32 is max possible
    
    for comment in submission.comments.list(): 
        print(20*'-')
        print('Parent ID:', comment.parent())
        print('Comment ID:', comment.id)
        print(comment.created_utc)
        print('Comment score:', comment.score)
        print(comment.body)
