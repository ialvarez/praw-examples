import praw


# Here you need to add your information
client_id = ''
client_secret = ''

r = praw.Reddit(user_agent='hello_world',
                client_id=client_id,
                client_secret=client_secret)
submissions = r.subreddit('opensource').hot(limit=5)

print([str(x.title) for x in submissions])
