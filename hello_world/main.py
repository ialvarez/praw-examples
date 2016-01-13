import praw

r = praw.Reddit(user_agent='hello_world')
submissions = r.get_subreddit('opensource').get_hot(limit=5)
print [str(x) for x in submissions]
