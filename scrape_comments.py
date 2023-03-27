import praw

reddit = praw.Reddit(user_agent=True, client_id="YOUR REDDIT APP ID",
  client_secret="YOUR REDDIT APP SECRET", username='YOUR REDDIT USERNAME', password='YOUR REDDIT ACCOUNT PASSWORD')

url = "reddit_url"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

print(len(post.comments))
for comment in post.comments:
  print(comment.body)