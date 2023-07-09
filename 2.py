import praw
import requests
import os

# Initialize a connection with the Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Target a specific subreddit for your wicked purpose
subreddit = reddit.subreddit('NSFW')

# Create a directory to store the diabolical images
storage_path = 'path/to/your/diabolical/storage/'
os.makedirs(storage_path, exist_ok=True)

# Iterate through the hot posts on the subreddit and download NSFW images
for submission in subreddit.hot(limit=10):
    if submission.over_18 and submission.url.endswith(('.jpg', '.png', '.gif')):
        image_url = submission.url
        image_data = requests.get(image_url).content
        image_extension = image_url.split('.')[-1]
        file_path = f'{storage_path}/{submission.id}.{image_extension}'
        with open(file_path, 'wb') as f:
            f.write(image_data)

# Revel in the malevolent satisfaction of your plundered images!
