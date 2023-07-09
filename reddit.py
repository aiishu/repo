import praw

# Establish a connection with the Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Target a specific subreddit for your wicked purpose
subreddit = reddit.subreddit('SUBREDDIT_NAME')

# Iterate through the hot posts on the subreddit and extract NSFW images
for submission in subreddit.hot(limit=10):
    if submission.over_18 and submission.url.endswith(('.jpg', '.png', '.gif')):
        # Save the NSFW image to your diabolical storage
        with open(f'{submission.id}.{submission.url.split(".")[-1]}', 'wb') as f:
            f.write(submission.url)
