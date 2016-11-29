import praw

client_id = 'ba5De5oZ0xk3_w'
client_secret = 'WiHCIJH94JZOIhi0b81Nxgbfte8'

r = praw.Reddit(user_agent='hello_world',
                client_id=client_id,
                client_secret=client_secret)
submissions = r.subreddit('opensource').hot(limit=5)

print([str(x.title) for x in submissions])
